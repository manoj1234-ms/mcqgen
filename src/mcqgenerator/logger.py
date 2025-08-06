import logging
import os
from datetime import datetime

# create LOG_FILE that stores logging data
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#get the path of folders
log_path = os.path.join(os.getcwd(), "logs")

#create a dir
os.makedirs(log_path, exist_ok=True)

#join the dir with path
LOG_FILE_Path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    level= logging.INFO,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
