---
layout: post
title:  "Simple Flight Logging - PiAware + dump1090"
tags: python, piaware, dump1090
---

If you read my [most recent post](https://www.georgeglessner.com/blog/first-impressions-piaware/) you would know that I recently installed PiAware on one of my Raspberry Pi's. I was very content with my setup... for a few hours. I had two things I was displeased about with my current setup. The first is my antenna / tracking distance, but that is something I plan to fix down the road. My main concern was that I wasn't storing any flight data locally. Not that it really matters, but I wanted to be able to keep track of which flights I had tracked that day, and FlightAware doesn't keep that historical data per user (I think). So, I decided to write a simple Python script to keep track of unique flights I have tracked per day. 

My original plan was to listen to `{hostip}:30003` and parse the messages coming in but that seemed like a less than ideal solution. Through some research, I found that dump1090 actually creates a few useful JSON files with different information. Specifically, they have one with current aircraft information that you are tracking, this is the one I was after! The url for the JSON file is `{hostip}:8080/data/aircraft.json`. 

This JSON file gives you quite a lot of information such as speed, position, flight name / callsign, etc. A full list can be found [here](https://github.com/SDRplay/dump1090/blob/master/README-json.md#aircraftjson). Since I really only wanted to keep track of the unique flights I tracked during the day, I focused on the `flight` key. 

## Solution

My solution is quite simple and basic. The main steps are as follows:

1. Open the current day's CSV file and read the contents. 
2. Load the JSON file
3. Loop through JSON file and add flight to CSV if flight does not exist in the current day's file already. 

The current code is as follows:

```python
from datetime import datetime
from datetime import date
from config import IP_ADDR
import requests
import os
import csv

today = date.today()
time = datetime.now().strftime("%H:%M:%S")

filename = "{}.csv".format(today)
folder = 'flights/'
filepath = folder + filename

if not os.path.isdir(folder):
    os.mkdir('flights')

# check if files exists
file_exists = os.path.isfile(filepath)

# get all flights tracked to check against for duplicates
flights = ""
if file_exists:
    with open(filepath, "r") as fp:
        flights = fp.read()


# get json data
json_dump = requests.get("http://{}:8080/data/aircraft.json".format(IP_ADDR)).json()

# write unique flights for the day to csv file
with open(filepath, "a", newline="") as file:
    writer = csv.writer(file)
    fieldnames = ["flight", "date", "time"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # create headers if first time writing to file
    if not file_exists:
        writer.writeheader()

    # add unique flights for the day
    for entry in json_dump["aircraft"]:
        if "flight" in entry and "{},{}".format(entry['flight'].strip(), today) not in flights:
            writer.writerow(
                {"flight": entry["flight"].strip(), "date": today, "time": time}
            )
```

## Executing

I have this script running on another Raspberry Pi of mine. I created a cron job to run the script every minute, which is fine with me. If you want the script to run more often than that, you can use `watch` or something similar. The crontab is set up as follows:

```bash
* * * * * cd /home/pi/FlightLogger/ && python3 /home/pi/FlightLogger/FlightLogger.py
```

This is sufficient enough to store the data since the data will be stored in `FlightLogger/flights`. 

I wanted to have a public repository of my flight data, so I created a repository called MyFlights. This folder is updated every 2 hours and pushed to GitHub. I created a simple bash script that copies the files from `FlightLogger/flights` into MyFlights and then pushes the changes to GitHub. The bash script is set up as follows:

```bash
#!/bin/bash
cd ~/MyFlights
cp -r ~/FlightLogger/flights .
git add .
git commit -m "Update flight log"
git push origin master
```

That's it for now! I am now able to track _most_ of the flights that I pick up every day and have a central location to look through them. 

### Links

[FlightLogger](https://github.com/georgeglessner/FlightLogger) - The main program 

[MyFlights](https://github.com/georgeglessner/MyFlights) - My personal flights tracked
