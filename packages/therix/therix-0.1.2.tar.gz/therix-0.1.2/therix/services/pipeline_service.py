import json
import os
import urllib
from therix.services.web_crawling import crawl_website
from therix.utils.rag import chat, create_embeddings, get_vectorstore
from ..db.session import SessionLocal
from ..entities.models import Pipeline, PipelineConfiguration
from therix.utils.rag import chat, create_embeddings, get_vectorstore


class PipelineService:
    def __init__(self):
        self.db_session = SessionLocal()

    def create_pipeline_with_configurations(self, pipeline_data, configurations_data):
        new_pipeline = Pipeline(**pipeline_data)
        self.db_session.add(new_pipeline)
        self.db_session.flush()  # Flush to assign an ID to the new_pipeline

        for config_data in configurations_data:
            config_data["pipeline_id"] = new_pipeline.id
            new_config = PipelineConfiguration(**config_data)
            self.db_session.add(new_config)

        self.db_session.commit()
        return new_pipeline

    def publish_pipeline(self, pipeline_data):
        pipeline = (
            self.db_session.query(Pipeline).filter_by(id=pipeline_data.id).first()
        )
        pipeline.status = "PUBLISHED"
        self.db_session.commit()
        return pipeline

    def get_pipeline(self, pipeline_id):
        return self.db_session.query(Pipeline).filter_by(id=pipeline_id).first()

    def get_pipeline_configurations(self, pipeline_id):
        return (
            self.db_session.query(PipelineConfiguration)
            .filter_by(pipeline_id=pipeline_id)
            .all()
        )

    def get_pipeline_configuraitons_by_type(self, pipeline_id, config_type):
        return (
            self.db_session.query(PipelineConfiguration)
            .filter_by(pipeline_id=pipeline_id, config_type=config_type)
            .all()
        )

    def preprocess_data(self, pipeline_id):
        data_sources = self.get_pipeline_configuraitons_by_type(
            pipeline_id, "INPUT_SOURCE"
        )
        output_file = None
        if "website" in data_sources[0].config:
            website_url = data_sources[0].config["website"]
            web_content = crawl_website(website_url)
            domain_name = urllib.parse.urlparse(website_url).netloc
            output_file = f"{domain_name}_data.json"
            with open(output_file, "w") as f:
                json.dump(web_content, f, indent=4)
            data_sources[0].config["files"] = [output_file]
        embedding_model = self.get_pipeline_configuraitons_by_type(
            pipeline_id, "EMBEDDING_MODEL"
        )
        create_embeddings(data_sources, embedding_model[0], str(pipeline_id))
        if "website" in data_sources[0].config:
            os.remove(output_file)

    def invoke_pipeline(self, pipeline_id, question, session_id, trace_details=None):
        embedding_model = self.get_pipeline_configuraitons_by_type(
            pipeline_id, "EMBEDDING_MODEL"
        )
        store = get_vectorstore(embedding_model[0], str(pipeline_id))
        retreiver = store.as_retriever()
        inference_model = self.get_pipeline_configuraitons_by_type(
            pipeline_id, "INFERENCE_MODEL"
        )
        return chat(
            question,
            retreiver,
            inference_model[0],
            embedding_model,
            session_id,
            pipeline_id,
            trace_details,
        )

    def __del__(self):
        self.db_session.close()
