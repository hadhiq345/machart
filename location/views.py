from inspect import Parameter
from django.shortcuts import render
from django.http import JsonResponse
import requests

from .models import Location
# Create your views here.
def home(request):
    return render(request, 'home.html')


def fetch_location(request):
    api = 'http://machart.in/api/list.php'
    latitude = request.GET['latitude']
    longitude = request.GET['longitude']

    if Location.objects.filter(latitude=latitude,longitude=longitude).exists():
        print('places from db')
        response = Location.objects.get(latitude=latitude,longitude=longitude).places
        return JsonResponse(response, safe= False) 
    
    parameters = {
        'lat': latitude,
        'lon': longitude
    }  
    response = requests.get(f"{api}", params=parameters)
    data = response.json()
    Location.objects.create(
        latitude=latitude,
        longitude=longitude,
        places=data
    )
    print('places from api')
    return JsonResponse(data, safe= False)   


