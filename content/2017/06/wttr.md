Title: Terminal Weather
Date: 2017-06-30
tags: linux

I do most of my computing in the terminal. Minimizing switches to graphical applications helps to improve my efficiency. While the web browser does tend to be superior for consuming and interacting with detailed weather forecasts, I like using [wttr.in](https://github.com/chubin/wttr.in) for answering simple questions like "Do I need a jacket?" or "Is it going to rain tomorrow?"

Of course, weather forecasts are location department. I don't want to have to think about where I am every time I want to use wttr. To feed it my current location, I use [jq](https://stedolan.github.io/jq/) to parse the zip code from the output of [ip-api.com](http://ip-api.com/).

    curl wttr.in/"${1:-$(curl http://ip-api.com/json | jq 'if (.zip | length) != 0 then .zip else .city end')}"
    
I keep this in a shell script so that I have a simple command that gives me current weather for wherever I happen to be -- as long as I'm not connected to a VPN.

    $ wttr
    Weather report: 94107

         \   /     Sunny
          .-.      62-64 °F
       ― (   ) ―   → 19 mph
          `-’      12 mi
         /   \     0.0 in
    ... 
