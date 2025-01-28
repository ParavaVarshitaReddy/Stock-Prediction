import tensorflow as tf

class LSTMModel:
    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.LSTM(50, return_sequences=True, input_shape=(10, 1)),
            tf.keras.layers.Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mse')

    def train(self, X, y):
        self.model.fit(X, y, epochs=10)

    def predict(self, X):
        return self.model.predict(X)
