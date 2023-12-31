from django.urls import path
from . import views

urlpatterns = [
    path('main_screen/', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('about/',views.about,name ="about"),
    path('',views.main_screen,name ="main_screen"),
]