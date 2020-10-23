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
        elif "POST" in method:
            print("Post Request")
            return createUser(event)

def getUserPreferences(event):
    if 'queryStringParameters' in event and 'preferences' in event["queryStringParameters"]:
        # Check we have parameters
        request = event["queryStringParameters"]["preferences"]
        try:
            db = access.Access_Db()
            db.getUserPreferences(request)
            return status.success()
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
            return db.createUser(message)
        except ValueError:
            print("Status was not provided")
            return status.failure_parameters()   
    else:
        return status.failure_parameters()

