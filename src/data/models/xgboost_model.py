from xgboost import XGBRegressor

class XGBoostModel:
    def __init__(self):
        self.model = XGBRegressor()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
