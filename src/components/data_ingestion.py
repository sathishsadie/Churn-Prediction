from src.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass
from src.exception import CustomException
import os
import sys

@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join("artifacts","train.csv")
    test_data_path : str = os.path.join("artifacts","test.csv")
    raw_data_path : str = os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def intiate_data_ingestion(self):
        logging.info("DataIngestion gets started ...")
        try:
            df = pd.read_csv("artifacts/customer_churn.csv")
            # logging.info("Data has been readed from the source.")
            os.makedirs(os.path.join(self.ingestion_config.train_data_path))
            os.makedirs(os.path.join(self.ingestion_config.test_data_path))
            os.makedirs(os.path.join(self.ingestion_config.raw_data_path))
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_data, test_data = train_test_split(df,test_size=.3,random_state=42)
            train_data.to_csv(self.ingestion_config.train_data_path)
            test_data.to_csv(self.ingestion_config.test_data_path)
            logging.info("Train and test data has been splited and saved in their directory ...")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)