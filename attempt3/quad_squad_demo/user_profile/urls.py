from django.urls import path
from . import views


urlpatterns = [
    path('<int:user_id>/', views.specific_index, name='specific_profile'),
    path('edit/', views.index, name='user_profile'),
]

urlpatterns += [   
]
