import os
import sys
from src.logger import logging
from src.exception import CustomException
import numpy as np
import pandas as pd
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer # for missing value handling
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.utils import save_object

class dataTransformationConfig:
    preprocessing_obj_file_path=os.path.join("artifacts","preprocessor.pkl")
    
class dataTransformation:
  def __init__(self):
     self.data_transform_config=dataTransformationConfig()
     
  def get_data_transformed_object(self):
    "This function is for preparing data for transformation"
    try:
      numerical_column=['reading_score','writing_score']
      categorial_column=[
        "gender",
        "race_ethnicity",
        "parental_level_of_education",
        "lunch",
        "test_preparation_course"
      ]
      numerical_pipeline=Pipeline(
       steps=[ 
        ("imputer",SimpleImputer(strategy="median")),
        ("Scaler",StandardScaler(with_mean=False))
       ]
      )
      
      categorial_pipeline=Pipeline(
        steps=[ 
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),  # Ensure dense output
        ("Scaler", StandardScaler(with_mean=False))  # Keep with_mean=False
       ]
      )

      preprocessor=ColumnTransformer(
        [
          ("numerical_pipeline",numerical_pipeline,numerical_column),
          ("categorical_pipeline",categorial_pipeline,categorial_column)
        ]
      )
      return preprocessor
    except Exception as e:
      raise CustomException(e,sys)
    
  def initiate_data_transformation(self,train_path,test_path):
    try:
      train_df=pd.read_csv(train_path)
      test_df=pd.read_csv(test_path)
      logging.info("Read train and test data completed")
      logging.info("obtained preprocessing object")
      preprocessing_obj=self.get_data_transformed_object()
      
      target_column=["math_score"]
      numerical_column=['reading_score','writing_score']      
      input_feature_train_df=train_df.drop(columns=train_df[target_column],axis=1)
      target_train_df=train_df[target_column]
      input_feature_test_df=test_df.drop(columns=test_df[target_column],axis=1)
      target_test_df=test_df[target_column]
      
      logging.info(
        f"Applying preprocessing object on train and test dataframe."
      )
      
      
      input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
      input_feature_test_arr=preprocessing_obj.transform(input_feature_train_df)
      train_arr=np.c_[input_feature_train_arr,np.array(target_train_df)]
      test_arr=np.c_[input_feature_test_df,np.array(target_test_df)]
    
      logging.info(f"saved all preprocessing objects.")
      
      save_object(
        file_path= self.data_transform_config.preprocessing_obj_file_path,
        obj=preprocessing_obj
      )
      
      return(
      train_arr,
      test_arr,
      self.data_transform_config.preprocessing_obj_file_path
      ) 
    except Exception as e:
      raise CustomException(e,sys)
  
    
