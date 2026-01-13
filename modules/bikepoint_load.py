# Import libraries
import os
import boto3

# Defining function to load .json data to S3 bucket
def load_function(data_dir, AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, logger):
    '''
    Loads .json files from data_dir to S3 bucket.
    
    :param data_dir: local directory containing extracted .json files
    :param AWS_ACCESS_KEY: aws access key
    :param AWS_SECRETS_KEY: aws secrets key
    :param AWS_BUCKET_NAME: S3 bucket name
    :param logger: assigns logger to function
    '''

    # Setting s3 client with authentication keys
    s3_client = boto3.client(
        's3'
        , aws_access_key_id = AWS_ACCESS_KEY
        , aws_secret_access_key = AWS_SECRET_KEY
    )

    # Assign data filepath to a variable
    data_dir = 'data'

    # Checks if folder is empty
    if len(os.listdir(data_dir)) == 0:
        print(f"The '{data_dir}' folder is empty.")
        logger.info(f"The '{data_dir}' folder is empty.") 

    else:
        print("The folder contains files.")

        # os.listdir returns everything in the folder (files and folders)
        all_items = os.listdir(data_dir)

        # Filter for files only
        file_list = []

        # Loops through all items in the data folder and adds them to a list
        for item in all_items:
            # Creates filepath for each file
            full_path = os.path.join(data_dir, item)
            # If file exists, append to the empty list
            if os.path.isfile(full_path):
                file_list.append(item)

        for filename in file_list:
            # Recreate the full path relative to the script for upload loop
            full_path = os.path.join(data_dir, filename)

            try:
                # Upload the file
                    # 1. Path of data folder
                    # 2. s3 bucket name
                    # 3. Name of the file you want to upload
                s3_client.upload_file(full_path, AWS_BUCKET_NAME, filename)
                print(f"Uploaded {filename}")
                logger.info(f"Uploaded and deleted local copy: {filename}") 
                
                # Delete the local file ONLY if the line above succeeds
                os.remove(full_path)
                print(f"Uploaded and deleted local copy: {filename}")
                logger.info(f"Uploaded and deleted local copy: {filename}") 

                
            except Exception as e:
                # If upload fails, the code jumps here, and the file is NOT deleted
                print(f"Failed to upload {filename}: {e}")
                logger.error(f"Failed to upload {filename}: {e}") 
