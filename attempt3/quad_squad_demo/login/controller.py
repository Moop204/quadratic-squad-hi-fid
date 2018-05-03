from user_profile.models import ExtUser, Degree
import logging

class loginQueries():
    # returns whether the credentials given have any corresponding records
    def loginValidation(username, password):
        result = User.objects.filter(username=username).filter(password=password).first()
        print(result)
        if result == None:
            return False
        else:
            return True

class userQueries():
    def addUser(dob, degree_id, email, desc, password, username, first_name, last_name):
        degree_id = int(degree_id)
        degree = Degree.objects.filter(id=degree_id).first()
        newUser = ExtUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name, 
            degree=degree,
            description=desc,
            dob=dob,
        )
        newUser.user_permissions.add(1)
        return newUser.save()  
