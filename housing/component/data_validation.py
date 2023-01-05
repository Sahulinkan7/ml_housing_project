from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig
from housing.exception import HousingException
from housing.entity.artifact_entity import DataIngestionArtifact
import os,sys

class DataValidation:

    def __init__(self,data_validation_config:DataValidationConfig,
        data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

    def is_train_test_file_exists(self)-> bool:
        try:
            logging.info("Checking if training and test file are Available ? ")
            is_train_file_exists=False
            is_test_file_exists=False

            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            is_train_file_exists=os.path.exists(train_file_path)
            is_test_file_exists=os.path.exists(test_file_path)

            is_available=is_train_file_exists and is_test_file_exists
            logging.info(f"Is train and test file exists ? -> {is_available}")

            if not is_available:
                trainig_file=self.data_ingestion_artifact.train_file_path
                testing_file=self.data_ingestion_artifact.test_file_path
                message=f"Trainig file: {trainig_file} or Testing file {testing_file} is not available"
                raise Exception(message)

            

            return is_available
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def validate_dataset_schema(self):
        try:
            valdiation_status=False

            return valdiation_status
        except Exception as e:
            raise HousingException(e,sys)

    def initiate_data_validation(self):
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()

        except Exception as e:
            raise HousingException(e,sys)

    
    


