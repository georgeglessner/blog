---
layout: post
title:  "DD-WRT DHCP Lease Check"
tags: dd-wrt, dhcp, networking
---

I was looking for a side project to work on one day and thought of being notified whenever a new client connects to your wifi. Of course, I could check the active clients by simply logging on to my router and manually checking, but what fun is that? I wanted a solution that was automated. So I decided to create a simple Python script that checks for new DHCP leases every 15 minutes via a cron job. 

Most people know which devices are connected to their wifi, so this may be of little use. But if you operate a business that has free wifi or are like me and let you neighbor use your wifi, you may want to keep tally of what devices are connected. 

The script works as follows:
1. SSH into the router
2. Get current leases by running `cat /tmp/dnsmasq.leases` 
3. Check those leases against the previous leases
4. If there are any new leases, send me a text / email. 

```python
from credentials import SERVER, USER, PASSWORD, G_USER, G_PASS, G_TO
from email.message import EmailMessage
import paramiko
import smtplib
import re
import os

# connect and execute ssh commands
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(SERVER, username=USER, password=PASSWORD)
stdin, stdout, ssh_stderr = ssh.exec_command("cat /tmp/dnsmasq.leases")

# get current leases from ssh command
leases = stdout.read().decode("utf-8")
stdin.flush()
ssh.close()

# check to see if leaseList.txt exists
# create file if it doesn't
if not os.path.exists("./leaseList.txt"):
    open("leaseList.txt", "a").close()

# initialize current leases array
currentLeases = []

# get current leases MAC addresses
# add to currentLeases array
for lease in leases.split("\n"):
    if len(lease) > 0:
        leaseCheck = re.compile("(?:[0-9a-fA-F]:?){12}")
        activeLeases = re.findall(leaseCheck, lease)
        currentLeases.append("{} : {}".format(activeLeases[0], lease.split()[3]))

# add current leases to leaseList.txt if empty
if os.stat("leaseList.txt").st_size == 0:
    with open("leaseList.txt", "w") as w:
        for lease in currentLeases:
            if len(lease) > 0:
                w.write("{}\n".format(lease))
    w.close()

# create lease list array from leaseList.txt
leaseList = [line.rstrip("\n") for line in open("leaseList.txt")]

# clear out the current lease list
with open("leaseList.txt", "w"):
    pass

# find any new leases, add to array
# add new leases to leaseList.txt
newLeases = []
with open("leaseList.txt", "w") as f:
    for lease in currentLeases:
        f.write("{}\n".format(lease))
        if (len(lease) > 0) and (lease not in leaseList):
            newLeases.append(lease)
f.close()


# send e-mail with new leases
if len(newLeases) > 0:
    # set up message
    msg = EmailMessage()
    msg["Subject"] = "New DHCP Leases Found"
    msg["From"] = G_USER
    msg["To"] = G_TO
    msg.set_content(str(newLeases))

    # send message
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(G_USER, G_PASS)
    s.send_message(msg)
    s.quit()
```

The email configuration is stored in `credentials.py`. To send the notification to multiple addresses, set `G_TO` to a list such as `G_TO = '1234567@vtext.com, test@test.com'`.

## Links
[Script GitHub Repo](https://github.com/georgeglessner/DHCP-Lease-Check)

