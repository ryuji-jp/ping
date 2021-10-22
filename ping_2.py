#!/usr/bin/python

from influxdb import InfluxDBClient
from datetime import datetime
from pytz import timezone
from pytz import timezone
import subprocess
import re
import datetime

client = InfluxDBClient(host='153.126.210.53',port=8086,database='ping')

sec_ping1 = 0
sec_ping2 = 0
sec_ping3 = 0


#ping ping-hokkaido.sinet.ad.jp
ping1 = subprocess.run(["ping","ping-hokkaido.sinet.ad.jp", "-c","2"],stdout=subprocess.PIPE)

#bye -> str
ping1 = ping1.stdout.decode("utf-8")

p = r'time=(.*)'
m = re.search(p, ping1)
t = m.group(1)
sec_ping1 = re.sub("[^\d.]", "", t)
sec_ping1 = float(sec_ping1)
print(sec_ping1)

#ping ping-iwate.sinet.ad.jp
ping2 = subprocess.run(["ping","ping-iwate.sinet.ad.jp", "-c","2"],stdout=subprocess.PIPE)

ping2 = ping2.stdout.decode("utf-8")

p = r'time=(.*)'
m = re.search(p, ping2)
t = m.group(1)
sec_ping2 = re.sub("[^\d.]", "", t)
sec_ping2 = float(sec_ping2)
print(sec_ping2)

#ping ping-tokyo.sinet.ad.jp
ping3 = subprocess.run(["ping","ping-tokyo.sinet.ad.jp", "-c","2"],stdout=subprocess.PIPE)

ping3 = ping3.stdout.decode("utf-8")

p = r'time=(.*)'
m = re.search(p, ping3)
t = m.group(1)
sec_ping3 = re.sub("[^\d.]", "", t)
sec_ping3 = float(sec_ping3)
print(sec_ping3)

#ping ping-osaka.sinet.ad.jp
ping4 = subprocess.run(["ping","ping-osaka.sinet.ad.jp", "-c","2"],stdout=subprocess.PIPE)

ping4 = ping4.stdout.decode("utf-8")

p = r'time=(.*)'
m = re.search(p, ping4)
t = m.group(1)
sec_ping4 = re.sub("[^\d.]", "", t)
sec_ping4 = float(sec_ping4)
print(sec_ping4)

#ping ping-okinawa.sinet.ad.jp
ping5 = subprocess.run(["ping","ping-okinawa.sinet.ad.jp", "-c","2"],stdout=subprocess.PIPE)

ping5 = ping5.stdout.decode("utf-8")

p = r'time=(.*)'
m = re.search(p, ping5)
t = m.group(1)
sec_ping5 = re.sub("[^\d.]", "", t)
sec_ping5 = float(sec_ping5)
print(sec_ping5)

#db
#time = datetime.now(timezone('UTC')).isoformat()

json_body = [
    {
        "measurement": "ping",
        "time": datetime.datetime.utcnow(),
        "fields": {
            "ping ping-hokkaido.sinet.ad.jp": sec_ping1,
            "ping ping-iwate.sinet.ad.jp": sec_ping2,
            "ping ping-tokyo.sinet.ad.jp": sec_ping3,
            "ping ping-osaka.sinet.ad.jp": sec_ping4,
            "ping ping-okinawa.sinet.ad.jp": sec_ping5
            }
        }
    ]

client.write_points(json_body)
