from uuid import uuid4
from therix.core.pipeline_component import PipelineComponent
from .constants import DataSourceMaster, EmbeddingModelMaster  # Import your constants
from ..services.pipeline_service import PipelineService  # Import your service
from ..entities.models import ConfigType  # Import your ConfigType enum


class Pipeline:

    def __init__(self, name, status="IN_DRAFT"):
        self.pipeline_data = {"name": name, "status": status}
        self.components = []
        self.pipeline_service = PipelineService()

    @classmethod
    def from_id(cls, pipeline_id):
        pipeline = cls.__new__(cls)
        pipeline.__init__(None)
        pipeline.load(pipeline_id)
        return pipeline

    def add(self, component):
        if not isinstance(component, PipelineComponent):
            raise ValueError("component must be an instance of PipelineComponent")
        self.components.append(component)
        return self  # Enable method chaining

    def add_data_source(self, name, config):
        data_source = PipelineComponent(ConfigType.INPUT_SOURCE, name, config)
        return self.add(data_source)

    def add_embedding_model(self, name, config):
        embedding_model = PipelineComponent(ConfigType.EMBEDDING_MODEL, name, config)
        return self.add(embedding_model)

    def add_inference_model(self, name, config):
        inference_model = PipelineComponent(ConfigType.INFERENCE_MODEL, name, config)
        return self.add(inference_model)

    def add_output_source(self, name, config):
        output_source = PipelineComponent(ConfigType.OUTPUT_SOURCE, name, config)
        return self.add(output_source)

    def save(self):
        configurations_data = [
            {
                "config_type": component.type.value,
                "name": component.name,
                "config": component.config,
            }
            for component in self.components
        ]
        # Save the pipeline and its components to the database
        self.pipeline_data = self.pipeline_service.create_pipeline_with_configurations(
            self.pipeline_data, configurations_data
        )
        self.id = self.pipeline_data.id
        self.name = self.pipeline_data.name
        return self.pipeline_data

    def publish(self):
        return self.pipeline_service.publish_pipeline(self.pipeline_data)

    def load(self, pipeline_id):
        self.pipeline_data = self.pipeline_service.get_pipeline(pipeline_id)
        self.id = self.pipeline_data.id
        self.name = self.pipeline_data.name
        return self.pipeline_data

    def preprocess_data(self):
        self.pipeline_service.preprocess_data(self.pipeline_data.id)

    def invoke(self, question, session_id=None):
        if session_id == None:
            session_id = uuid4()
        pipeline_trace_config = (
            self.pipeline_service.get_pipeline_configuraitons_by_type(
                self.pipeline_data.id, ConfigType.TRACE_DETAILS
            )
        )
        if pipeline_trace_config:
            trace_details = pipeline_trace_config[0].config
        else:
            trace_details = None
        # trace_details = { "name": self.pipeline_data.name, "id": self.pipeline_data.id}
        answer = self.pipeline_service.invoke_pipeline(
            self.pipeline_data.id, question, session_id, trace_details
        )
        return {"answer": answer, "session_id": session_id}
