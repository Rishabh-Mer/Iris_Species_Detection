from django.urls import path
from .views import result, home

urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result')
]
