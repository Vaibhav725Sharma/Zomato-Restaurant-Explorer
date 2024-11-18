# Zomato-Restaurant-Explorer

Overview
Zomato Restaurant Explorer is an interactive data visualization app built using Streamlit that helps users explore restaurant data. It leverages data from the Zomato dataset to analyze restaurant ratings, cuisines, locations, and more. The project is designed to provide valuable insights into restaurant trends and recommend eateries based on user preferences.

Key Features
Restaurant Filter: Filter restaurants by city, cuisine, online orders, or table booking availability.
Visualization Dashboard: View visual representations of restaurant ratings, average cost, and the number of votes across different cities and cuisines.
Recommendation System: Get personalized restaurant recommendations based on location and rating filters.
Top Restaurants: Identify top-rated restaurants in various categories like "Best for Delivery," "Best for Dining," etc.
Data Analysis: Analyze trends in restaurant pricing, popular cuisines, and customer reviews.
Technologies Used
Streamlit: For building the interactive web app.
Pandas: For data manipulation and processing.
Matplotlib / Seaborn: For visualizations.
Scikit-learn: For machine learning models (optional, for recommendations or clustering).
Dataset
The project uses the Zomato Restaurant dataset, which contains the following key columns:

url, address, name, online_order, book_table, rate, votes, location, rest_type, dish_liked, cuisines, approx_cost(for two people), reviews_list, menu_item, listed_in(type), listed_in(city).
Installation
To run the Zomato Restaurant Explorer app on your local machine, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Zomato-Restaurant-Explorer.git
cd Zomato-Restaurant-Explorer
Create a virtual environment (optional, but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
streamlit run app/main.py
Open the app in your browser at localhost:8501.

How to Use
Upon loading the app, users can choose filters based on city, cuisine, and online order availability.
Visualizations will update dynamically based on selected filters, providing insights such as average restaurant ratings, cost for two people, and the number of votes for each restaurant.
Users can also get personalized restaurant recommendations based on their preferred criteria.
Project Structure
bash
Copy code
Zomato-Restaurant-Explorer/
├── app/
│ └── main.py # Streamlit app for data visualization and recommendations
├── data/
│ └── zomato.csv # Zomato dataset (51717 rows, 17 columns)
├── notebooks/
│ └── data_cleaning.py # Script for cleaning and preprocessing the data
├── requirements.txt # Python dependencies
└── README.md # Project documentation
Future Improvements
Advanced Recommendation System: Implement a collaborative filtering or content-based recommendation model.
User Authentication: Allow users to save their preferences and previous searches.
Geospatial Analysis: Incorporate maps to visualize restaurant locations.
Contributing
Feel free to fork the repository and contribute to the project! If you find bugs or have ideas for improvements, open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
