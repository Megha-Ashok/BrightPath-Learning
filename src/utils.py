import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score

def save_object(file_path,obj):
  try:
    dir_path=os.path.dirname(file_path)
    os.makedirs(dir_path,exist_ok=True)
    with open(file_path,"wb") as file_obj:
      dill.dump(obj,file_obj)  # saving pkl file in hard disk
      
  except Exception as e:
    raise CustomException(e,sys)
  

def model_evaluator(x_train, y_train, x_test, y_test, models):
    model_score=[]
    model_list=[]
    
    for key,model in models.items():
      model.fit(x_train,y_train)
      train_predicted=model.predict(x_train)
      test_predicted=model.predict(x_test)
      
      train_r2=r2_score(y_train,train_predicted)
      test_r2=r2_score(y_test,test_predicted)
      model_list.append(model)
      model_score.append(test_r2)
    return model_list, model_score
