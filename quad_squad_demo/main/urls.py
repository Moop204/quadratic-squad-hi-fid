from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),
    path('login/', views.index_login, name='login'),
    path('login/sign_up/', views.create_account, name='sign_up'),
    path('logout/', views.index_logout, name='logout'),
    path('dashboard/', views.index_dashboard, name='dashboard'),
    path('edit/', views.edit_profile, name='edit_profile'),   
    path('user/<int:user_id>', views.specific_user, name='specific_profile'), 
    path('match/', views.index_match, name='match'), 
    path('meetup/', views.index_meetup, name='meetup'),
    path('meetup/create/', views.create_meetup, name='make_meetup'),
    path('message/', views.index_message, name='message'),
    path('textbook/', views.index_textbook, name='textbook'),
]

