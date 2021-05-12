from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ScrapModel
from .serializers import ScrapSerializer

import yfinance as yf
import pandas as pd

from datetime import datetime


TICKER=['PD','ZUO','PINS','ZM', 'CLDR','RUN']


class YahooUpdate(APIView):
    def get(self, request, format=None):
        global TICKER
        posts=ScrapModel.objects.latest('id')
        current_date=str(posts.date)
        last_date=str(datetime.today())[:10]
        dif=abs((int(current_date[8:]))-int(last_date[8:]))
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
        context={'result':'succes'}
        return Response(context)
        




class YahooScrap(APIView):
    def get(self, request, name, format=None):
        tickerStrings = TICKER
        df_list = list()
        for ticker in tickerStrings:
                try:
                    data = yf.download(ticker, group_by="Ticker", period='max')
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
        context={'hist':'succes'}
        return Response(context)


class YahooList(APIView):
    def get(self, request, format=None):
        posts=ScrapModel.objects.all().order_by('-id')
        serializer=ScrapSerializer(posts, many=True)
        return Response(serializer.data)



class YahooOne(APIView):
    def get(self, request, name , format=None):
        posts=ScrapModel.objects.filter(name=name.upper()).order_by('-id')
        if not posts.exists():
            return Response(status=400)
        else:
            serializer=ScrapSerializer(posts, many=True)
            return Response(serializer.data)
    


