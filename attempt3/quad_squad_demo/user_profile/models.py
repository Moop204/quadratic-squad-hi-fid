from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=20) 
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Degree(models.Model):
    name = models.CharField(max_length=20) 
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=20) 
    password = models.CharField(max_length=20)
    dob = models.DateTimeField('date of birth') 
    name = models.CharField(max_length=40) 
    #preferred = models.CharField(max_length=20)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    #course_list = models.ForeignKey(Courses)
    #calendar = ???
    description = models.CharField(max_length=300)   

    def __str__(self):
        return self.name

class Textbook(models.Model):
    title = models.CharField(max_length=20) 
    author= models.CharField(max_length=20) 
    pubDate = models.DateTimeField() 

    def __str__(self):
        return self.title

class Recommend_Textbook(models.Model):
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    #type = models.IntegerField()

class Message(models.Model):
    user1 = models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE)
    textFile = models.FilePathField()

    def __str__(self):
        return self.textFile
                   
class Matches(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    MATCH_STATUS=(
        ('p','Pending'),
        ('a','Accepted'),
    )
    status = models.CharField(max_length=1, choices=MATCH_STATUS, blank=False, help_text='Matches')

class Pending_Meetup(models.Model):
    host = models.ForeignKey(User, related_name='host', on_delete=models.CASCADE)
    guest = models.ForeignKey(User, related_name='guest',  on_delete=models.CASCADE)
    status = models.IntegerField()
    location = models.CharField(max_length=20)
    time = models.DateTimeField('') #  CHECK 
    date = models.DateTimeField('') 
    description = models.CharField(max_length=300) 


