from user_profile.models import User, Matches

Class matchMaker:
    # given the user id, returns a list of User objects, where each user in the list is compatible with the given user
    # compatibility is currently determined via a degree comparison
    def findMatches(user_id):
        result = User.objects.filter(id != user_id).filter(degree = User.objects.filter(id=user_id).first().degree).all()
        return result

    def makeMatchRequest(user1_id, user2_id):
        request = Matches(sender = user1_id, receiver = user2_id, MATCH_STATUS = 'p')
        request.save()

    def acceptMatch(match_id):
        match = Matches.objects.filter(id = match_id).first()
        if match not None:
            match.MATCH_STATUS = 'a'
            match.save()
