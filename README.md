# Restaurant Recommendation and Insights Dashboard

An interactive web application that provides personalized restaurant recommendations and insights into restaurant trends, leveraging the Zomato dataset. This project integrates machine learning, natural language processing, and data visualization to deliver a comprehensive dashboard.

## Project Features

1. **Restaurant Recommendations**

   - Personalized suggestions based on user inputs like location, cuisine, and budget.
   - Content-based recommendation system using features like cuisine type, ratings, and location.

2. **Insights and Visualizations**

   - Interactive visualizations showing trends in ratings, costs, popular cuisines, and more.
   - Analysis of restaurant density, cost variations, and cuisine popularity by location.

3. **Sentiment Analysis**

   - Sentiment analysis on customer reviews to determine trends and feedback.
   - Visual representation of sentiments for popular dishes and restaurants.

4. **Streamlit Dashboard**
   - Dynamic, user-friendly interface with pages for insights, recommendations, and sentiment analysis.
   - Sidebar inputs for refining user preferences.

## Folder Structure

```
restaurant_dashboard/
├── data/
│   └── zomato.csv               # Dataset
├── notebooks/
│   ├── eda.ipynb                # Exploratory Data Analysis
│   └── model_dev.ipynb          # Recommendation and Sentiment Model Development
├── app/
│   ├── pages/
│   │   ├── insights.py          # Page for Insights
│   │   ├── recommendations.py   # Page for Recommendations
│   │   └── reviews.py           # Page for Review Sentiment Analysis
│   └── main.py                  # Main Streamlit app script
├── models/
│   ├── recommendation_model.pkl # Trained Recommendation Model
│   └── sentiment_model.pkl      # Trained Sentiment Analysis Model
├── static/
│   ├── css/                     # Optional CSS for styling Streamlit
│   ├── images/                  # Images for branding
├── utils/
│   ├── preprocessing.py         # Functions for data cleaning and preprocessing
│   ├── eda_helpers.py           # Helper functions for visualizations
│   └── recommend.py             # Recommendation engine logic
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation
```

## Key Technologies

- **Backend and Analysis:** Pandas, NumPy, Scikit-learn
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Natural Language Processing:** NLTK, Spacy, VADER
- **Frontend:** Streamlit

## Installation and Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YourUsername/restaurant_dashboard.git
   cd restaurant_dashboard
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run app/main.py
   ```

## Features in Detail

### 1. Recommendations

- Input preferences such as location, cuisine, and budget.
- Display the top 5 recommended restaurants.

### 2. Insights

- Visualize trends such as:
  - Top cuisines in a city.
  - Rating distributions.
  - Cost variations across locations.

### 3. Sentiment Analysis

- Analyze and display customer feedback trends.
- Sentiment analysis for specific dishes or restaurants.

## Deployment

The app can be deployed using platforms like **Streamlit Cloud** or **Render**. Ensure the `Procfile` and environment dependencies are correctly configured.

## Future Enhancements

- **Advanced Recommendations:** Incorporate collaborative filtering for personalized suggestions.
- **Interactive Maps:** Display restaurant locations with advanced filtering options.
- **Real-Time Updates:** Allow users to upload new data dynamically.

## Acknowledgments

This project is inspired by the Zomato dataset and aims to provide valuable insights and recommendations for food enthusiasts and business owners.

---

**Author:** Vaibhav Sharma  
For any queries or contributions, feel free to reach out!
