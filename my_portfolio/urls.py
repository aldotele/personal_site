from django.urls import path
from my_portfolio.views import index


urlpatterns = [
    path('', index, name='index'),
]