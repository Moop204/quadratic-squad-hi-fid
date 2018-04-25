from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dashboard'),
]
urlpatterns += [   
    path('match/', views.main_match, name='main_match'),
    path('meetup/', views.main_meetup, name='main_meetup'),
    path('message/', views.main_message, name='main_message'),
    path('textbook/', views.main_textbook, name='main_textbook'),
    path('edit/', views.main_profile, name='main_textbook'),
]

