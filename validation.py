import status

class User():

    def __init__(self):
        print("Creating New User")
        self.error = False
        self.username = None
        self.email = None
        self.dob = None
        self.firstName = None
        self.lastName = None
        self.createdDate = None


def newUser(user):
    new_user = User()
    if (user['userAttributes']['email'] or 
        user['userAttributes']['username'] or
        user['userAttributes']['dob'] or
        user['userAttributes']['firstName'] or
        user['userAttributes']['lastName'] or
        user['userAttributes']['createdDate']
    ) is None:
        user.error = True
    else:
        user.email = user['userAttributes']['email']
        user.username = user['userAttributes']['username']
        user.dob = user['userAttributes']['dob']
        user.firstName = user['userAttributes']['firstName']
        user.lastName = user['userAttributes']['lastName']
        user.createdDate = user['userAttributes']['createdDate']
    return user    
