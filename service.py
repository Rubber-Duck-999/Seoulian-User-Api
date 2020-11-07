# -*- coding: utf-8 -*-
import json
import access
import status
import logging
 
class New():

    def __init__(self):
        self.username = ""
        self.email = ""
        self.userId = ""

def handler(event, context):
    # Handler function
    if 'httpMethod' in event:
        method = event["httpMethod"]
        if "GET" in method:
            print("Get Request")
            return getUserPreferences(event)
        elif "PUT" in method:
            print("Update User")
            return status.success()

    elif 'triggerSource' in event:
        if event['triggerSource'] == "PostConfirmation_ConfirmSignUp":
            createUser(event)
        print("Finishing up")
        return event

def getUserPreferences(event):
    if 'queryStringParameters' in event and 'preferences' in event["queryStringParameters"]:
        # Check we have parameters
        request = event["queryStringParameters"]["preferences"]
        try:
            db = access.Access_Db()
            return db.getUserPreferences(request)
        except ValueError:
            print("Status was not provided")
            return status.failure_parameters()   
    else:
        return status.failure_parameters()

def createUser(event):
    print(event["request"])
    if 'request' in event and 'username' in event:
        # Check we have parameters
        new_user = New()
        new_user.email = event["request"]["userAttributes"]["email"]
        new_user.userId = event["request"]["userAttributes"]["sub"]
        new_user.username = event["username"]
        try:
            db = access.Access_Db()
            return db.createUser(new_user)
        except ValueError:
            print("Status was not provided")
            return status.failure_parameters()   
    else:
        return status.failure_parameters()

