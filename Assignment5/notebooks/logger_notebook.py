import logging
import os
from datetime import datetime


# Setting log directory
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M')}.log"
logs_dir = os.path.join("logs")

# Creating log directory
os.makedirs(logs_dir, exist_ok=True)

# Configuring full log path 
LOGS_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Rotating Handler: 5MB max size, keep 
# handler = RotatingFileHandler("mylog.log", maxBytes=5*1024*1024, backupCount=3)

# Configuring logging
logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format="%(message)s",
    level=logging.INFO
)

# # Testing if logging working
if __name__ == "__main__":
    logging.info("check logging")