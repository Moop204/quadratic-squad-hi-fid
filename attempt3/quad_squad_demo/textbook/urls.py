from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='textbook'),
    path('', views.textbook_detailed, name='textbook'),
   
]

