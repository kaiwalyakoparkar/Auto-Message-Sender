import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get requests
def sendPostRequest(reqUrl, apiKey, secretKey, usetype, phoneNo, senderId, textMesage):
    req_params = {
        'apikey':apiKey
        'secret':secretKey
        'usetype':usetype
        'phone':phoneNo
        'message':textMesage
        'senderid':senderId
    }
return requess.post(reqUrl, req_params)

# get response

response = sendPostRequest(URL, '', '', 'stage', '', '', '')

"""
Note :-
You must provide apikey, secretkey, usetype, mobile, senderid and message values and then request to api
"""

# print response if needed
# print(response.txt)