import pytest
from omop2poll.pivot_data import pivot_data_numeric
import pandas as pd
import os


def test_pivot_data_numeric_creates_correct_output(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    sample_file = d / "test.csv"
    sample_data = "respondent_id,question_concept_id,answer_numeric\n1,100,5\n2,100,6"
    sample_file.write_text(sample_data)

    expected_output_path = d / "pivot_n_test.csv"
    expected_output_file = str(expected_output_path)

    pivot_data_numeric(str(sample_file))

    assert os.path.exists(expected_output_file), "The expected pivoted output file does not exist."

    expected_df = pd.DataFrame({
        'q100': [5, 6]
    }, index=[1, 2])
    expected_df.index.name = 'respondent_id'
    output_df = pd.read_csv(expected_output_file, index_col='respondent_id')

    pd.testing.assert_frame_equal(output_df, expected_df)

