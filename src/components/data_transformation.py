from dataclasses import dataclass
import os
import sys
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_file_obj : str = os.path.join('artifacts/preprocessor.pkl')



class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self,data):
        try:
            num_cols = data.select_dtypes(['int','float']).columns
            cat_cols = data.select_dtypes(['object','category']).columns[1:]
            target_col = cat_cols[-1]
            cat_cols = cat_cols[:-1]
            
            num_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='mean')),
                    ('scaler',StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoder',OrdinalEncoder()),
                    ('target',StandardScaler())
                ]
            )
            target_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoder',OrdinalEncoder())
                ]
            )
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline',num_pipeline,num_cols),
                    ('cat_pipelin',cat_pipeline,cat_cols),
                    ('target',target_pipeline,target_col)
                ]
            )
            logging.info("Preprocessor has been created ...")
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_transformation(self,train_path,test_path):
        try : 
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Train and test data has been readed .")
            preprocessing_obj = self.initiate_data_transformation(self,train_df)
            train_arr = preprocessing_obj.fit_transform(train_df)
            test_arr = preprocessing_obj.transform(test_df)
            save_object(
                filepath = self.transformation_config.preprocessor_file_obj,
                obj = preprocessing_obj
            )
            logging.info("Data has been transformed and saved in the source ...")
            return (
                train_arr,
                test_arr,
                self.transformation_config.preprocessor_file_obj
            )
        except Exception as e:
            raise CustomException(e,sys)