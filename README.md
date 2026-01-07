# BikePoint Data Pipeline

This project was completed as a part of The Information Lab's Data Engineering School. It was incrementally developed on a weekly basis by applying the core skills that correspond to the main stages in the Data Engineering lifecycle: Extract, Transform and Load (ETL). The data for this project comes from Transport for London's (TfL) Unified API. This readme is divided into sections that provide more detail on each stage of development

* Extract - ingesting data via API call in python script 🐍
* Transform
* Load

---

## Extract
This project uses BikePoint data for Transport for London's Santander Cycles. They make this data available via their Unified API. The data was ingested using the following python script - `bikepoint_api_call.py`.

### bikepoint_api_call.py
This script calls the API and writes a .json file into our data folder. The script has robust error handling and logging features to allow monitoring of the scripts performance.
