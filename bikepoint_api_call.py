import requests
import os
from datetime import datetime
import json
import time
import logging


#Checking  logs folder exists. If it doesn't, folder is created
logs_dir = 'logs'
if os.path.exists(logs_dir):
    pass
else:
    os.mkdir(logs_dir)

#Filename variable with timestamp
filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#Create log filename variable
log_filename = f"logs/logging_example_{filename}.log"

#Logging config
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

#Logger config variable
logger = logging.getLogger()

# Documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk//BikePoint'

#Create variables for while check status code loop
number_of_tries = 3
count = 0

#Limit number of time API call retries
while count < number_of_tries:
    #Make API call and assign data to variable response_json and status code variable created
    response = requests.get(url, timeout=10)
    response_code = response.status_code

    #Wrapping folder, filename, filepath, write logic in an if that checks repsonse status code
    if response_code == 200:
        response_json = response.json()

        #Create variable for folder name
        dir = 'data'
        
        #Checking if data folder exists. If it doesn't, folder is created
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)

        #Created filepath using filename variable and folder variable
        filepath = f'{dir}/{filename}.json'

        try:
            #Writing data file
            with open(filepath, 'w') as file:
                json.dump(response_json,file)
            #Print success message
            print(f'Download successful at {filename} 😊')
            logger.info(f'Download successful at {filename} 😊') 
        except Exception as e:
            print(e)
            logger.error(f"An error occurred; {e}")             
        break

    elif response_code > 499 or response_code < 200:
        #Retry with 10 second wait
        print(response.reason)
        logger.warning(response.reason)        
        time.sleep(10)
        count += 1

    else:
        print(response.reason)
        logger.error(response.reason)             
        break