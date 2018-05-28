from .models import *
import datetime
from django.contrib.auth import authenticate, login

class MeetupQueries():
        # given a user id, returns a list of other users who have sent a request to the current user
    def getRequestList(user):
        meetups = Pending_Meetup.objects.filter(guest=user).filter(status='p').filter(date__gte=datetime.datetime.now()).all()
        return meetups

    def getSentList(user):
        sends = Pending_Meetup.objects.filter(host=user).filter(status='p').filter(date__gte=datetime.datetime.now()).all()
        return sends

    def getMeetupList(user):
        meetups = []
        for meetup in Pending_Meetup.objects.filter(host=user).filter(status='a').filter(date__gte=datetime.datetime.now()).all():
            meetups.append(meetup)
        for meetup in Pending_Meetup.objects.filter(guest=user).filter(status='a').filter(date__gte=datetime.datetime.now()).all():
            meetups.append(meetup)
        return meetups
        
