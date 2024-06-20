import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "your_stock_api_key_here" 
NEWS_API_KEY = "your_news_api_key_here" 
TWILIO_SID = "your_twilio_sid_here" 
TWILIO_AUTH_TOKEN = "your_twilio_auth_token_here" 
PHONE_NUMBER = "+your_phone_number_here" 

## STOCK: https://alphavantage.co/
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
# Get yesterday's closing stock price
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()
print(stock_data)
stock_data_list = [value for (key, value) in stock_data.items()]
ytd_closing_stock_price = stock_data_list[0]["4. close"]
print(ytd_closing_stock_price)

# Get the day before yesterday's closing stock price
day_bef_closing_stock_price = stock_data_list[1]["4. close"]
print(day_bef_closing_stock_price)

# Find the positive difference between yesterday's closing stock price and the day before yesterday's closing stock price
pos_difference = abs((float(ytd_closing_stock_price) - float(day_bef_closing_stock_price)))
up_down = None
if pos_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Find the percentage difference in price between closing price yesterday and closing price the day before yesterday
diff_percentage = round((pos_difference / float(ytd_closing_stock_price)) * 100)


## NEWS: https://newsapi.org/ 
news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}
# If percentage difference is greater than 5, then use the News API to get articles related to the COMPANY_NAME
if abs(diff_percentage) > 5: 
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # Create a list that contains the first 3 articles
    chosen_articles = articles[:3]
    print(chosen_articles)


## SMS: https://twilio.com/
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in chosen_articles]

# Send each article as a separate message via Twilio. 
for article in formatted_articles:
    message = client.messages.create(
        body= article,
        from_=PHONE_NUMBER,
        to=PHONE_NUMBER
    )