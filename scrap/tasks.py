from celery import shared_task
from .models import ScrapModel

import yfinance as yf
import pandas as pd
from datetime import datetime


TICKER=['PD','ZUO','PINS','ZM', 'CLDR','RUN']


@shared_task()
def update():
    global TICKER
    posts=ScrapModel.objects.latest('id')
    current_date=str(posts.date)
    last_date=str(datetime.today())[:10]
    dif=abs((int(current_date[8:])-1)-int(last_date[8:]))
    dif=str(dif)+'d'
    tickerStrings = TICKER
    df_list = list()
    if dif!=0:
        for ticker in tickerStrings:
            try:
                data = yf.download(ticker, group_by="Ticker", period=dif)
                data['ticker'] = ticker  
                df_list.append(data)
            except Exception:
                continue
    
    hist = pd.concat(df_list)
    for x in range(len(hist)):
        a=hist.iloc[x]
        if ScrapModel.objects.filter(date=a.name, volume_field=a.loc['Volume'], name=a.loc['ticker']).exists():
            continue
        else:
            b=ScrapModel(date=a.name, open_filed=a.loc['Open'],
                        hight_field=a.loc['High'],
                        low_field=a.loc['Low'],
                        close_field=a.loc['Close'],
                        adj_close_field=a.loc['Close'],
                        volume_field=a.loc['Volume'],
                        name=a.loc['ticker'])
        b.save()

@shared_task()
def get(name):
    tickerStrings = [name.upper()]
    global TICKER
    TICKER.append(name.upper())
    df_list = list()
    post=ScrapModel.objects.latest('id')
    date=post.date
    for ticker in tickerStrings:
        try:
            data = yf.download(ticker, group_by="Ticker", period='7d')
            data['ticker'] = ticker  
            df_list.append(data)
        except Exception:
            continue
        
    hist = pd.concat(df_list)
    for x in range(len(hist)):
        a=hist.iloc[x]
        b=ScrapModel(date=a.name, open_filed=a.loc['Open'],
                            hight_field=a.loc['High'],
                            low_field=a.loc['Low'],
                            close_field=a.loc['Close'],
                            adj_close_field=a.loc['Close'],
                            volume_field=a.loc['Volume'],
                            name=a.loc['ticker'])
        b.save()
        