import pytest
from omop2poll.pivot_data import pivot_data_text
import pandas as pd
import os


def test_pivot_data_text_creates_correct_output(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    sample_text_file = d / "test_text.csv"
    sample_text_data = "respondent_id,question_concept_id,answer_text\n1,100,Yes\n2,100,No"
    sample_text_file.write_text(sample_text_data)

    expected_text_path = d / "pivot_t_test_text.csv"
    expected_text_file = str(expected_text_path)

    pivot_data_text(str(sample_text_file))

    assert os.path.exists(expected_text_file), "The expected pivoted output file does not exist."

    expected_text_df = pd.DataFrame({
        'q100': ['Yes', 'No']
    }, index=[1, 2])
    expected_text_df.index.name = 'respondent_id'
    output_text_df = pd.read_csv(expected_text_file, index_col='respondent_id')

    pd.testing.assert_frame_equal(output_text_df, expected_text_df)
