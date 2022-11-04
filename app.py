from flask import Flask, request
from flask_cors import CORS, cross_origin
from pywebpush import webpush, WebPushException
import json
import config

app = Flask(__name__)
CORS(app)

# VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
# VAPID_PUBLIC_KEY = open(DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")

VAPID_CLAIMS = {
# "sub": "mailto:develop@raturi.in"
"sub": "mailto: <shaikhshahnawaz8821@gmail.com>"
}

def send_web_push(subscription_information, message_body):
    return webpush(
        subscription_info=subscription_information,
        data=message_body,
        vapid_private_key=config.VAPID_PRIVATE_KEY,
        vapid_claims=VAPID_CLAIMS
    )

# PAYLOAD = "Push Test"
PAYLOAD = json.dumps({
            "title": 'Push Test',
            "body": 'Hello From AWS 🚀🤘',
            "icon": 'http://mongoosejs.com/docs/images/mongoose5_62x30_transparent.png'
          })

@app.route('/')
def greet():
    return 'Welcome Sir !'

@app.route('/webpush/show',methods=["POST"])    
def showPushNotification():
    try:
        SUBCRIPTION = request.json
        send_web_push(SUBCRIPTION, PAYLOAD)
        # print('subcription =>>',subcription)
        return 'success'
    except:
        print('some error occured')    