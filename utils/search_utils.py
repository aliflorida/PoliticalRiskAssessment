import requests
import os

def get_country_news(country):
    try:
        serp_api_key = os.getenv("SERPAPI_API_KEY")
        url = f"https://serpapi.com/search.json?q=political+news+{country}&api_key={serp_api_key}&engine=google_news"
        res = requests.get(url)
        articles = res.json().get("news_results", [])[:3]
        return [f"{a['title']} - {a['link']}" for a in articles] if articles else None
    except Exception as e:
        return f"Error retrieving news: {e}"