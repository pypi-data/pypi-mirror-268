from omop2poll.codebook import create_codebook, print_codebook
import pandas as pd
from unittest.mock import patch
import io


def test_print_codebook(capsys):

    df = pd.DataFrame({
        'question_concept_id': [1, 2],
        'question': ['Q1', 'Q2'],
        'answer_concept_id': [10, 20],
        'answer_numeric': [0, 1],
        'answer_text': ['No', 'Yes']
    })

    codebook_df = create_codebook(df)

    print_codebook(codebook_df)

    captured = capsys.readouterr()
    assert "Q1" in captured.out
    assert "No" in captured.out
