from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='textbook'),
    path('<uuid:text_id>', views.textbook_detailed, name='textbook'),
   
]

