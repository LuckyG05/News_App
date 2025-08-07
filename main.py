# Import the 'requests' library to get data from the web.
import requests
import json 
from datetime import datetime

API_KEY = "f33a0790c7b749ce92981124f44769f2"

# To get news articles from the API.
def get_news(query, from_date=None):
    base_url = "https://newsapi.org/v2/everything"
    
    # Instructions we send to the API.
    params = {
        "q": query,
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }

    # Add the date to the parameters if the user provided it
    if from_date:
        params["from"] = from_date
    
    try:
        # Send a request to the API with our instructions.
        response = requests.get(base_url, params=params)
        
        # Check for any HTTP errors (like a bad API key or wrong address).
        response.raise_for_status()
        
        # Convert the JSON response to a Python dictionary
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        # Handle network or request errors
        print(f"Error fetching news: {e}")
        return None
    except json.JSONDecodeError:
        # Handle cases where the response is not valid JSON
        print("Error: Could not decode JSON response from the API.")
        return None

# Get the search topic from the user
user_query = input("Enter a topic to search for news: ")

# Get a start date from the user and validate the format
while True:
    user_date_str = input("Enter a start date (YYYY-MM-DD format): ")
    try:
        datetime.strptime(user_date_str, "%Y-%m-%d")
        break   # Exit the loop if the format is correct
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Get the news data based on the user's input
news_data = get_news(user_query, from_date=user_date_str)

# Check if we got articles
if news_data and news_data["articles"]:
    articles = news_data["articles"]
    print(f"\n--- Found {len(articles)} articles for '{user_query}' ---\n")
    
    for index, article in enumerate(articles):
        print(f"Article {index + 1}:")
        print(f"Title: {article.get('title', 'N/A')}")
        print(f"URL: {article.get('url', 'N/A')}")
        print("\n" + "*" * 50 + "\n")
else:
    # If no articles were found
    print("Could not retrieve news articles. Please check your query or API key.")



