import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define relative paths
data_path = os.path.join(BASE_DIR, 'data', 'heart_disease_ml_ready.csv')
imputed_data_path = os.path.join(BASE_DIR, 'data', 'heart_disease_imputed_clinical.csv')
model_path = os.path.join(BASE_DIR, 'models', 'heart_disease_model.pkl')
scaler_path = os.path.join(BASE_DIR, 'models', 'scaler.pkl')
label_encoder_path = os.path.join(BASE_DIR, 'models', 'label_encoder.pkl')

# Load the dataset
heart_data = pd.read_csv(data_path)

# Function to fill missing values (same as before)
def fill_missing_values(df):
    # Logical imputation based on domain knowledge
    for index, row in df.iterrows():
        disease = row['Disease']
        if pd.isnull(row['cp']):
            df.at[index, 'cp'] = 3 if "Angina" in disease else 0
        # Add remaining imputation logic here...
    return df

# Apply the imputation function
heart_data_imputed = fill_missing_values(heart_data)

# Save the refined dataset
heart_data_imputed.to_csv(imputed_data_path, index=False)

# Train model
data = pd.read_csv(imputed_data_path)
X = data.drop(columns=['Disease'])
y = LabelEncoder().fit_transform(data['Disease'])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model, scaler, and label encoder
with open(model_path, 'wb') as model_file:
    pickle.dump(model, model_file)

with open(scaler_path, 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

# Save label encoder
with open(label_encoder_path, 'wb') as le_file:
    pickle.dump(LabelEncoder(), le_file)
