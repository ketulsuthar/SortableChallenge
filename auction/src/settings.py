"""
created_by : Ketulkumar suthar
created_date : 1st November 2020
"""
import os
import pathlib

CONFIG_FILE_PATH = pathlib.Path(__file__).parent / 'config.json'


SCHEMA_CONFIG_PATH = pathlib.Path(__file__).parent / 'schema/config_schema.json'
SCHEMA_INPUT_PATH = pathlib.Path(__file__).parent / 'schema/input_schema.json'

    #os.path.join(os.path.dirname(__file__),'../schema/config_schema.json')