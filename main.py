# Import libraries
from modules.bikepoint_logging import logging_function
from modules.bikepoint_extract import extract_function
from modules.bikepoint_load import load_function
from datetime import datetime
from dotenv import load_dotenv
import os
from pathlib import Path

# Define Runtime timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# Documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk//BikePoint'


# Load .env file
load_dotenv()

# Assign keys to variables
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# Create logger to be fed into extract function
extract_logger = logging_function('extract', timestamp)

# Extract data from BikePoint, save to "data" folder and log
extract_function(url, 3, extract_logger, timestamp)

# Create logger to be fed into extract function
load_logger = logging_function('load', timestamp)

# Extract data from BikePoint, save to "data" folder and log
load_function('data', AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, load_logger)