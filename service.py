# -*- coding: utf-8 -*-
import json
import access
import status
import logging
 
def handler(event, context):
    # Handler function
    if 'httpMethod' in event:
        method = event["httpMethod"]
        if "GET" in method:
            print("Get Request")
            return getUserPreferences(event)
    elif 'triggerSource' in event:
        print(event)
        return createUser(event)

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
    if 'queryStringParameters' in event and 'user' in event["queryStringParameters"]:
        # Check we have parameters
        message = event["queryStringParameters"]["user"]
        try:
            db = access.Access_Db()
            return status.success()
            #return db.createUser(message)
        except ValueError:
            print("Status was not provided")
            return status.failure_parameters()   
    else:
        return status.failure_parameters()

