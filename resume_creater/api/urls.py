from django.urls import path,include
from api import views

urlpatterns = [
    path('api/',views.api,name='api'), 
]