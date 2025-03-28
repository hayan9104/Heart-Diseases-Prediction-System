'''import pickle
import pandas as pd

# Load the pre-trained scaler, label encoder, and model
def load_scaler():
    with open('myapp/ml/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return scaler

def load_label_encoder():
    with open('myapp/ml/label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    return label_encoder

def load_model():
    with open('myapp/ml/heart_diseases_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Prediction function
def predict(csv_file):
    # Load the CSV data into a DataFrame
    data = pd.read_csv(csv_file)

    # Preprocess the data
    scaler = load_scaler()
    label_encoder = load_label_encoder()
    model = load_model()

    # Assuming the label column is "target" (adjust as necessary)
    if 'target' in data.columns:
        data = data.drop(columns=['target'])

    scaled_data = scaler.transform(data)

    # Predict
    predictions = model.predict(scaled_data)

    # Decode labels
    decoded_predictions = label_encoder.inverse_transform(predictions)

    return decoded_predictions
'''