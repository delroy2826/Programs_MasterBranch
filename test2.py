
import requests, json

url_web = "https://outlook.office.com/webhook/257d6d03-de88-4392-8c7e-395cb390d54e@e6cbec2f-2f23-43ca-82c4-51a7c9b71e7a/IncomingWebhook/946d59c00b3c4a6bab4f8ddb84c690b6/7fd3ca2b-4eb7-43c5-bd74-576f3f93c68f"

def postMessageOnSlack(Message):
    url = url_web
    header = {"Content-type": "application/json"}
    payload={"text": Message}
    response_decoded_json = requests.post(url,json.dumps(payload),header)


postMessageOnSlack("Test 5")