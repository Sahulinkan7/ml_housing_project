from housing.entity.config_entity import ModelTrainerConfig
from housing.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from housing.exception import HousingException
import sys
from housing.logger import logging
from housing.util.util import load_numpy_array_data
from housing.entity.model_factory import ModelFactory

class ModelTrainer:
    
    def __init__(self,model_trainer_config:ModelTrainerConfig,data_transformation_artifact: DataTransformationArtifact):
        try:
            logging.info(f"{'<<'*20} Model Trainer log started {'>>'*20}")
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            logging.info(f"Loading transformed training dataset")
            transformed_train_file_path=self.data_transformation_artifact.transformed_train_file_path
            train_array=load_numpy_array_data(file_path=transformed_train_file_path)

            logging.info(f"Loading transfored testing dataset")
            transformed_test_file_path=self.data_transformation_artifact.transformed_test_file_path
            test_array=load_numpy_array_data(transformed_test_file_path)

            logging.info(f"Splitting training and testing input and target feature")
            x_train,y_train,x_test,y_test=train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1]

            logging.info(f"Extracting model config file path")
            model_config_file_path=self.model_trainer_config.model_config_file_path

            logging.info(f"Initializing model factory class using above model config file: {model_config_file_path}")
            model_factory=ModelFactory(model_config_path=model_config_file_path)

            base_accuracy=self.model_trainer_config.base_accuracy
            logging.info(f"Expected accuracy: {base_accuracy}")

            logging.info(f"Initiating operation model selection")
            best_model=model_factory.get_best_model(x=x_train,y=y_train,base_accuracy=base_accuracy)

            model_trainer_artifact=ModelTrainerArtifact()

            return model_trainer_artifact
        except Exception as e:
            raise HousingException(e,sys) from e