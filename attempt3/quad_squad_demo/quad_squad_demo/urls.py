"""quad_squad_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('match/', include('match.urls')),
    path('meetup/', include('meetup.urls')),
    path('message/', include('message.urls')),
    path('textbook/', include('textbook.urls')),
    path('edit/', include('user_profile.urls')),
]

urlpatterns += [
    # Redirects startup to login page
    path('', RedirectView.as_view(url='/login/')),
    path('login/dashboard/', RedirectView.as_view(url='/dashboard/')),

    # return to dashboard 
    path('dashboard/message/dashboard/', RedirectView.as_view(url='/dashboard/')),
    path('dashboard/textbook/dashboard/', RedirectView.as_view(url='/dashboard/')),
    path('dashboard/meetup/dashboard/', RedirectView.as_view(url='/dashboard/')),    
    path('dashboard/match/dashboard/', RedirectView.as_view(url='/dashboard/')),
    path('dashboard/edit/dashboard/', RedirectView.as_view(url='/dashboard/')),
    path('textbook/dashboard/', RedirectView.as_view(url='/dashboard/')),
    path('textbook/dashboard/', RedirectView.as_view(url='/dashboard/')),
    path('login/credentials/dashboard', RedirectView.as_view(url='/dashboard/')),
]
