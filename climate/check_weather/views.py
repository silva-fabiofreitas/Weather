from django.http import JsonResponse
from django.shortcuts import render

from .producer import publish

def index(request):
    # publish(body='Ola mundo')
    return render(request, '/home/fabio/curso/rabbitmq/Weather/climate/check_weather/templates/index.html')
