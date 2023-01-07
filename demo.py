from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.exception import HousingException
import os,sys
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation

def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()

        # data_transformation_config=Configuration().get_data_transformation_config()
        # print(data_transformation_config)

        # schema_file_path=r"E:\My new World\Ineuron\ML Projects\ml_housing_project\config\schema.yaml"
        # file_path=r"E:\My new World\Ineuron\ML Projects\ml_housing_project\housing\artifact\data_ingestion\23-01-05-08-38-45\ingested_data\train\housing.csv"

        # df=DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)


    
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__=="__main__":
    main()