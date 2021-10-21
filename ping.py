#!/usr/bin/python3

from influxdb import InfluxDBClient
from datetime import datetime
from pytz import timezone
from pytz import timezone
import subprocess
import re
import datetime

client = InfluxDBClient(host='153.126.210.53',port=8086,database='ping')

#ping 1.1.1.1
ping1 = subprocess.run(["ping","1.1.1.1", "-c","2"],stdout=subprocess.PIPE)

#bye -> str
ping1 = ping1.stdout.decode("utf-8")

p = r'time=(.*)'
m = re.search(p, ping1)
t = m.group(1)
sec_ping1 = re.sub("[^\d.]", "", t)
sec_ping1 = float(sec_ping1)
print(sec_ping1)

#ping 8.8.8.8
ping2 = subprocess.run(["ping","8.8.8.8", "-c","2"],stdout=subprocess.PIPE)

ping2 = ping2.stdout.decode("utf-8")

p = r'time=(.*)'
m = re.search(p, ping2)
t = m.group(1)
sec_ping2 = re.sub("[^\d.]", "", t)
sec_ping2 = float(sec_ping2)
print(sec_ping2)

#ping codeblue.jp
ping3 = subprocess.run(["ping","codeblue.jp", "-c","2"],stdout=subprocess.PIPE)

ping3 = ping3.stdout.decode("utf-8")

p = r'time=(.*)'
m = re.search(p, ping3)
t = m.group(1)
sec_ping3 = re.sub("[^\d.]", "", t)
sec_ping3 = float(sec_ping3)
print(sec_ping3)

#db
#time = datetime.now(timezone('UTC')).isoformat()

json_body = [
    {
        "measurement": "ping",
        "time": datetime.datetime.utcnow(),
        "fields": {
            "ping 1.1.1.1": sec_ping1,
            "ping 8.8.8.8": sec_ping2,
            "ping codeblue.jp": sec_ping3
            }
        }
    ]

client.write_points(json_body)

