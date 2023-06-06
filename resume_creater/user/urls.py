from django.urls import path,include
from user import views

urlpatterns = [
    path('login/',views.login_view,name='login'), 
    path('logout/',views.logout_view,name='logout'), 
    path('social/signup/',views.signup,name='signup'),
    
]