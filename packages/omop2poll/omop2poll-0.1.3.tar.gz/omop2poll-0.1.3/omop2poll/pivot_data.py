import pandas as pd
import os


def pivot_data_numeric(filename):
    if not os.path.exists(filename):
        print(f"The specified file {filename} does not exist.")
        return

    data = pd.read_csv(filename)
    pivot_df = data.pivot_table(index='respondent_id',
                                columns='question_concept_id',
                                values='answer_numeric',
                                aggfunc='first')

    pivot_df.columns = ['q' + str(col) for col in pivot_df.columns]
    dir_name = os.path.dirname(filename)
    new_filename = 'pivot_n_' + os.path.basename(filename)
    new_filepath = os.path.join(dir_name, new_filename)
    pivot_df.to_csv(new_filepath)

    print(f"Pivoted dataset with numeric values saved as: {new_filepath}")


def pivot_data_text(filename):
    if not os.path.exists(filename):
        print(f"The specified file {filename} does not exist.")
        return

    data = pd.read_csv(filename)
    pivot_df = data.pivot_table(index='respondent_id',
                                columns='question_concept_id',
                                values='answer_text',
                                aggfunc='first')

    pivot_df.columns = ['q' + str(col) for col in pivot_df.columns]
    dir_name = os.path.dirname(filename)
    new_filename = 'pivot_t_' + os.path.basename(filename)
    new_filepath = os.path.join(dir_name, new_filename)
    pivot_df.to_csv(new_filepath)

    print(f"Pivoted dataset with text values saved as: {new_filename}")
