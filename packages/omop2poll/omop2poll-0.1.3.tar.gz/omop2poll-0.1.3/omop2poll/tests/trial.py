import os
import pandas as pd
from omop2poll.map_responses import map_responses
from omop2poll.recode_missing import recode_missing_values
from omop2poll.pivot_data import pivot_data_numeric,pivot_data_text
from omop2poll.codebook import generate_codebook, create_formatted_codebook, create_codebook, print_codebook
working_directory = 'C:/Users/elifd/PycharmProjects/omop2poll/omop2poll/'
os.chdir(working_directory)
fake_data = pd.read_csv('fake_healthcare_data.csv')

recoded_fake_data = map_responses(fake_data)
