#import packages
import requests
import os
from datetime import datetime
import json
import time
import logging

#Creating variable for logs folder creation logic 
logs_dir = 'logs'

#Checking  logs folder exists. If it doesn't exist, a folder is created
if os.path.exists(logs_dir):
    pass
else:
    os.mkdir(logs_dir)

#Create filename variable containing run timestamp
filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#Create log filename variable that will create a new log file for each run
log_filename = f"logs/logging_example_{filename}.log"

#Logging config
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

#Create logger config variable
logger = logging.getLogger()

# Documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk//BikePoint'

#Create variables for while loop check status code test
number_of_tries = 3
count = 0

#While loop that ensures retires does not exceed number_of_retries variable above
while count < number_of_tries:

    #Make API call and status code variable created
    response = requests.get(url, timeout=10)
    response_code = response.status_code

    #Wrapping folder creation, filepath creation, file write logic into an if that checks repsonse status code is successful "== 200". Response reason will be returned if not 200.
    if response_code == 200:
        #Assign json data to variable
        response_json = response.json()

        #Create variable for data folder creation logic
        dir = 'data'

        #Checking if data folder exists. If it doesn't exist, a folder is created
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)

        #Created filepath using filename variable and folder variable
        filepath = f'{dir}/{filename}.json'

        #try/except block to provide information if there are any issues writing the file
        try:
            #Writing data file
            with open(filepath, 'w') as file:
                json.dump(response_json,file)
            #Print success message
            print(f'Download successful at {filename} 😊')
            #Logger will note a message if file write is successful
            logger.info(f'Download successful at {filename} 😊') 
        except Exception as e:
            print(e)
            #Logger will note exception error if file write is unsuccessful
            logger.error(f"An error occurred; {e}")             
        break

    elif response_code > 499 or response_code < 200:
        #Retry with 10 second wait
        print(response.reason)
        #Logger notes response reason when response code is 100s or 500s
        logger.warning(response.reason)     
        #The time.sleep function makes the script wait 10 seconds before retrying
        time.sleep(10)
        count += 1

    else:
        print(response.reason)
        #Logger notes response reason when response code is not 100s, 200s, 500s
        logger.error(response.reason)             
        break