from django.urls import path
from location.views import home, fetch_location

urlpatterns = [
    path('', home ),
    path('fetch-location', fetch_location)
]