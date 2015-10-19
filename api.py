import requests
import json


def send_confirmation():
  url = 'http://www.robofeedpet.com/pi_confirmation'
  payload = {'request': 'success'}
  r = requests.put(url, json=payload)
  return

# r = requests.put('http://www.robofeedpet.com/run_pi', data = {"feed":"yes"})
r = requests.get('http://www.robofeedpet.com/run_pi')

r = r.json()
print r

if r["request"] == "feed":
  import servo1;
  send_confirmation();
else:
  print "No food now"







