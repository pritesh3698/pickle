# predictor.py

import pickle
import pandas as pd

def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def make_predictions(model, new_data_path):
    new_data = pd.read_csv(new_data_path)
    predictions = model.predict(new_data)
    return predictions

if __name__ == "__main__":
    # Define paths
    model_path = 'model.pkl'
    new_data_path = 'new_data.csv'

    # Load the model
    model = load_model(model_path)

    # Make predictions
    predictions = make_predictions(model, new_data_path)

    # Print or use predictions as needed
    print("Predictions:", predictions)
