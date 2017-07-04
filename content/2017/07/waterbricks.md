Title: Water Rotation
Date: 2017-07-03
tags: water

I use four [WaterBricks](http://www.waterbrick.org/) for water storage at home, and for the occasional vehicle-borne excursions. They're simple to store in small areas, stack securely, and are easy to pour from with the [spigot assembly](http://www.waterbrick.org/product/ventless-spigot-assembly/). I prefer them over the more common [Scepter Water Canisters](http://civ.sceptermilitary.com/water_containers). The 3.5 gallon capacity of the WaterBricks is in the sweet spot of being able to hold a lot of water, but isn't so heavy that life sucks when you need to haul them around.

I took one of the WaterBricks on this year's [ARRL Field Day](http://www.arrl.org/field-day) last month. This was the first time this particular WaterBrick had been opened in three years. The water tasted fine, albeit with a plasticy flavor that wasn't surprising, but storing water for this length of time seems at best excessive and at worse negligent. I took this as an opportunity to implement a rotation schedule.

Each of the WaterBricks is now labelled. They are grouped in to two 12-month rotation periods, each six months apart. This provides an opportunity to not only change the water, but also bleach and dry the inside of the containers to discourage any growth. By performing the rotation six months apart, I can be assured of always having two full WaterBricks on hand.

By scheduling the rotation in [taskwarrior](https://taskwarrior.org/) I never have to think about it.

    $ task add project:waterstorage due:2017-06-01 recur:yearly wait:due-7days rotate waterbrick alpha
    $ task add project:waterstorage due:2017-06-01 recur:yearly wait:due-7days rotate waterbrick bravo
    $ task add project:waterstorage due:2017-12-01 recur:yearly wait:due-7days rotate waterbrick charlie
    $ task add project:waterstorage due:2017-12-01 recur:yearly wait:due-7days rotate waterbrick delta
    
I use 28 drops of Aquamira chlorine dioxide per WaterBrick, although I'm not sure how necessary that is now with the rotation schedule.
