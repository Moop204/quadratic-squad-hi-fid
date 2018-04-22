from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('/', views.index, name='index')
]
