import requests
import os
import json
import time

def extract_function(url, number_of_tries, logger, timestamp):
    '''
    Designed for extracting data for TfL BikePoints
    
    :param url: API call URL
    :param number_of_tries: max number of times API retries connection
    :param logger: assigns logger to function
    :param timestamp: runtime timestamp
    '''

    count = 0

    #While loop that ensures retires does not exceed number_of_retries variable above
    while count < number_of_tries:

        #Make API call and status code variable created
        response = requests.get(url, timeout=10)
        response_code = response.status_code

        #Wrapping folder creation, filepath creation, file write logic into an if that checks response status code is successful "== 200". Response reason will be returned if not 
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
            filepath = f'{dir}/{timestamp}.json'

            #try/except block to provide information if there are any issues writing the file
            try:
                #Writing data file
                with open(filepath, 'w') as file:
                    json.dump(response_json,file)
                #Print success message
                print(f'Download successful at {timestamp} 😊')
                #Logger will note a message if file write is successful
                logger.info(f'Download successful at {timestamp} 😊') 
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