from housing.entity.config_entity import DataIngestionConfig
import os,sys
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile
from six.moves import urllib
import pandas as pd

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20} Data Ingestion Log Started {'='*20}")
            self.data_ingestion_config=data_ingestion_config
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    def download_housing_data(self)->str:
        try:
            #extraction remote url to download dataset
            download_url=self.data_ingestion_config.dataset_download_url

            #folder location to download file
            tgz_download_dir=self.data_ingestion_config.tgz_download_dir

            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)

            os.makedirs(tgz_download_dir)

            housing_file_name=os.path.basename(download_url)

            tgz_file_path=os.path.join(tgz_download_dir,housing_file_name)
            logging.info(f"Downloading file from :[{download_url}] into :[{tgz_file_path}]")
            logging.info(f"File : [{tgz_file_path}] has been downloaded successfully. ")
            urllib.request.urlretrieve(download_url,tgz_file_path)

            return tgz_file_path

        except Exception as e:
            raise HousingException(e,sys) from e

    def extract_tgz_file(self,tgz_file_path:str):
        try:
            raw_data_dir=self.data_ingestion_config.raw_data_dir
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir)

            logging.info(f"extracting tgz file : [{tgz_file_path}] into dir: [{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as housing_tgz_file_object:
                housing_tgz_file_object.extractall(path=raw_data_dir)
            logging.info(f"Extraction completed")

        except Exception as e:
            raise HousingException(e,sys) from e

    def split_data_as_train_test(self):
        try:
            raw_data_dir=self.data_ingestion_config.raw_data_dir
            file_name=os.listdir(raw_data_dir)[0]

            housing_file_path=os.path.join(raw_data_dir,file_name)
            housing_dataframe=pd.read_csv(housing_file_path)
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_Ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path=self.download_housing_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
        except Exception as e:
            raise HousingException(e,sys) from e