#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac
import objectpath

##Account Info
AccessId ='25TcJtV3y8wdtHr4iV2I'
AccessKey ='K_D!)R-{bYx(f8yi9zw3))GGq$5jz_3n2-z]pT99'
Company = 'lookingpoint'


##Request Info
httpVerb ='GET'
resourcePath = '/device/devices/'

## Search for any device where the display name contains "PUB"
queryParams ='?filter=displayName~*PUB*&fields=id,displayName'
#queryParams =''
data = ''

##Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath + queryParams

##Get current time in milliseconds
epoch = str(int(time.time() * 1000))

##Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

##Construct signature
signature = base64.b64encode(hmac.new(AccessKey,msg=requestVars,digestmod=hashlib.sha256).hexdigest())
#print signature

##Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature + ':' + epoch
headers = {'Content-Type':'application/json','Authorization':auth}

#print url
#print headers

#Make request
response = requests.get(url, data=data, headers=headers)

#print response

#Print status and body of response
#print 'Response Status:',response.status_code
#print 'Response Body:',response.content

info = response.content
#print(json.loads(info))

##load the json results into a "dictionary"
myjson = json.loads(info)

##grab just the data/items subgroups from the json
myitems = myjson['data']['items']
#print(myjson['data']['items'])

##separate out just the ids and print them
for x in myitems:
	myids = x['id']
	print(myids)

