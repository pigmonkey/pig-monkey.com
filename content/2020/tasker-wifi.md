Title: Managing Android Wifi with Tasker
Date: 2020-12-27
Tags: telephone

One of the earliest programs I installed when I bought my first smartphone in 2013 was [Kismet's Smarter Wi-Fi Manager](https://web.archive.org/web/20160304051134/https://kismetwireless.net/android-swm/). It kept the phone's wireless radio disabled unless I explicitly enabled it and connected to a network. When that happened, it would store the location by identifying nearby cell towers. Whenever it saw those towers again, it would turn the wireless radio on. In all other cases it would keep the radio off. This was a simple solution to the problem of only wanting wifi turned on at known locations, like home and work. It helped save battery, and prevented information leaks when wandering around meatspace.

Recently, when setting up a new phone, I discovered that Smarter Wi-Fi Manager had been abandoned. I thought I had heard something about the behaviour being integrated into the latest version of Android, but it seems that is not the case. Fortunately I found that [Tasker](https://tasker.joaoapps.com/) can be configured to replicate the behaviour.

In Tasker, a profile can be created to recognize a location using [a few different means](https://tasker.joaoapps.com/userguide/en/loctears.html). I setup one profile for home and one for work, both using the "cell near" context state. Like the Smarter Wi-Fi Manager of old, this just stores the identities of nearby cell towers. Then I created two tasks: one to turn wifi on and one to turn it off. The first task is added to both profiles as the main task. The latter is added to the profiles as the exit task. The result is that when the phone sees the cell towers near my trusted locations, the wireless radio turns on. When I leave, the wireless radio turns off.


    Profile: Home (1)
        Restore: no
        State: Cell Near [ ... bunch o' towers here ... ]
        Enter: Wifi On (4)
            A1: WiFi [ Set:On ]
        Exit: Wifi Off (9)
            A1: WiFi [ Set:Off ]

    Profile: Work (2)
        Restore: no
        State: Cell Near [ ... bunch o' towers here ... ]
        Enter: Wifi On (4)
            A1: WiFi [ Set:On ]
        Exit: Wifi Off (9)
            A1: WiFi [ Set:Off ]

The task to turn the wireless off is only triggered when I leave the location, which means I can still manually turn the radio on when I am somewhere unknown without Tasker immediately turning it back off. That new location will not automatically be stored as a trusted location, but if I want it to be remembered it only takes a minute to create a new profile and hook it up to my two wifi tasks.

I found the Tasker interface to be somewhat confusing. It took me a while to figure out how to achieve my desired behaviour. This is probably because [Tasker can do a lot of other things](https://tasker.joaoapps.com/exampleuses.html). I don't think my phone is integrated enough into my life to make its other capabilities relevant to me (though I might set it up to [only enable GPS when mapping applications are open](https://forum.joaoapps.com/index.php?resources/turn-gps-on-when-in-google-maps-turn-it-off-otherwise-no-root.179/)), but I was happy to pay the low price to retake control of my wireless radio.
