from django.urls import path
from .views import YahooScrap, YahooList, YahooOne, YahooUpdate

urlpatterns = [
    path('new/<str:name>', YahooScrap().as_view()),
    path('', YahooList().as_view()),
    path('one/<str:name>', YahooOne().as_view()),
    path('update/', YahooUpdate().as_view()),
    
]