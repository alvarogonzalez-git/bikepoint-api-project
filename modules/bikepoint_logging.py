# Import libraries
import logging
import os
from datetime import datetime

def logging_function(prefix, timestamp):
    '''
    Function that set up desired logs
    
    :param prefix: For the folder name for the logs
    :param timestamp: For the name of the log files
    '''

    # Create logs_dir name based on prefix parameter
    data_dir = (f'{prefix}_logs')
    os.makedirs(data_dir, exist_ok = True)

    #Create log filename variable that will create a new log file for each run
    log_filename = (f"{data_dir}/{timestamp}.log")

    #Logging config
    logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
    )

    return logging.getLogger()