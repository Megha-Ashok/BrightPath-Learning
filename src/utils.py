import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.logger import logging
def save_object(file_path,obj):
  try:
    dir_path=os.path.dirname(file_path)
    os.makedirs(dir_path,exist_ok=True)
    with open(file_path,"wb") as file_obj:
      dill.dump(obj,file_obj)  # saving pkl file in hard disk
      
  except Exception as e:
    raise CustomException(e,sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        model_list = []
        model_score = []

        for key, model in models.items():  
            para = param.get(key, {})  

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            model_list.append(model)
            model_score.append(test_model_score)
            logging.info("hypertuning is  done")
        return model_list, model_score

    except Exception as e:
        raise CustomException(e, sys)  
