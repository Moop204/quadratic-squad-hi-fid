from user_profile.models import ExtUser, Degree

class userQueries():
    def findUser(u_id):
        user = ExtUser.objects.filter(id=u_id).first()
        return user 

    def findUserDegree(u_id):
        user = ExtUser.objects.filter(id=u_id).first()
        return user.degree.name

