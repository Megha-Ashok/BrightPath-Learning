import os
import sys
from dataclasses import dataclass 
from sklearn.linear_model import Lasso, Ridge
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor  

from src.utils import model_evaluator, save_object
from src.exception import CustomException
from src.logger import logging

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting train and test data")

            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(),  
                "AdaBoost Regressor": AdaBoostRegressor()
            }

            # Evaluate models
            model_name,model_score = model_evaluator(x_train, y_train, x_test, y_test, models)
            logging.info(f"Model scores: {model_score}")
            # Find the best model
            best_model_score = max(model_score)  
            best_model = model_name[model_score.index(best_model_score)]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info(f"Best model found: {best_model} with score {best_model_score}")

            # Save the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_path,
                obj=best_model
            )

            # Make predictions with the best model
            predicted = best_model.predict(x_test)
            r2_square = r2_score(y_test, predicted)
            logging.info(f"average score is {r2_square}")
            return r2_square

        except Exception as e:
            raise CustomException(e, sys)
