from src.data.data_loader import load_data
from src.data.preprocess import preprocess_data
from src.ensemble.stacking_ensemble import StackingEnsemble

if __name__ == "__main__":
    data = load_data("data/stock_prices.csv")
    data = preprocess_data(data)

    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    ensemble = StackingEnsemble()
    ensemble.train(X, y)
    predictions = ensemble.predict(X)
    print("Predictions:", predictions)
