import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Data Cleaning
def clean_data(df):
    # Drop rows with missing values
    df = df.dropna()
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Reset index after cleaning
    df.reset_index(drop=True, inplace=True)
    
    return df

# Feature Engineering
def feature_engineering(df):
    # Example: Convert categorical columns to numerical (Label Encoding)
    label_encoder = LabelEncoder()
    df['encoded_column'] = label_encoder.fit_transform(df['categorical_column'])
    
    # Create new features (if applicable)
    df['new_feature'] = df['existing_column1'] * df['existing_column2']  # Example
    
    return df

# Scaling/Normalization
def scale_data(df):
    # Normalize numerical columns using StandardScaler
    scaler = StandardScaler()
    df[['numerical_column1', 'numerical_column2']] = scaler.fit_transform(df[['numerical_column1', 'numerical_column2']])
    
    return df

# Combine all preprocessing steps
def preprocess_data(file_path):
    df = load_data(file_path)
    df = clean_data(df)
    df = feature_engineering(df)
    df = scale_data(df)
    return df

# Example usage
if __name__ == "__main__":
    processed_data = preprocess_data('data/zomato.csv')
    print(processed_data.head())
