from django.urls import path,include
from create_resume import views

urlpatterns = [
    path('create/',views.create,name='create'), 
]