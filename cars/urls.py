from django.urls import path

from cars.views import  car_check

urlpatterns = [
    path("", car_check, name='car_check')
]