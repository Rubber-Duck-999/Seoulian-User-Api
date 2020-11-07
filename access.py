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
        table = dynamodb.Table('Seoulian-User')
        response = table.put_item(
        Item={
                'Email': user["email"],
                'FirstName': user["firstName"],
                'LastName': user["lastName"],
                'Phone': user["phone"],
                'Country': user["country"]
            }
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return status.success()
        else:
            return status.failure_db()

    def getUserPreferences(self, status_request):
        print("Creating query for getting status record")

    