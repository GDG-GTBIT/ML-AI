STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_API= #YOUR ALPHA API KEY
NEWS_API = #YOUR NEW API KEY


import requests


from twilio.rest import Client

auth_token = #YOUR AUTH TOKEN
account_sid = #YOUR SID


stock_params ={
    "function":"TIME_SERIES_DAILY",
    "symbol":  STOCK_NAME,
    "apikey": ALPHA_API,

}

response_stock =  requests.get(STOCK_ENDPOINT, stock_params)

data = response_stock.json()["Time Series (Daily)"]

data_list = [ value for(key,value) in data.items() ] #new_item for item in list

yesterdays_closing_price = float(data_list[0]["4. close"])
day_before_yesterdays_closing_price = float(data_list[1]["4. close"])

difference = yesterdays_closing_price - day_before_yesterdays_closing_price

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference =round(abs(difference)*100 / yesterdays_closing_price)


if percentage_difference < 5:
    #print("get news")

    #Getting news:

    news_params = {
        "apikey":NEWS_API,
         "qInTitle": COMPANY_NAME
    }

    response_news = requests.get(NEWS_ENDPOINT,news_params)
    data = response_news.json()["articles"]
    data_slice = data[:3]


    #

    formatted_data = [f"{STOCK_NAME} {up_down} {percentage_difference} \nHeading:{articles['title']}. \nBrief:{articles['description']}" for articles  in data_slice]

    client = Client(account_sid, auth_token)

    for article in formatted_data:
        message = client.messages.create(
            body=article,
            from_=  " ", # twillio demo number
            to= '' #your number
        )
        print(message.status)
        print(message.sid)






