from django.urls import path,include
from core import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user/',include('user.urls')),
    path('resume/',include('create_resume.urls')),
    path('php/',include('api.urls')),
]