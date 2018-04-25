from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='login'),
]

urlpatterns += [   
    path('login/', views.submit_credentials, name='submit_credentials'),
    path('credentials/', views.create_account, name='create_account'),

]
