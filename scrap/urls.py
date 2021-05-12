from django.urls import path
from .views import YahooScrap, YahooList, YahooOne

urlpatterns = [
    path('new/<str:name>', YahooScrap().as_view()),
    path('', YahooList().as_view()),
    path('<str:name>', YahooOne().as_view()),
    
]