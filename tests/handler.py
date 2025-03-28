def handle(event, context):
    return {
        "body": {
            "message": 'Hello, world',
        },
        "statusCode": 200,
    }
