# Python News CLI App
A News App in Python by integrating with news APIs like NewsAPI that will fetch the latest headlines, display articles, and allow users to filter news based on categories or keywords.

---

## Project Overview
This Python-based command-line interface (CLI) app efficiently fetches and displays news headlines and URLs from the News API. It allows users to search for news on a specific topic and filter results by a custom start date, providing a focused and streamlined news gathering experience.

---

## Features
* **Topic-Based Search:**   Find news articles on any subject of your choice.

* **Date Filtering:**   Specify a start date to narrow down your search results.

* **Clean Output:**   Get a focused list of article titles and their corresponding URLs.

* **Robust Error Handling:**   The script gracefully handles network issues or invalid API responses.

---

## Getting Started
Follow these steps to get a local copy of the project up and running.

### Prerequisites
**Python 3.x:**  
Ensure you have Python installed. You can check your version by running python --version in your terminal.

### Requests Library: 
This script uses the requests library to make API calls. You can install it with pip:
```bash
pip install requests
```

### Installation & Setup
* **Clone the repository:**   Get a copy of the project on your local machine using this command:
```bash
git clone https://github.com/LuckyG05/News_App.git
```
```bash
cd News_App
```

* **Get a News API Key:**
Sign up for a free API key at News API.

* **Configure Your API Key:**
Open the news_app.py file and replace the placeholder API key with your own:
```bash
API_KEY = "YOUR-API-KEY-HERE"
```

---

## How to Use
**Simply run the script from your terminal and follow the prompts.** 
```bash
python news_app.py
```  

The app will ask you for a search topic and a start date.

**Example Session:** 
```bash
Enter a topic to search for news: technology
Enter a start date (YYYY-MM-DD format): 2025-07-20

--- Found 5 articles for 'technology' ---

Article 1:
Title: The Future of AI in Modern Computing
URL: https://example.com/ai-future

**************************************************

Article 2:
Title: New Quantum Chip Breakthrough Announced
URL: https://example.com/quantum-chip

**************************************************
...
```
---

## Contributing
Feel free to fork this repository and submit pull requests to improve the script. All contributions are welcome!

---

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contact
If you have any questions or feedback, feel free to reach out:
* **GitHub:** [LuckyG05](https://github.com/LuckyG05)

---
