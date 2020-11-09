import status

class User():

    def __init__(self):
        print("Creating New User")
        self.error = False
        self.username = ""
        self.email = ""
        self.dob = ""
        self.firstName = ""
        self.lastName = ""
        self.createdDate = ""


def newUser(user):
    new_user = User()
    if (user['userAttributes']['email'] or 
        user['userAttributes']['username'] or
        user['userAttributes']['dob'] or
        user['userAttributes']['firstName'] or
        user['userAttributes']['lastName'] or
        user['userAttributes']['createdDate']
    ) is None:
        new_user.error = True
    else:
        new_user.email = user['userAttributes']['email']
        new_user.username = user['userAttributes']['username']
        new_user.dob = user['userAttributes']['dob']
        new_user.firstName = user['userAttributes']['firstName']
        new_user.lastName = user['userAttributes']['lastName']
        new_user.createdDate = user['userAttributes']['createdDate']
    return new_user

def convertUser(row):
    new_user = User()
    print(row)
    if (row[0] or row[1] or row[2] or row[3] or row[4] or row[5]) is None:
        new_user.error = True
    else:
        new_user.id = row[0]
        new_user.email = row[1]
        new_user.username = row[2]
        new_user.dob = row[3]
        new_user.firstName = row[4]
        new_user.lastName = row[5]
        new_user.createdDate = row[6]
    return new_user 
