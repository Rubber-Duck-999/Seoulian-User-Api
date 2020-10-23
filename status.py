import json


def success():
    return {
        'statusCode': 200,
        'body': json.dumps('Status is correct')
    }

def failure_parameters():
    return {
        'statusCode': 400,
        'body': json.dumps('Incorrect parameters')
    }

def failure_authorization():
    return {
        'statusCode': 401,
        'body': json.dumps('Authorization failure')
    }

def failure_db():
    return {
        'statusCode': 403,
        'body': json.dumps('Forbidden request')
    }
