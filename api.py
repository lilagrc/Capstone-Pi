import requests
import json

from crontab import CronTab

# from requests.auth import HTTPBasicAuth


def send_confirmation():
  url = 'http://www.robofeedpet.com/api/v1/requests/confirmation'
  headers = {'Authorization': 'Token token="0ifRocz56aTevQbdBTbqjQtt"'}
  payload = {'request': 'success'}
  r = requests.put(url, json=payload, headers=headers)
  return

# r = requests.put('http://www.robofeedpet.com/run_pi', data = {"feed":"yes"})
url = 'http://www.robofeedpet.com/api/v1/requests/new'
headers = {'Authorization': 'Token token="0ifRocz56aTevQbdBTbqjQtt"'}

r = requests.get(url, headers=headers)

r = r.json()
print r

if r["feed_request"] == None and r["schedule_request"] == None:
  print "do nothing"
elif r["feed_request"] == "feed" and r["schedule_request"] == None:
  import servo1;
  send_confirmation();
elif r["schedule_request"] != "cancel" and r["feed_request"] == None:
  time = r["schedule_request"]
  time = int(time)

  cron = CronTab(user='root')
  cmd = 'sh /home/pi/schedule_launcher.sh'

  duplicate = None

  for job in cron:
    if job.command == cmd:
      duplicate = "yes"

  if duplicate != "yes":
    new_job = cron.new(cmd)
    new_job.minute.on(0)
    new_job.hour.on(time)
    cron.write()
elif r["schedule_request"] == "cancel":
  tab = CronTab(user='root')
  cmd = 'sh /home/pi/schedule_launcher.sh'

  cron_job = tab.find_command(cmd)
  tab.remove_all(cmd)
  tab.write()
  print "or am i deleting?"
else:
  print "No food now"


#* * * * * sleep 00; sh /home/pi/launcher.sh
#* * * * * sleep 15; sh /home/pi/launcher.sh
#* * * * * sleep 30; sh /home/pi/launcher.sh
#* * * * * sleep 45; sh /home/pi/launcher.sh









