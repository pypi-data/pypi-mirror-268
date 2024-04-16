from google.oauth2 import service_account
import google.auth.transport.requests
import requests
from rest import settings
from rest import log


FCM_ENDPOINT = 'https://fcm.googleapis.com/v1/projects/{}/messages:send'

logger = log.getLogger("fcm", filename="fcm.log")


def getCredentials(data):
    # Load the credentials from the dictionary
    credentials = service_account.Credentials.from_service_account_info(
        data,
        scopes=["https://www.googleapis.com/auth/firebase.messaging"])
    # Use the credentials to authenticate a Requests session
    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)
    return credentials


def sendToDevice(device, data):
    return sendData(device.cm_token, data)


def sendNotification(to_token, title, body):
    return postMessage(dict(token=to_token, notification=dict(title=title, body=body)))


def sendData(to_token, data, priority="high"):
    return postMessage(dict(token=to_token, data=data, content_available=True, priority=priority))


def postMessage(credentials, payload):
    logger.info("sending FCM", payload)
    headers = {
        'Authorization': 'Bearer ' + credentials.token,
        'Content-Type': 'application/json; UTF-8',
    }
    body = dict(message=payload)
    resp = requests.post(FCM_ENDPOINT.format(credentials.project_id), headers=headers, json=body)
    logger.info("response", resp.text)
    return resp


