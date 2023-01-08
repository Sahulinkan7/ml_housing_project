from housing.exception import HousingException
import os,sys
import yaml
from housing.logger import logging
from collections import namedtuple
from typing import List
import importlib

GRID_SEARCH_KEY = 'grid_search'
MODULE_KEY = 'module'
CLASS_KEY = 'class'
PARAM_KEY = 'params'
MODEL_SELECTION_KEY = 'model_selection'
SEARCH_PARAM_GRID_KEY = "search_param_grid"

BestModel = namedtuple("BestModel", ["model_serial_number",
                                     "model",
                                     "best_model",
                                     "best_parameters",
                                     "best_score", ])

InitializedModelDetail = namedtuple("InitializedModelDetail",
                                    ["model_serial_number", "model", "param_grid_search", "model_name"])

class ModelFactory:
    def __init__(self,model_config_path: str=None):
        try:
            self.config=ModelFactory.read_params(model_config_path)
            
            self.grid_search_cv_module: str=self.config[GRID_SEARCH_KEY][MODULE_KEY]
            self.grid_search_class_name: str=self.config[GRID_SEARCH_KEY][CLASS_KEY]
            self.grid_search_property_data: dict=dict(self.config[GRID_SEARCH_KEY][PARAM_KEY])

            self.model_initialization_config: dict=dict(self.config[MODEL_SELECTION_KEY])

            self.model_initialized_list=None
            self.grid_searched_best_model_list=None

        except Exception as e:
            raise HousingException(e,sys) from e
    @staticmethod
    def read_params(config_path:str)->dict:
        try:
            with open(config_path) as yaml_file:
                config:dict=yaml.safe_load(yaml_file)
            return config
        except Exception as e:
            raise HousingException(e,sys) from e

    @staticmethod
    def class_for_name(module_name:str,class_name:str):
        try:
            #load module ,will raise importError if module can not be loaded
            module=importlib.import_module(module_name)

            #get the class,will raise attributeError if class can not be found
            logging.info(f"Executing command : from {module} import {class_name}")
            class_ref=getattr(module,class_name)
            return class_ref
            
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_initialized_model_list(self)->List[InitializedModelDetail]:
        """
        This function will return a list of model details.
        return List[ModelDetail]
        """

        try:
            initialized_model_list=[]


        except Exception as e:
            raise HousingException(e,sys) from e

    def get_best_model(self,x,y,base_accuracy=0.6)-> BestModel:
        try:
            logging.info(f"Started Initializing model from config file")
            initialized_model_list=self.get_initialized_model_list()
        except Exception as e:
            raise HousingException(e,sys)

