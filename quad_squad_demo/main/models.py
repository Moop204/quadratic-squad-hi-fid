from django.db import models
from django.contrib.auth.models import AbstractUser
 
# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=20)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ExtUser(AbstractUser):
    dob = models.DateField(help_text='Format yyyy-mm-dd') 
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Enrolment(models.Model):
    user = models.ForeignKey(ExtUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        name = (Course.objects.filter(id=self.course.id).first()).name
        return str(self.user) + " enrolled in " + str(name)

class Matches(models.Model):
    sender = models.ForeignKey(ExtUser, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(ExtUser, related_name='receiver', on_delete=models.CASCADE)
    MATCH_STATUS=(
        ('p','Pending'),
        ('a','Accepted'),
    )
    status = models.CharField(max_length=1, choices=MATCH_STATUS, help_text='Matches')

class comment():
    '''
class Textbook(models.Model):
    title = models.CharField(max_length=20) 
    author= models.CharField(max_length=20) 
    pubDate = models.DateField() 

    def __str__(self):
        return self.title

class Recommend_Textbook(models.Model):
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)

class Message(models.Model):
    user1 = models.ForeignKey(ExtUser, related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(ExtUser, related_name='user2', on_delete=models.CASCADE)
    textFile = models.FilePathField()

    def __str__(self):
        return self.textFile
                   
class Pending_Meetup(models.Model):
    host = models.ForeignKey(ExtUser, related_name='host', on_delete=models.CASCADE)
    guest = models.ForeignKey(ExtUser, related_name='guest',  on_delete=models.CASCADE)
    status = models.IntegerField()
    location = models.CharField(max_length=20)
    time = models.DateTimeField('')  
    date = models.DateTimeField('') 
    description = models.CharField(max_length=300)
'''
