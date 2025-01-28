import pytest
from src.data.preprocess import preprocess_data
import pandas as pd

def test_preprocess_data():
    data = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, None]})
    processed = preprocess_data(data)
    assert not processed.isnull().values.any()
