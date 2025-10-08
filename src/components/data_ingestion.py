import os
import pandas as pd 
from src.constant import APPLICATION_TRAIN_PATH
from src.logger import logging
from dataclasses import dataclass # koi bhi class define krna k liya hmm log init define krta h so newer python m usko hatana k liya we have something called data class
# __init__ is subsiitute of dataclass
from src.exception import CustomException
import sys
@dataclass
class DataIngestionConfig:
    artifact_folder: str = "artifacts"
    train_file_name: str = "application_train.csv"

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            os.makedirs(self.config.artifact_folder, exist_ok=True)
            logging.info(f"Created artifact folder at: {self.config.artifact_folder}")
            dst_path = os.path.join(self.config.artifact_folder, self.config.train_file_name)
            df = pd.read_csv(APPLICATION_TRAIN_PATH)
            df.to_csv(dst_path, index=False)
            logging.info(f"data saved to: {dst_path}")
            logging.info("Data Ingestion completed successfully")
        except Exception as e:
            logging.error(f"Error occured during Data Ingestion: {str(e)}")
            raise CustomException(e, sys)



if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()
    print("Data Ingestion process finished.")

    # abh ek kam karta h is script ko pehla test karat h tu test folder hamna pehla hee bnaya hua tha tu test karta h 