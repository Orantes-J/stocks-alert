import json
import requests
import os
from newsapi import NewsApiClient
from twilio.rest import Client

# LOWS AND HIGHS OF A STOCK
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey=CX8DGPAPEET395PW'
request_for_data = requests.get(url).json()

with open('stock_info.json', 'w') as info:
    json.dump(request_for_data, info, indent=1)


with open('stock_info.json', 'r') as info:
    stock_info = json.load(info)
    days_info = stock_info['Time Series']
    for i in days_info:
        start_day = 31
        print(days_info[i[f'2021-08-{start_day}']])
        start_day -= 1

# NEWS

newsapi = NewsApiClient(api_key="demo")


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

account_sid = 'demo'
print(account_sid)
auth_token = 'demo'
client = Client(account_sid, auth_token)

message = client.messages.create(body="Hello Juan", from_='demo', to='demo')

print(message.sid)



