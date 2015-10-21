import requests
import json

# from requests.auth import HTTPBasicAuth


def send_confirmation():
  url = 'http://www.robofeedpet.com/api/v1/requests/confirmation'
  headers = {'Authorization': 'Token token="rl69KLMDARz3xBdQy3valQtt"'}
  payload = {'request': 'success'}
  r = requests.put(url, json=payload, headers=headers)
  return

# r = requests.put('http://www.robofeedpet.com/run_pi', data = {"feed":"yes"})
url = 'http://www.robofeedpet.com/api/v1/requests/new'
headers = {'Authorization': 'Token token="rl69KLMDARz3xBdQy3valQtt"'}

r = requests.get(url, headers=headers)

r = r.json()
print r

if r["feed_request"] == "feed" and r["schedule_request"] == None:
  import servo1;
  send_confirmation();
elif r["schedule_request"] and r["feed_request"] == None:
 # Need to add logic to deal with times that are sent, which trigger scripts
 print "we're getting there"
else:
  print "No food now"







