import requests

# r = requests.put('http://www.robofeedpet.com/run_pi', data = {"feed":"yes"})
r = requests.get('http://www.robofeedpet.com/run_pi')

r = r.json()
print r

if r["request"] == "feed":
  import servo1
else:
  print "No food now"


