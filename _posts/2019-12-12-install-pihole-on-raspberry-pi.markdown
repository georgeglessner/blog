---
layout: post
title:  "How to Install PiHole on a Raspberry Pi"
---

Before we begin, I will assume that you already have your raspberry pi set up and are able to log in. If not, you can find guides on how to do that [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up). 

## Step 1
Log in to your rapsberry pi. You may also ssh into your machine and follow this guide via ssh.

`ssh pi@IP_ADDRESS`

## Step 1
Open terminal and enter the following command to begin installation. 

`curl -sSL https://install.pi-hole.net | bash`

The install script will perform a few checks before proceeding. 

## Step 3
If all the checks passed in step 2, you should see a screen that looks like the following

<figure>
  <img src="{{site.baseurl}}/assets/welcome-pihole.png" alt="PiHole Dashboard">
</figure>

Hit enter to continue through the first few welcome messages until you arrive at this screen
<figure>
  <img src="{{site.baseurl}}/assets/interface-pihole.png" alt="PiHole Dashboard">
</figure>
## Step 4
Choose either `eth0` (ethernet) or `wlan0` (wireless). I prefer an ethernet connection, but use whatever you prefer. This particular device I am installing PiHole on is connected via WiFi so I will select `wlan0`. 

__Tip:__ Use the up/down arrow keys to change selection and the space bar to select. Hit enter to move to next screen. Left/right keys are used to select "ok" and "cancel".  

## Step 5
Next it will ask you to choose an upstream DNS provider. I always go with Google, but choose whichever you prefer. 
<figure>
  <img src="{{site.baseurl}}/assets/dns-pihole.png" alt="PiHole Dashboard">
</figure>

## Step 6
Next it will ask you to choose a block list, don't worry about which one you choose as you can add alternative ones later. Pick whichever one you would like for now. 
<figure>
  <img src="{{site.baseurl}}/assets/block-list-pihole.png" alt="PiHole Dashboard">
</figure>
## Step 7
Select the protocol you wish to use. Most likely this will be IPv4. 
<figure>
  <img src="{{site.baseurl}}/assets/protocol-pihole.png" alt="PiHole Dashboard">
</figure>
## Step 8 
This is where you can set your static IP if you do not already have one set. If you select "Yes" here, make sure you note what your current IP address is as this will be the IP address you will use from now on for this machine. 
<figure>
  <img src="{{site.baseurl}}/assets/ip-address-pihole.png" alt="PiHole Dashboard">
</figure>
## Step 9
Next it will ask you if you would like to install the web admin interface (GUI). I highly recommend you do as this makes modifying your PiHole settings and visualizing the statics much easier. 
<figure>
  <img src="{{site.baseurl}}/assets/web-interface-pihole.png" alt="PiHole Dashboard">
</figure>
## Step 10
This step asks if you would like to install the webserver. If you do not have a webserver already installed you must select "on" in order to use the GUI. 
<figure>
  <img src="{{site.baseurl}}/assets/web-server-pihole.png" alt="PiHole Dashboard">
</figure>
## Step 11
Next it will ask if you would like to log queries. Enabling this will allow you to see all the domains devices connected to PiHole have tried to access. 
<figure>
  <img src="{{site.baseurl}}/assets/queries-pihole.png" alt="PiHole Dashboard">
</figure>
## Step 12
Next it will ask which level of privacy you want. I suggest you show everything, but choose whatever you are most comfortable with. 
<figure>
  <img src="{{site.baseurl}}/assets/privacy-pihole.png" alt="PiHole Dashboard">
</figure>
PiHole will finsih the installation process and apply all the settings you have chosen. 

## Step 13
Run the following command to set a new admin password. 

`sudo pihole -a -p` 

If everything was successful, you should now be able to open a web browser and go to `PIHOLE_IP_ADDRESS/admin` and see the GUI. 

<figure>
  <img src="{{site.baseurl}}/assets/GUI-pihole.png" alt="PiHole Dashboard">
</figure>
Click "Login" and enter the admin password you set in step 13. 

Congratulations! You have successfully set up PiHole. If you would like to specify only certain devices to use PiHole, simply set their DNS server to the IP address of your PiHole. If you would like to set up network wide ad blocking, continue reading. 

## Network Wide Ad Blocking

To enable network wide ad blocking, we must set our router's DNS to point to the IP address of our PiHole. All routers are different, so you may need to look up how to do it for your particular router. If your router does not allow you to modify the DNS settings, you can set the DNS for individual devices as stated previously. 

My DNS settings are located under "Setup". I set my primary DNS to be my PiHole IP address. If you would like to add redundancy in case your PiHole loses connectivity, you may duplicate your setup on another device and add that IP address as a backup DNS server. 

<figure>
  <img src="{{site.baseurl}}/assets/router-dns.png" alt="PiHole Dashboard">
</figure>

## Adding Additional Block Lists
Once logged in to the PiHole GUI, go to Settings -> Blocklists. Here you will see all of the blocklists currently installed. There are many resources online providing you with blocklists for all sort of different blocking scenarios. One of my favorite lists is `https://dbl.oisd.nl`. You can find out more information about this blocklist [here](https://www.reddit.com/r/oisd_blocklist/comments/dwxgld/dbloisdnl_internets_1_domain_blocklist/). Once you have added the lists you want, click "Save and Update". PiHole will update and add the new lists. 
<figure>
  <img src="{{site.baseurl}}/assets/add-blocklist-pihole.png" alt="PiHole Dashboard">
</figure>

<figure>
  <img src="{{site.baseurl}}/assets/gravity-success-pihole.png" alt="PiHole Dashboard">
</figure>

You should now see over 1 million domains on your blocklist!

<figure>
  <img src="{{site.baseurl}}/assets/GUI-update-pihole.png" alt="PiHole Dashboard">
</figure>

If you have any questions, please feel free to contact me. 
