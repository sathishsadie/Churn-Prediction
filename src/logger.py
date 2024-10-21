import logging
import os
from datetime import datetime


log_file = f"{datetime.now().strftime('%m-%d-%Y-%H-%M')}.log"
log_path = os.path.join(os.getcwd(),'logs',log_file)
os.makedirs(log_path,exist_ok=True)


log_file_path = os.path.join(log_path,log_file)


logging.basicConfig(
    filename=log_file_path, 
    level=logging.INFO,
    format = '[%(asctime)s] %(lineno)d %(levelname)s - %(message)s'
)
if __name__=='__main__':
    logging.info("LOgging has been started.")