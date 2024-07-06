import boto3

def lambda_handler(event, context):
    #Crear un bucket
    nombre_bucket = event['body']['bucket']

    # Proceso
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket)

    return {
        'statusCode': 200,
        'bucket': nombre_bucket
    }