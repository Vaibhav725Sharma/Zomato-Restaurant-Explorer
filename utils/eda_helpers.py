import matplotlib.pyplot as plt
import seaborn as sns

def plot_ratings_distribution(data):
    """
    Plot the distribution of ratings.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data['rate'], bins=20, kde=True, color='blue')
    plt.title('Ratings Distribution')
    plt.xlabel('Ratings')
    plt.ylabel('Frequency')
    plt.show()

def plot_top_cuisines(data, n=10):
    """
    Plot the top cuisines by count.
    """
    top_cuisines = data['cuisines'].value_counts().head(n)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette='viridis')
    plt.title(f'Top {n} Cuisines by Count')
    plt.xlabel('Count')
    plt.ylabel('Cuisines')
    plt.show()

def plot_cost_distribution(data):
    """
    Plot the distribution of approximate costs for two people.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data['approx_cost(for two people)'], bins=20, kde=True, color='green')
    plt.title('Cost Distribution')
    plt.xlabel('Cost (for two people)')
    plt.ylabel('Frequency')
    plt.show()
