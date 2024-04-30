from django.urls import path
from .import views

urlpatterns = [
    path("", views.CountryHome, name="CountryHome"),
    path("CountryHome", views.CountryHome, name="CountryHome"),
    path('addCountry', views.addCountry,name='addCountry'),
    path('displayCountry', views.displayCountry,name='displayCountry'),
    path('addloc', views.addloc,name='addloc'),
    path('addLocation', views.addLocation, name='addLocation'),
    path('add_location', views.add_location, name='add_location'),
    path('display_locations', views.display_locations, name='display_locations'),
    path('addressJoin', views.addressJoin, name='addressJoin'),
    path('addressNotJoin', views.addressNotJoin, name='addressNotJoin'),
]