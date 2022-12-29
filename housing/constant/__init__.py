import os
from datetime import datetime

ROOT_DIR=os.getcwd()
print(ROOT_DIR)
CONFIG_DIR="config"
CONFIG_FILE_NAME="config.yaml"
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
print(CONFIG_FILE_PATH)

CURRENT_TIME_STAMP=f"{datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"

# Training pipeline related variables

TRAINING_PIPELINE_CONFIG_KEY="training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY="artifact_dir"
TRAINING_PIPELINE_NAME_KEY="pipeline_name"

# Data Ingestion related variables

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR="data_ingestion"
DATA_INGESTION_DWONLOAD_URL_KEY="dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR="raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY="tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY="ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY="ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY="ingested_test_dir"