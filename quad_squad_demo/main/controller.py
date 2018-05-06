from .models import ExtUser, Degree

# queries involving user
class userQueries():
    # search for user given their id
    def findUser(u_id):
        user = ExtUser.objects.filter(id=u_id).first()
        return user 

    # search for a degree's name given a user id  
    def findUserDegree(u_id):
        user = ExtUser.objects.filter(id=u_id).first()
        degree = Degree.objects.filter(id=user.degree_id).first()
        return degree.name

    # add a record to the user table 
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

# queries involved in the logging in process
class loginQueries():
    # returns whether the credentials given have any corresponding records
    def loginValidation(username, password):
        result = User.objects.filter(username=username).filter(password=password).first()
        print(result)
        if result == None:
            return False
        else:
            return True

    # checks whether credentials exist 
    def authLogin(request):
        in_username = request.POST['username']
        in_password = request.POST['password']
        user = authenticate(request, username=in_username, password=in_password)
        if user is not None:
            login(request, user) 
            return True 
        else:
            return False 

# queries involved with matches
class matchMaker:
    # given the user id, returns a list of User objects, where each user in the list is compatible with the given user
    # compatibility is currently determined via a degree comparison
    def findMatches(user_id):
        UserDegree = ExtUser.objects.filter(id=user_id).first().degree
        print(UserDegree)
        result = ExtUser.objects.filter(degree = UserDegree).all()
        print(result)
        return result

    # given a user id, returns a list of other users who are matched to the current user
    def getMatchList(user_id):
        result = []
        matches = Matches.objects.filter(sender = user_id).filter(status = 'a').all()
        for match in matches:
            curr = ExtUser.objects.filter(id = match.sender.id).filter(id != user_id).first()
            result.append(curr)
        matches = Matches.objects.filter(receiver = user_id).filter(status = 'a').all()
        print(matches)
        for match in matches:
            print(user_id)
            print(match.receiver.id)
            curr = ExtUser.objects.filter(id = match.receiver_id).filter(id != user_id).first()
            print(curr)
            result.append(curr)
        return result

    # given a user id, returns a list of other users who have sent a request to the current user
    def getRequestList(user_id):
        matches = Matches.objects.filter(status = 'p').filter(receiver = user_id).all()
        result = []
        for match in matches:
            curr = ExtUser.objects.filter(id = match.sender).first()
            result.append(curr)
        return result

    # given two user ids (first is sender, second is receiver), makes a match request from the first user to the second
    def makeMatchRequest(user1_id, user2_id):
        request = Matches(sender = user1_id, receiver = user2_id, status = 'p')
        request.save()

    # given two user ids (first is sender, second is receiver), accepts the match request from the sender to the receiver, assuming the request has already been made
    def acceptMatch(user1_id, user2_id):
        match = Matches.objects.filter(sender = user1_id).filter(receiver = user2_id).first()
        match.status = 'a'
        match.save()


