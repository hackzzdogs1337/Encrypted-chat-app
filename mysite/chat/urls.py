# chat/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('chat/room/',views.index,name='enterroom'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('login/',LoginView.as_view(template_name='chat/login.html'),name='login'),
    path('register',views.register,name='register'),
    path('logout/',LogoutView.as_view(template_name='chat/logout.html'),name='logout'),
    
]