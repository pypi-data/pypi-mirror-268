import pytest
from unittest.mock import patch, mock_open
from omop2poll.load_data import load_survey_data
import pandas as pd


def test_load_survey_data_file_not_found():
    with patch("os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError):
            load_survey_data("nonexistent_file.csv")


def test_load_survey_data_reads_correctly():
    data = "col1,col2\nval1,val2"
    expected_df = pd.DataFrame({"col1": ["val1"], "col2": ["val2"]})

    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.return_value = expected_df
        with patch("os.path.exists", return_value=True):
            df = load_survey_data("dummy_file.csv")
            mock_read_csv.assert_called_once()  # Ensures pandas.read_csv was called
            pd.testing.assert_frame_equal(df, expected_df)
