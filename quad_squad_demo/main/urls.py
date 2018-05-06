from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_login, name='login'),
    path('login/', views.index_login, name='login'),
    path('dashboard/', views.index_dashboard, name='dashboard'),
    path('match/', views.index_match, name='match'),
    path('meetup/', views.index_meetup, name='meetup'),
    path('message/', views.index_message, name='message'),
    path('textbook/', views.index_textbook, name='textbook'),
    path('<int:text_id>', views.textbook_detailed, name='textbook'),
    path('<int:user_id>/', views.specific_index, name='specific_profile'),
    path('edit/', views.index_user_profile, name='user_profile'),
]
urlpatterns += [   
    path('user/edit/', views.main_profile, name='edit'),
    path('sign_up/', views.create_account, name='sign_up'),
]

