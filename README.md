# Apache-Beam-Pipeline Skeleton
This is a skeleton of Apache Beam Pipeline for handling csv data.

## Local setup
1. Create virtual environment  **python -m venv venv** (windows) or **python3 -m venv venv** (unix). If you are using *virtualenv* you can **virtualenv venv**
2. Activate it - **venv\Scripts\activate** (windows) \ **source venv/bin/activate** (unix)
3. Install the dependencies - **pip install -r requirements.txt**
4. Running **python -m process** should start the execution of the pipeline

## Project Tour

As already mentioned this is just a skeleton and the GCP needs to be configured and the validation and transformations implemented. 

Still when you run process.py you can see a lot of stuff happening. 

### 1. Pipeline configuration and main process

Apache beam pipeline is defined in *process.py*, which is what we execute. It triggers the reading of the csv files, the parsing, the validation and the transformation. Once they are over we can write to Postgres. 

The aforementioned processes are separated into different modules.

### 2. Utils
Generic module for utilies. 
- csv_utils.py:
  
    parse_csv - currentlty the only active util we need. This map a single row values to correct columns extracted from the csv file and make sure they are the correct type.

### 3. Mappings
A place to store the different configurations and mappings based on the csv file type. Currently we only support "partners_data" type but having it store here make the code reusable and easier to maintain.  

- csv_files mappings - currently we only need CSV_MAPPING_COLUMNS to extract the columns names and the numeric type columns
- schemas mappings - the pg schema(string) for the different csv types we ingest. 

### 4. Validators 
A module for validating the data after parse. 

### 5. Transformators

A module for transforming data after and validation. 
