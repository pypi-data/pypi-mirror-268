from datetime import datetime
import json
import os
import time
import boto3
import pytz

sqs = boto3.client('sqs', region_name='us-east-1')
queue_url = 'https://sqs.us-east-1.amazonaws.com/764374292299/setnext_metering'

from langchain_community.llms import Bedrock

llm = Bedrock(model_id="anthropic.claude-v2:1",
              region_name="us-east-1",
              )


def count_token(message):
    num_token = llm.get_num_tokens(message)
    print("Num of Token Found", num_token)
    return num_token

def send(message, token_type):
    try:
        clientId = os.environ.get("CLIENT_ID")
        cloud_platform = os.environ.get("CLOUD_PLATFORM")
        ai_platform = os.environ.get("AI_PLATFORM")
        model_id = os.environ.get("MODEL_ID")
        application_name = os.environ.get("APPLICATION_NAME")
        setnext_ai_metering_api_token = os.environ.get("SETNEXT_METERING_API_TOKEN")

        token = count_token(message)
        tokenSize = "s"
        current_datetime = datetime.now().isoformat()
        current_unix_ts = int(time.mktime(datetime.now().timetuple()))
        tzInfo = pytz.timezone('Asia/Kolkata')

        fmt = '%d-%m-%Y %H:%M:%S %Z%z'
        india_date_time = datetime.fromtimestamp(current_unix_ts, tz=tzInfo).strftime(fmt)

        if token < 300:
            tokenSize = "s"
        elif 300 <= token <= 600:
            tokenSize = "m"
        elif 601 <= token <= 1000:
            tokenSize = "l"
        elif 1001 <= token <= 2000:
            tokenSize = "xl"
        elif 2001 <= token <= 3000:
            tokenSize = "xxl"
        elif 3001 <= token <= 4000:
            tokenSize = "xxxl"
        else:
            tokenSize = "4xl"

        messageBody = {"clientId": clientId, "num_of_token": token, "tokenSize": tokenSize, "cloud": cloud_platform,
                       "ai_plaform": ai_platform, "model_id": model_id, "application_name": application_name,
                       "date_time": current_datetime, "token_type": token_type, "india_date_time": india_date_time,
                       "unix_ts": current_unix_ts}

        response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageAttributes={
                'clientId': {
                    'DataType': 'String',
                    'StringValue': clientId
                },
                'application_name': {
                    'DataType': 'String',
                    'StringValue': application_name
                },
                'dateTime': {
                    'DataType': 'String',
                    'StringValue': current_datetime
                },
                'api_token': {
                    'DataType': 'String',
                    'StringValue': setnext_ai_metering_api_token
                }
            },
            MessageBody=json.dumps(messageBody)
        )
        print("Message Sent")
        return {"status": "success"}
    except Exception as err:
        print("Exception Occure while pushing the metrics, Error :", err)
        return {"status": "failed", "error": err}


def receive(client_id):
    return client_id + ":" + "Hello"


send("Hello How are you", "input")
