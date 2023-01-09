

from housing.entity.artifact_entity import ModelPusherArtifact,ModelEvaluationArtifact
from housing.config.configuration import ModelPusherConfig

from housing.exception import HousingException
from housing.logger import logging
import os,sys



class ModelPusher:

    def __init__(self,model_pusher_config:ModelPusherConfig,
                model_evaluation_artifact: ModelEvaluationArtifact
                ):
        try:
            logging.info(f"{'<<'*30} Model Pusher log started {'>>'*30}")
            self.model_pusher_config=model_pusher_config
            self.model_evaluation_artifact=model_evaluation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
    def export_model(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_model_pusher(self)->ModelPusherArtifact:
        try:
            return self.export_model()
        except Exception as e:
            raise HousingException(e,sys) from e

    def __del__(self):
        logging.info(f"{'<<'*30} Model Pusher log completed {'>>'*30}")