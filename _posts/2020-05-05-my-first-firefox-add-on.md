---
layout: post
title:  "My First Firefox Add On"
tags: firefox, javascript
---

Tonight I decided to make my first Firefox add-on. I have thought about creating one for a while, but just didn't know what I wanted to create. My original idea was to make a plugin that would "listen" for a change on the local page you were on to see if the file had been modified and refresh the page if it was. Well, that was short lived because I am limited to only using vanilla javascript for add-ons. So, I thought of another idea. 

Recently Instagram implemented a feature on their web application that makes it so you cannot view a user's pictures without being logged in. So I decided I would create an add-on to get around this. The solution ended up being **very** simple, but it took me a while to figure out what needed to be done. 

The plugin works by finding the `href` of the image you clicked on, and opens the url to that photo / photo set in a new tab. That's it. 

The popup does still appear when you click on a picture and are brought to the new tab to view that picture. This makes it annoying when you close out of the picture tab to go back to the main page and are greeted with that pesky popup. I will try fixing this soon. 

You can download the add-on [here](https://addons.mozilla.org/en-US/firefox/addon/instasee/) and the source code can be found [here](https://github.com/georgeglessner/InstaSee).

## [Changelog ](https://github.com/georgeglessner/InstaSee/releases)
