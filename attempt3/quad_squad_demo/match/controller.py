from user_profile.models import ExtUser, Matches

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
