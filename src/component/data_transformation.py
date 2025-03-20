import os
import sys
from src.logger import logging
from src.exception import CustomException
import numpy as np
import pandas as pd
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer  # For missing value handling
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.utils import save_object

class dataTransformationConfig:
    preprocessing_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")
    
class dataTransformation:
    def __init__(self):
        self.data_transform_config = dataTransformationConfig()
     
    def get_data_transformed_object(self):
        "This function is for preparing data for transformation"
        try:
            # Define columns
            numerical_column = ['reading_score', 'writing_score']
            categorical_column = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            
            # Numerical Pipeline
            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            
            # Categorical Pipeline
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            
            # Column Transformer combines both pipelines
            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_column),
                    ("categorical_pipeline", categorical_pipeline, categorical_column)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            logging.info("Obtained preprocessing object")
            preprocessing_obj = self.get_data_transformed_object()
            
            # Specify target column
            target_column = ["math_score"]
            numerical_column = ['reading_score', 'writing_score']      
            
            # Separate input features and target
            input_feature_train_df = train_df.drop(columns=target_column, axis=1)
            target_train_df = train_df[target_column]
            input_feature_test_df = test_df.drop(columns=target_column, axis=1)
            target_test_df = test_df[target_column]
            
            logging.info("Applying preprocessing object on train and test dataframe.")
            
            # Transform features using the preprocessor
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            
            # Combine transformed features with target
            train_arr = np.c_[input_feature_train_arr, np.array(target_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_test_df)]
        
            logging.info("Saved all preprocessing objects.")
            
            save_object(
                file_path=self.data_transform_config.preprocessing_obj_file_path,
                obj=preprocessing_obj
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transform_config.preprocessing_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)
