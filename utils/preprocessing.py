import pandas as pd
import numpy as np
import re
import string
from sklearn.preprocessing import MinMaxScaler
from nltk.corpus import stopwords

# Function to preprocess the data
def preprocess_data(file_path):
    """
    Preprocesses the restaurant data.
    
    Args:
        file_path (str): Path to the dataset CSV file.
    
    Returns:
        pd.DataFrame: Cleaned and preprocessed dataset.
    """
    # Load dataset
    zomato = pd.read_csv(file_path)

    # Dropping unnecessary columns
    zomato = zomato.drop(['url', 'dish_liked', 'phone'], axis=1)

    # Removing duplicates
    zomato.drop_duplicates(inplace=True)

    # Dropping rows with missing values
    zomato.dropna(how='any', inplace=True)

    # Renaming columns for consistency
    zomato = zomato.rename(columns={
        'approx_cost(for two people)': 'cost',
        'listed_in(type)': 'type',
        'listed_in(city)': 'city'
    })

    # Transforming 'cost' column to numeric
    zomato['cost'] = zomato['cost'].astype(str).apply(lambda x: x.replace(',', '')).astype(float)

    # Cleaning 'rate' column
    zomato = zomato[zomato.rate != 'NEW']
    zomato = zomato[zomato.rate != '-']
    zomato['rate'] = zomato['rate'].str.replace('/5', '').astype(float)

    # Normalizing mean ratings
    restaurants = zomato['name'].unique()
    zomato['Mean Rating'] = 0
    for restaurant in restaurants:
        zomato.loc[zomato['name'] == restaurant, 'Mean Rating'] = zomato.loc[zomato['name'] == restaurant, 'rate'].mean()

    # Scaling 'Mean Rating'
    scaler = MinMaxScaler(feature_range=(1, 5))
    zomato[['Mean Rating']] = scaler.fit_transform(zomato[['Mean Rating']])

    # Lowercasing and cleaning 'reviews_list'
    zomato['reviews_list'] = zomato['reviews_list'].str.lower()
    zomato['reviews_list'] = zomato['reviews_list'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
    stop_words = set(stopwords.words('english'))
    zomato['reviews_list'] = zomato['reviews_list'].apply(lambda x: ' '.join(word for word in x.split() if word not in stop_words))
    zomato['reviews_list'] = zomato['reviews_list'].apply(lambda x: re.sub(r'https?://\S+|www\.\S+', '', x))

    return zomato
