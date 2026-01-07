import requests
import os
from datetime import datetime
import json

# Documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk//BikePoint'

#Make API call and assign data to variable response_json
response = requests.get(url, timeout=10)
response_json = response.json()

#Create variable for folder name
dir = 'data'

#Checking if folder exists. If it doesn't, folder is created
if os.path.exists(dir):
    pass
else:
    os.mkdir(dir)

#Creating filename using timestamp
filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#Created filepath using filename variable and folder variable
filepath = f'{dir}/{filename}.json'

#Writing data file
with open(filepath, 'w') as file:
    json.dump(response_json,file)

#Write success message
print(f'Download successful at {filename} 😉')
