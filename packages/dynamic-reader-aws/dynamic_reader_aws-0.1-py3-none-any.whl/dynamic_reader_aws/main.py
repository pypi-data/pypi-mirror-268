#from home.env import config

import boto3
from botocore.client import Config
from django.conf import settings
import json

# Get secret value from AWS Secret Manager




def dynamic_secret_manager(secret_name, value='string', region_name='us-east-1', AWS_ACCESS_KEY_ID="string", AWS_SECRET_ACCESS_KEY="string"):

    
    session = boto3.session.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=region_name,
        
    )
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    # Fetch secret value
    valueof = value
    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
        else:
            print("Error:", e)
        return None
    else:
        if 'SecretString' in response:
            # Parse the SecretString as JSON
            secret_data = json.loads(response['SecretString'])
            # Extract the DJANGO_SECRET_KEY value
            key_value = secret_data.get(valueof)
            if key_value:
                return key_value
            else:
                print("Value not found in the secret.")
                return None
        else:
            print("SecretString not found in the response.")
            return None






