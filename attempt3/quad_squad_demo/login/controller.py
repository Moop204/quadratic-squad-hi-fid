from user_profile.models import User, Degree
import logging

class loginQueries():
    def loginValidation(username, password):
        result = User.objects.filter(username=username).filter(password=password).first()
        print(result)
        if result == None:
            return False
        else:
            return True

    def loginID(username, password):
        return User.objects.filter(username=username).filter(password=password).first()

class userQueries():
    def addUser(dob, university_id, degree_id, email, desc, password, username, name):
        degree_id = int(degree_id)
        degree = Degree.objects.filter(id=degree_id).first()
        newUser = User(username=username, password=password, dob=dob, name=name, degree=degree)
        return newUser.save()  
