import pickle
import numpy as np


def load_model():

    model = pickle.load(open("models/trained_model.pkl", "rb"))

    return model


def predict_bankruptcy(features):

    model = load_model()

    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)

    if prediction[0] == 1:
        return "High Bankruptcy Risk"
    else:
        return "Low Bankruptcy Risk"