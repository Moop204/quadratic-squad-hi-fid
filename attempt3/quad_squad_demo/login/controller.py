from user_profile.models import User
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
  
