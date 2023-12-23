from mlProject.custom_logger import logger
from mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline


def run_training_pipeline(stage_name, pipeline_class):
    try:
        logger.info(f"------  {stage_name} started  ------") 
        pipeline = pipeline_class()
        pipeline.main()
        logger.info(f"------  {stage_name} completed  ------\n\n||==========||")
    except Exception as e:
        logger.exception(e)
        raise e

run_training_pipeline("Data Ingestion stage", DataIngestionTrainingPipeline)
run_training_pipeline("Data Validation stage", DataValidationTrainingPipeline)
run_training_pipeline("Data Transformation stage", DataTransformationTrainingPipeline)
run_training_pipeline("Model Trainer stage", ModelTrainerTrainingPipeline)
run_training_pipeline("Model Evaluation stage", ModelEvaluationTrainingPipeline)




