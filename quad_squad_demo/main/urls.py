from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.index_login, name='login'),
    path('dashboard/', views.index_dashboard, name='dashboard'),
    path('match/', views.index_match, name='match'),
    path('meetup/', views.index_meetup, name='meetup'),
    path('message/', views.index_message, name='message'),
    path('textbook/', views.index_textbook, name='textbook'),
    path('<int:text_id>', views.textbook_detailed, name='textbook'),
    path('<int:user_id>/', views.specific_index, name='specific_profile'),
    path('edit/', views.index_user_profile, name='user_profile'),
    path('dashboard/', views.index_user_profile, name='user_profile'),
    path('find/', views.match_find, name='find'),
]
urlpatterns += [   
    path('user/edit/', views.index_user_profile, name='edit'),
    path('login/sign_up/', views.create_account, name='sign_up'), #How do we add urls
    path('match/', views.index_match, name='return_match'),
    path('../dashboard/', views.index_dashboard, name='return_dashboard'),
    path('../../dashboard/', views.index_dashboard, name='rreturn_dashboard'),
 
]

