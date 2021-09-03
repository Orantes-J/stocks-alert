import json
import requests
import os
from newsapi import NewsApiClient
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# LOWS AND HIGHS OF A STOCK
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey=CX8DGPAPEET395PW'
request_for_data = requests.get(url).json()

# with open('stock_info.json', 'w') as info:
#     json.dump(request_for_data, info, indent=1)


with open('stock_info.json', 'r') as info:
    stock_info = json.load(info)
    days_info = stock_info['Time Series']
    for i in days_info:
        start_day = 31
        print(days_info[i[f'2021-08-{start_day}']])
        start_day -= 1

# NEWS

newsapi = NewsApiClient(api_key="2120e0fe626148868fe7126eae4a3da3")


top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                          category='business',
                                          language='en',
                                          country='us')

all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                      sources='bbc-news,the-verge',
                                      from_param='2021-08-00',
                                      to='2021-08-25',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

sources = newsapi.get_sources()

with open("news.json", 'w') as info:
    json.dump(sources, info, indent=1)


with open('news.json', 'r') as info:
    news_info = json.load(info)
    print(news_info)

# SMS A PHONE NUMBER

# account_sid = 'AC3e931cf5141b7ab634d400aacf52c159'
# print(account_sid)
# auth_token = '08237ba3793ab9c7f4dc15835476c082'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(body="Hello Juan", from_='16105959056', to='2138422717')
#
# print(message.sid)



