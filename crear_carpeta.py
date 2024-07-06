import boto3
import json

def lambda_handler(event, context):
    # Entrada (json)
    info_json= json.loads(event['body'])
    nombre_bucket = info_json['bucket']
    nombre_carpeta = info_json['carpeta']
    
# Proceso
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=f'{nombre_carpeta}/')
        
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Carpeta creada exitosamente',
            'bucket': nombre_bucket,
            'carpeta': nombre_carpeta
        })
    }