Title: I've been happily using my AquaRain filter for a little short of a decade now.
Date: 2017-07-04
Tags:  micro, water

My only complaint about [the system](/2008/10/aquarain-water-filtration-systems/) is that the filter elements degrade slowly enough that I rarely notice the decreased flow. Cleaning and assessing the health of the elements (which is done by measuring their circumference with the provided tool) should happen periodically, but it isn't the type of thing I'll ever think to do myself. As with my [water rotation](/2017/07/waterbricks/), I let [taskwarrior](https://taskwarrior.org/) solve the problem for me.

    $ task add project:waterstorage due:2017-07-01 recur:6months wait:due-7days clean and assess aquarain filter
