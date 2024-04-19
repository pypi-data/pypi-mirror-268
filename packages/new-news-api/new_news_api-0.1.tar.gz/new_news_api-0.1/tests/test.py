from new_news_api.my_news import NewsAPI

# Replace 'your_api_key' with your actual News API key
news_api = NewsAPI(api_key='b52eb77ce6764314a4d14eeee7f0255b')

# Example usage
top_headlines = news_api.get_top_headlines()
print(top_headlines)

search_results = news_api.search_news(query='python')
print(search_results)
