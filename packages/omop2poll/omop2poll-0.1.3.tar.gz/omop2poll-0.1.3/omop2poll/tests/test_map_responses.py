from omop2poll.map_responses import map_responses
from unittest.mock import patch
import pandas as pd


def test_map_responses_correctly_maps():
    survey_data = pd.DataFrame({
        'question_concept_id': [43528661, 43528660],
        'answer_concept_id': [43529550, 903096],
        'answer_numeric': [0, -98],
        'answer_text': ['No', 'Skip']
    })

    input_data = pd.DataFrame({
        'question_concept_id': [43528661, 43528660],
        'answer_concept_id': [43529550, 903096],
    })

    with patch("omop2poll-a.load_data.load_survey_data", return_value=survey_data):
        result = map_responses(input_data)
        assert result['answer_numeric'].tolist() == [0, -98]
        assert result['answer_text'].tolist() == ['No', 'Skip']
