import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('registration_data')


def lambda_handler(event, context):
    response = table.put_item(
       item={
           'email':event['email'],
           'name': event['name'],
           'phone': event['phone'],
           'password': event['password']
       }

    )

    return{
        'statusCode':200,
        'headers':{
            'Content-type':'application/json',
            'Access-control-Allow-Origin': '*'
        },
        'body':json.dumps({'message':'Registration Successful !!'})
    }


# def lambda_handler(event, context):
#     response = table.get_item(Key={
#         'id':'0'
#     })
#     views = response['Item']['views']
#     views = views + 1
#
#     print(views)
#
#     response = table.put_item(Item={
#         'id':'0',
#         'views': views
#     })
#
#     return views
