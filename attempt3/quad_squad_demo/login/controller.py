

class loginQueries():
    def loginValidation(username, password):
        result = Entry.objects.filter(username=username).filter(password=password)
        if result.length > 1 or result.length == 0:
            return False
        else:
            return True

    def loginID(username, password):
        return Entry.objects.filter(username=username).filter(password=password)
  
