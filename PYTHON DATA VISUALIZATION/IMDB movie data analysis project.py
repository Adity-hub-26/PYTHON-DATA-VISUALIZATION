# Step 1: Import required libraries
import pandas as pd  # For handling data
import matplotlib.pyplot as plt  # For plotting
import seaborn as sns  # For better styled plots
import os  # To create directories

# Step 2: Ensure the 'plots' directory exists
# This is where we will save the generated plots
if not os.path.exists('plots'):
    os.makedirs('plots')

# Step 3: Load the dataset into a pandas DataFrame
# Reading the movie data from the CSV file
movies = pd.read_csv('C:/Users/Admin/PYTHON/IMDB-Movie-Data.csv')

# Step 4: Clean the data
# Convert the 'Revenue (Millions)' column to numeric, because it may have missing or non-numeric values
movies['Revenue (Millions)'] = pd.to_numeric(movies['Revenue (Millions)'], errors='coerce')

# Convert 'Runtime (Minutes)' to numeric in case of any errors
movies['Runtime (Minutes)'] = pd.to_numeric(movies['Runtime (Minutes)'], errors='coerce')

# Step 5: Plot - Distribution of Movie Ratings
# We will create a histogram to visualize how the movie ratings are distributed
plt.figure(figsize=(10, 6))  # Create a figure for the plot
sns.histplot(movies['Rating'], bins=10, kde=True, color='blue')  # Plot the histogram with a kernel density estimate
plt.title('Distribution of Movie Ratings')  # Add a title
plt.xlabel('Rating')  # Label for the x-axis
plt.ylabel('Number of Movies')  # Label for the y-axis
plt.savefig('plots/distribution_of_ratings.png')  # Save the plot as an image

plt.show()  # Show the plot

# Step 6: Plot - Top 10 Movies by Revenue
# Sort the movies by revenue and pick the top 10
top_revenue_movies = movies.nlargest(10, 'Revenue (Millions)')

# Create a bar plot to visualize these top 10 movies
plt.figure(figsize=(12, 6))  # Create a new figure
sns.barplot(x='Revenue (Millions)', y='Title', data=top_revenue_movies, palette='viridis')  # Bar plot
plt.title('Top 10 Movies by Revenue')  # Add a title
plt.xlabel('Revenue (Millions)')  # Label for the x-axis
plt.ylabel('Movie Title')  # Label for the y-axis
plt.savefig('plots/top_10_movies_by_revenue.png')  # Save the plot as an image

plt.show()  # Show the plot

# Step 7: Plot - Correlation between Rating and Revenue
# We will create a scatter plot to show the relationship between movie rating and revenue
plt.figure(figsize=(8, 6))  # Create a new figure
sns.scatterplot(x='Rating', y='Revenue (Millions)', data=movies)  # Scatter plot
plt.title('Rating vs Revenue')  # Add a title
plt.xlabel('Rating')  # Label for the x-axis
plt.ylabel('Revenue (Millions)')  # Label for the y-axis
plt.savefig('plots/rating_vs_revenue.png')  # Save the plot as an image

plt.show()  # Show the plot

# Step 8: Plot - Count of Movies by Genre
# First, we need to split the genre column, as a movie can belong to multiple genres
movies['Genres'] = movies['Genre'].str.split(',')

# Now, we 'explode' the genres so each genre has its own row
movies_exploded = movies.explode('Genres')

# Create a count plot to show how many movies belong to each genre
plt.figure(figsize=(12, 6))  # Create a new figure
sns.countplot(y='Genres', data=movies_exploded, order=movies_exploded['Genres'].value_counts().index, palette='coolwarm')  # Count plot
plt.title('Count of Movies by Genre')  # Add a title
plt.xlabel('Count')  # Label for the x-axis
plt.ylabel('Genre')  # Label for the y-axis
plt.savefig('plots/count_of_movies_by_genre.png')  # Save the plot as an image

plt.show()  # Show the plot

# Step 9: Plot - Average Runtime of Movies by Year
# We will create a line plot to show how movie runtimes have changed over the years
plt.figure(figsize=(10, 6))  # Create a new figure
sns.lineplot(x='Year', y='Runtime (Minutes)', data=movies, marker='o', ci=None)  # Line plot with markers
plt.title('Average Runtime of Movies by Year')  # Add a title
plt.xlabel('Year')  # Label for the x-axis
plt.ylabel('Runtime (Minutes)')  # Label for the y-axis
plt.savefig('plots/average_runtime_by_year.png')  # Save the plot as an image

plt.show()  # Show the plot
