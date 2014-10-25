Title: Gear Tracker
Date: 2010-12-24
Modified: 2013-05-17
Tags: python, code, gear, django
Slug: gear-tracker

<a href="/gear/">Gear Tracker</a> is an <a href="https://github.com/pigmonkey/django-geartracker">open-source</a> inventory system for wilderness travel gear.

When I first <a href="http://pig-monkey.com/2009/06/19/digital-scale/">bought my scale</a>, I started <a href="https://spreadsheets.google.com/pub?key=rkWMdPMTMCFFQjvJwrWaB9A">a spreadsheet</a> containing the weights of various pieces of gear. It seemed like a good idea -- I knew I wanted some sort of database to store my measured weights and other notes in -- but I never got around to updating it. Data in a spreadsheet is too static. You can't do much with it. I think that characteristic contributed to my disinterest with the spreadsheet.

So for a while now I've had the idea of writing a web application to track my gear. Over the past week, I finally got around to doing it.

Gear Tracker is built on <a href="http://www.djangoproject.com/">Django</a>, a web application framework. (If you're not familiar with Django, and you have anything to do with making websites, it's probably worth your time to <a href="http://www.djangobook.com/">learn a thing or two</a>.)

<!--more-->

<h2>Gear</h2>

Gear Tracker's primary purpose is to track gear.

<a href="/media/geartracker/images/demo/admin-item.png"><img src="/media/geartracker/images/demo/admin-item_thumb.png" alt="Screenshot of item admin" /></a>

Each item has a weight and acquisition date associated with it. It can be categorized, tagged, and related to other items. There are fields to input size, a link to the manufacturer's page, a link to a review, and to upload an image. A text area allows the user to store any notes related to the item.

Items can be archived. This provides a way to not list gear that the user no longer owns, but to keep it in the database for future reference of its weight or other attributes.

<h3>Weights</h3>

Weights are always input in grams.

The metric system makes the most sense and is the easiest to work with. An item's weight can be displayed in grams or, if the item weighs more than 1,000 grams, kilograms. But because some of us are crippled and still like to see imperial weights, Gear Tracker can also display the item's weight in ounces or pounds.

<h2>Gear Lists</h2>

Gear Tracker can also generate gear lists.

One of the things that has prevented me from doing many gear lists in the past is that they're a pain in the rear to create. It takes a while to manually write out every item of gear that I take on a trip. If I want to add the weight of each item -- well, that's asking too much! It's not worth it.

<a href="/media/geartracker/images/demo/admin-gear_list.png"><img src="/media/geartracker/images/demo/admin-gear_list_thumb.png" alt="Screenshot of gear list admin" /></a>

Now, making gear lists is easy. Gear Tracker already has detailed knowledge about each piece of gear. All it takes to create a gear list is to select the item, specify how many of that item I took, and whether the item was packed or carried. The result is an organized, detailed gear list for every trip. Total weights are calculated, of course, and can be output in either metric or imperial units.

<h3>Private Gear Lists</h3>

Gear lists can be made private.

I generally create gear lists when I'm packing before a trip. But I don't like to publish the lists until I actually return from the trip and also have a report and photos for people to peruse. So, Gear Tracker allows a gear list to be marked as private.

<h2>Download It, Hack It, Use It</h2>

I'm running Gear Tracker at <a href="/gear/">/gear</a>, but if you want to grab your own copy and run it yourself, you can! I've open-sourced the code under a BSD-license. You can <a href="https://github.com/pigmonkey/django-geartracker">find it at GitHub</a>.
