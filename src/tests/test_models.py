import pytest
from src.models.lstm_model import LSTMModel

def test_lstm_model():
    model = LSTMModel()
    X = [[[i] for i in range(10)]]
    y = [1]
    model.train(X, y)
    predictions = model.predict(X)
    assert len(predictions) == len(X)
