import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import joblib

# Load your dataset with error handling
try:
    # Adjust the path to match the actual location of your CSV file
    df = pd.read_csv('zomato.csv/zomato.csv')
except FileNotFoundError:
    raise FileNotFoundError("Error: 'zomato.csv' file not found. Please check the file path.")
except pd.errors.ParserError:
    raise ValueError("Error parsing the 'zomato.csv' file. Ensure the file has proper CSV formatting.")
except Exception as e:
    raise Exception(f"An unexpected error occurred while loading the dataset: {e}")

# Sample recommendation function
def get_recommendations(user_input):
    """
    Given user input (keywords, preferences), recommend restaurants.
    This is a simplified version; you can improve the model.
    """
    try:
        # Example: Filter based on user input or preferences (e.g., restaurant type, rating, location)
        filtered_df = df[df['restaurant_name'].str.contains(user_input, case=False, na=False)]
        
        if filtered_df.empty:
            return "No recommendations found based on your input."
        
        # Example: Filter and return top 5 recommendations based on the rating
        recommendations = filtered_df[['restaurant_name', 'location', 'rating']] \
            .sort_values(by='rating', ascending=False) \
            .head(5)
        
        return recommendations

    except KeyError:
        raise KeyError("Error: Ensure 'restaurant_name', 'location', and 'rating' columns exist in the dataset.")
    except Exception as e:
        raise Exception(f"An error occurred during recommendations: {e}")

# Function to load a pre-trained recommendation model (if available)
def load_model():
    """
    Load a pre-trained recommendation model, if one exists.
    """
    try:
        model = joblib.load('models/recommendation_model.pkl')  # Adjust the path if necessary
        return model
    except FileNotFoundError:
        print("No pre-trained model found. Using default recommendations logic.")
        return None
    except Exception as e:
        raise Exception(f"An unexpected error occurred while loading the model: {e}")
