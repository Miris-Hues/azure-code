import json
import urllib

from pyfcm import FCMNotification

req = urllib.request.Request("http://mirishueswebapp.azurewebsites.net/text")
data = urllib.request.urlopen(req).read()
data = data.decode('utf-8')
jsonString = data

asdf = json.loads(jsonString)
sendString = ""
for x in range(len(asdf['regions'])):
    for j in asdf['regions'][x]['lines']:
        for k in j['words']:
            sendString += k['text'] + ' '

print(sendString)

apiKey = 'AAAANjzfayI:APA91bHMX2Vb_Oq23cA4Z9Af7kbzuTQELVxqu2BiirFAxZ8YUUrDGE4pOB85zTKhLhzhl_ai_G0P3MVKn80KvbawN-yu8ZI1kQ9lch5ZWyjR_U-nYvCSde9UUnzUEo8lgWoYM5bz5siY'

push_service = FCMNotification(api_key=apiKey)

push_tokens = 'e6axTmsk9lQ:APA91bHTSkkBsiEUGCw80zuYtoYTGyvS0JmixlBLOj5DWeaQdnqdHdw_Bcen_faD5GHrIBWJ3QUfhdAruFjbCRCQexEn9NM3Ea3xTrRTDin9m4GxV61PNH8aDCkp_3V-16R7gMnW04yH'
message_title = 'hello'

result = push_service.notify_single_device(registration_id=push_tokens,
                                           message_title=message_title,
                                           message_body=sendString)
