---
layout: post
title:  "Home Network Overview"
---

My home network is moderately simple, consisting of a modem, router, and two [raspberry pis](https://www.raspberrypi.org/). I’d like to take the time to go over the what and why of every aspect of my home network.
 
## Modem / Router
Truthfully, the main reason I have this setup is because I got a great package deal via Craigslist. My router is a [Netgear R6400 V2]( https://www.netgear.com/support/product/R6400v2.aspx) and my modem is an [Arris Surfboard SB6183]( https://www.arris.com/surfboard/products/cable-modems/sb6183/). This setup has proven to be very effective, despite everything now being enclosed in a cabinet in my TV stand (I know, I know). I flashed [DD-WRT]( https://dd-wrt.com/) onto my router in order to get the most customization, as the Netgear provided OS was very basic. DD-WRT has worked great for me, allowing me to tweak very advanced settings on my router. The only issue I have, and still have, with DD-WRT is that I am unable to set up a guest network. If I ever get it working, I will be sure to post my solution for future reference. I may upgrade my router at some point in the future, but my current device has proven to be very powerful even in its less than ideal placement.
 
Side note: I also have ~12 devices connected at all times with no problem.
 
## Raspberry Pi (x2)
I currently have two (running) raspberry pis on my network. One is a 3b and the other is a 3b+. Both are connected to my router via ethernet, and have static IP addresses.
 
### Raspberry Pi 1 (3b)
This is what I like to call my “development” raspberry pi. This device is used to host and run a couple Twitter bots, an API I created, some custom scripts, and most importantly [Duck DNS]( https://www.duckdns.org/).

> Duck DNS is a free service which will point a DNS (sub domains of duckdns.org) to an IP of your choice

This allows me to use my Duck DNS domain to point to my networks public IP address, and will update my public IP address anytime it may change. This is very important for my VPN server, which is running on my second raspberry pi. My Duck DNS script runs every 5 minutes from this machine. You can find out how to install Duck DNS [here]( https://www.duckdns.org/install.jsp).
 
### Raspberry Pi 2 (3b+)
This device is more of my “networking” device. I am running  [PiVPN]( http://www.pivpn.io/), [PiHole]( https://pi-hole.net/), and a NAS (Network Attached Storage) powered by [Samba]( https://www.samba.org/) on this device.
 
PiVPN is a VPN server, as its name suggests. I installed PiVPN in order to access my home network no matter where I am. This is very useful for when I am away from home and need to access my router or my NAS. The installation is a very simple, one-line command.

PiHole is “a black hole for Internet advertisements”. I have PiHole setup as a network-wide ad blocker, meaning my router’s DNS is pointed to the IP of my raspberry pi running PiHole (this is why a static IP is important). Currently I have over one million domains on my blocklist, and I average about 35% blocked. I personally love PiHole, I believe it has sped up my browsing time, and it has also improved my quality of browsing by seeing __way__ less ads on pages. A few times, PiHole will block a domain that I need to access, but that is a simple fix by whitelisting the domain from the PiHole GUI. Just like PiVPN, PiHole is a one-line command install. 

<figure>
  <img src="{{site.baseurl}}/assets/images/pihole.png" alt="PiHole Dashboard">
  <center><figcaption>PiHole Dashboard.</figcaption></center>
</figure>


My NAS allows me to store files in a centralized location and access them from any device connected to my network. My NAS is powered by Samba, and the storage device is a 1TB external hard drive. I store backups of my devices and any other files I’d like to be able to access from more than one machine on this device. 


If you have any questions about my home network, or would like me to explain any part of this setup in greater detail, please feel free to reach out to me!