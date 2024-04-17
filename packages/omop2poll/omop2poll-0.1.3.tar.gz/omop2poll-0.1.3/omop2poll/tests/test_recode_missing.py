from omop2poll.recode_missing import recode_missing_values
import pytest


def test_recode_missing_values_unsupported_file_type():
    with pytest.raises(ValueError):
        recode_missing_values("unsupported_file_type.txt")
