from mlProject.custom_logger import logger
from mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline



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



