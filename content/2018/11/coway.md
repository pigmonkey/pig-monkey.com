Title: A Personal Air Filtration System
Date: 2018-11-12
tags: review, gear, air

Another year, and California is burning.

After [Napa burned to the ground last year](https://en.wikipedia.org/wiki/October_2017_Northern_California_wildfires#Air_pollution) I decided to invest in an air filter. I ended up with a [Coway AP-1512HH](https://www.amazon.com/Coway-AP-1512HH-Mighty-Purifier-True/dp/B01728NLRG), which seemed like the right size for my small apartment, and came with a [good recommendation from The Wirecutter](https://thewirecutter.com/reviews/best-air-purifier/).

<a href="https://www.flickr.com/photos/pigmonkey/31983440568/in/dateposted/" title="Coway AP-1512HH"><img src="https://farm5.staticflickr.com/4849/31983440568_36ce4bcd97_c.jpg" width="800" height="450" alt="Coway AP-1512HH"></a>

The unit has three different filters: a pre-filter intended for large dust particles, hair, and the like; a carbon filter to remove odors; and a HEPA filter that does the heavy lifting.

The pre-filter I clean by vacuuming every 4-6 weeks (when I think of it). The carbon filter I've never attempted to clean. The HEPA filter has a 12-month lifespan. The air quality sensor is also supposed to be cleaned every couple months. I've cleaned this once, after about 8 months of service, when I noticed that the unit was constantly registering a high pollution level that I disagreed with. Cleaning the sensor immediately fixed the problem.

The Coway is supposed to light an LED when the HEPA filter needs replacing. My unit has been in use for 12 months now, and that LED has never turned on. I'm not sure why that is, but since the replacement cycle is yearly, and the LED alert is nothing more intelligent than a timer, I simply offloaded the problem to [taskwarrior](https://taskwarrior.org/).

    $ task add project:air due:2018-12-15 recur:yearly wait:due-8weeks "replace Coway AP1512HH filter set (3304899)"

The filter detects pollution and, when placed in automatic mode, adjusts the fan speed appropriately. The current pollution level is indicated by a ridiculously bright LED that can light up a whole room. I've placed a piece of tape over this. This is necessary if the unit is in the same room that you sleep in.

<a href="https://www.flickr.com/photos/pigmonkey/45129936514/in/dateposted/" title="Coway AP-1512HH Control Panel"><img src="https://farm2.staticflickr.com/1928/45129936514_095f461324_c.jpg" width="800" height="450" alt="Coway AP-1512HH Control Panel"></a>

I've enjoyed using the filter throughout the year. It takes care of cooking smells, so that I'm not smelling my dinner all night. I assume the copious dust I clean out of its pre-filter would otherwise end up in my lungs. At its lowest two settings it is quiet enough to leave on overnight, providing pleasant airflow even if I don't need the filtering. During the cooler months when I don't want the extra airflow, I keep the unit in "eco" mode, which disables the fan module when no pollution has been detected for 30 minutes.

However, I had not felt that the cost of the unit justified what I was getting out of it, until California caught fire again. [Since last Thursday](https://en.wikipedia.org/wiki/Camp_Fire_(2018)) San Francisco has been inundated with smoke, requiring the use of a mask during outdoor activity. But I've had clean, clear air indoors. I tried turning the Coway off for a few hours when the [Air Quality Index](https://airnow.gov/index.cfm?action=aqibasics.aqi) was in red. The difference was immediately noticeable. I don't have any measurements to measure the efficacy of the unit on wildfire smoke, but in my qualitative experience, it makes a huge difference.

Living in an area where air quality can become tainted -- which, given climate change, seems to be most areas of human habitation -- I think a personal air filtration system is as important as [water filtration](/2008/10/aquarain-water-filtration-systems/) and [storage](/2017/07/waterbricks/). It is the kind of thing you won't spend much thought on until you need it, at which point its presence or absence can make a significant impact on quality of life.

I have not used any other air filter, so I'm not sure what the best option is, but I have no complaints about the Coway AP-1512HH beyond the LEDs. This past week has moved it from the *would-not-purchase-again* category firmly into my *would-purchase-again-immediately* category.
