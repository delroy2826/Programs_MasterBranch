# import pymsteams
#
# # You must create the connectorcard object with the Microsoft Webhook URL
# teams_webHook = "https://outlook.office.com/webhook/257d6d03-de88-4392-8c7e-395cb390d54e@e6cbec2f-2f23-43ca-82c4-51a7c9b71e7a/IncomingWebhook/946d59c00b3c4a6bab4f8ddb84c690b6/7fd3ca2b-4eb7-43c5-bd74-576f3f93c68f"
#
# myTeamsMessage = pymsteams.connectorcard(teams_webHook)
#
# # Add text to the message.
# myTeamsMessage.text(f"https://s3-chanel-emeav3-ecom-tools-selenium-reports-eu-west-1.s3.eu-west-3.amazonaws.com/result/Run-2020-05-29-19-00-48/Summary.html")
#
# # send the message.
# myTeamsMessage.send()
#
#
# dict1_1 = {"List1":['a','b','c'],"Str1":"Delroy"}
# print(dict1_1["List1"])

import re
def check(str1):
    match = pattern.search(str1)
    return not bool(match)

pattern = re.compile(r'[^\w+]')
str1 = "delro3y1229"
print(check(str1))
str1 = "delro#3y1229"
print(check(str1))
print(int())