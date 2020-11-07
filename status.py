import json

def return_user(user_found):
    returned_user = json.dumps(user_found.__dict__, default=str)
    return {
        'statusCode': 200,
        'body': returned_user
    }

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
