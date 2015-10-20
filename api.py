import requests
import json

from requests.auth import HTTPBasicAuth


def send_confirmation():
  url = 'http://www.robofeedpet.com/api/v1/requests/confirmation'
  payload = {'request': 'success'}
  r = requests.put(url, json=payload)
  return

# r = requests.put('http://www.robofeedpet.com/run_pi', data = {"feed":"yes"})
url = 'http://www.robofeedpet.com/api/v1/requests/new'
headers = {'Authorization': 'Token token="EDlux0E1KtmRT6YDvQRTvQtt"'}

r = requests.get(url, headers=headers)

r = r.json()
print r

if r["request"] == "feed":
  import servo1;
  #send_confirmation();
else:
  print "No food now"







