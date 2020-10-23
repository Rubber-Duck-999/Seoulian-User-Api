import json
import logging
import uuid
import boto3
import status

class Access_Db():

    status_type   = "latest"

    def __init__(self):
        print("Creation")

    def createUser(self, user):
        print("Creating record in db")
        if user == None:
            return status.failure_db()
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('User-db')
        response = table.put_item(
        Item={
                'UserId': str(uuid.uuid4()),
                'email': user["email"],
                'firstName': user["firstName"],
                'lastName': user["lastName"],
                'phone': user["phone"]
            }
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return status.success()
        else:
            return status.failure_db()

    def getUserPreferences(self, status_request):
        print("Creating query for getting status record")

    