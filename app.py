import json

def lambda_handler(event, context):
    try:
        parameter1 = int(event['p1'])
        parameter2 = int(event['p2'])
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Missing required parameter: {str(e)}')
        }
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid parameter value.')
        }
    result = parameter1 + parameter2
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
