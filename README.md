# Stock News Alert System

This Python script fetches stock data and relevant news articles for a specified company, and sends SMS alerts about significant changes in the stock price along with the news articles. It utilizes APIs from Alpha Vantage for stock data and News API for news articles. SMS alerts are sent using the Twilio API.

![Screenshot 2024-06-20 211714](https://github.com/xinconggg/Stock-Trading-News-Alert/assets/82378681/56a8f159-2d4f-4bf6-a0ff-1851414dbfc2)

## Features

- Retrieves daily stock data for a specified company from Alpha Vantage API.
- Fetches news articles related to the specified company using News API.
- Sends SMS alerts containing stock price changes and relevant news articles via Twilio API.
- Alerts triggered when the percentage difference between yesterday's and the day before yesterday's closing stock price exceeds 5%.

## Requirements

- Python 3.x
- `requests` library
- `twilio` library
- Alpha Vantage API key
- News API key
- Twilio Account SID and Auth Token
- Twilio phone number

## Setup

1. Obtain API keys for Alpha Vantage, News API, and Twilio.
2. Replace the placeholders with your API keys and phone number in the code.
3. Install necessary packages (`requests`, `twilio`) using pip.

## Usage

1. Run the script periodically (e.g., via cron job) to stay updated with stock changes and news.
2. Receive SMS alerts when there's a significant change in the stock price along with relevant news articles.
3. Stay informed about stock movements and associated news impacting the specified company.

## Components

### 1. Stock Data Retrieval

- **API Used:** Alpha Vantage
- **Functionality:** Retrieves daily stock data for a specified company.
- **Data Obtained:** Closing stock prices for yesterday and the day before yesterday.

### 2. News Article Retrieval

- **API Used:** News API
- **Functionality:** Fetches news articles related to the specified company.
- **Trigger:** Activates when the percentage difference between yesterday's and the day before yesterday's closing stock price exceeds 5%.

### 3. SMS Alert System

- **Service Used:** Twilio
- **Functionality:** Sends SMS alerts containing stock price changes and relevant news articles.
- **Format:** Each SMS includes the stock symbol, percentage change, headline, and a brief description of the news article.

## Code Explanation
### Stock Data Retrieval
The script makes a request to the Alpha Vantage API to retrieve daily stock data for the specified company. It then extracts the closing stock prices for yesterday and the day before yesterday.
### News Article Retrieval
When the percentage difference in stock prices exceeds 5%, the script makes a request to the News API to fetch news articles related to the specified company. It selects the first three articles for further processing.
### SMS Alert System
The script uses the Twilio API to send SMS alerts containing information about stock price changes and relevant news articles. It formats the message to include the stock symbol, percentage change, headline, and brief description of each article. SMS messages are sent for each article retrieved.



