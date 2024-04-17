import pandas as pd
import os

def load_data(input_data):
    if isinstance(input_data, pd.DataFrame):
        return input_data
    elif input_data.endswith('.csv') or input_data.endswith('.txt'):
        return pd.read_csv(input_data)
    elif input_data.endswith('.xlsx') or input_data.endswith('.xls'):
        return pd.read_excel(input_data)
    else:
        raise ValueError("Unsupported file format or data type.")

def pivot_data_numeric(input_data):
    data = load_data(input_data)
    pivot_df = data.pivot_table(index='respondent_id',
                                columns='question_concept_id',
                                values='answer_numeric',
                                aggfunc='first')
    pivot_df.columns = ['q' + str(col) for col in pivot_df.columns]

    if isinstance(input_data, pd.DataFrame):
        print("Data pivoted. You can further process or save the DataFrame as needed.")
        return pivot_df
    else:
        dir_name = os.path.dirname(input_data)
        new_filename = 'pivot_n_' + os.path.basename(input_data)
        new_filepath = os.path.join(dir_name, new_filename)
        pivot_df.to_csv(new_filepath)
        print(f"Pivoted dataset with numeric values saved as: {new_filepath}")

def pivot_data_text(input_data):
    data = load_data(input_data)
    pivot_df = data.pivot_table(index='respondent_id',
                                columns='question_concept_id',
                                values='answer_text',
                                aggfunc='first')
    pivot_df.columns = ['q' + str(col) for col in pivot_df.columns]

    if isinstance(input_data, pd.DataFrame):
        print("Data pivoted. You can further process or save the DataFrame as needed.")
        return pivot_df
    else:
        dir_name = os.path.dirname(input_data)
        new_filename = 'pivot_t_' + os.path.basename(input_data)
        new_filepath = os.path.join(dir_name, new_filename)
        pivot_df.to_csv(new_filepath)
        print(f"Pivoted dataset with text values saved as: {new_filename}")
