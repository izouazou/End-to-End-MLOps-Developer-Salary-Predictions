import pandas as pd
import os
from mlProject.custom_logger import logger
from catboost import CatBoostRegressor
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from mlProject.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        categorical_transformer = Pipeline([('one_hot_encode', OneHotEncoder(handle_unknown='ignore', sparse_output=False))])
        original_columns = ['Country', 'Age', 'EdLevel', 'RemoteWork', 'DevType', 'OrgSize', 'YearsCodePro']
        preprocessor = ColumnTransformer(transformers=[('categorical', categorical_transformer, original_columns)],remainder='passthrough')
        data_processing_pipeline = Pipeline([('preprocessor', preprocessor)])
        
        train_x = data_processing_pipeline.fit_transform(train_x)
        test_x = data_processing_pipeline.transform(test_x)


        model = CatBoostRegressor(depth=self.config.depth, l2_leaf_reg=self.config.l2_leaf_reg,
                                  learning_rate=self.config.learning_rate, verbose=self.config.verbose
                                )
        model.fit(train_x, train_y)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
        joblib.dump(data_processing_pipeline, os.path.join(self.config.root_dir, self.config.preprocessor))

