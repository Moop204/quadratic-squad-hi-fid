from user_profile.models import User, Matches

Class matchMaker:
    # given the user id, returns a list of User objects, where each user in the list is compatible with the given user
    # compatibility is currently determined via a degree comparison
    def findMatches(user_id):
        result = User.objects.filter(id != user_id).filter(degree = User.objects.filter(id=user_id).first().degree).all()
        return result

    # given a user id, returns a list of other users who are matched to the current user
    def getMatchList(user_id):
        matches = Matches.objects.filter(sender = user_id or receiver = user_id).filter(MATCH_STATUS = 'a').all()
        result = []
        for (match in matches):
            curr = User.objects.filter((id = match.receiver or id = match.sender) and id != user_id).first()
            result.append(curr)
        return result

    # given a user id, returns a list of other users who have sent a request to the current user
    def getRequestList(user_id):
        matches = Matches.objects.filter(MATCH_STATUS = 'p').filter(receiver = user_id).all()
        result = []
        for match in matches:
            curr = User.objects.filter(id = match.sender).first()
            result.append(curr)
        return result

    # given two user ids (first is sender, second is receiver), makes a match request from the first user to the second
    def makeMatchRequest(user1_id, user2_id):
        request = Matches(sender = user1_id, receiver = user2_id, MATCH_STATUS = 'p')
        request.save()

    # given two user ids (first is sender, second is receiver), accepts the match request from the sender to the receiver, assuming the request has already been made
    def acceptMatch(user1_id, user2_id):
        match = Matches.objects.filter(sender = user1_id).filter(receiver = user2_id).first()
        if match not None:
            match.MATCH_STATUS = 'a'
            match.save()
