from sklearn.ensemble import IsolationForest
import numpy as np


def train_model():

    training_data = np.array([
        [1, 1, 10],
        [1, 1, 10],
        [1, 2, 50],
        [2, 2, 50],
        [3, 3, 85],
        [4, 3, 80],
        [5, 1, 10],
        [1, 1, 10],
        [2, 2, 50],
        [3, 3, 85]
    ])

    model = IsolationForest(
        contamination=0.2,
        random_state=42
    )

    model.fit(training_data)

    return model


if __name__ == "__main__":

    model = train_model()

    test_data = np.array([
        [10, 10, 100]
    ])

    prediction = model.predict(test_data)

    print("AI Threat Prediction:")
    print(prediction)
