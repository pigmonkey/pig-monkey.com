Title: Mobile Weather
Date: 2019-01-09
Tags: android

[Los Angeles is suing The Weather Channel for selling the data of mobile users](https://www.nytimes.com/2019/01/03/technology/weather-channel-app-lawsuit.html). This behaviour shouldn't be surprising. Most mobile software, from the operating system on up, seems to exist primarily to provide some base modicum of functionality in exchange for the privilege of fucking you in new and exciting ways.

There are exceptions to the rule. I starting using [Arcus](http://www.arcusweather.com) for mobile weather in 2014, and it seems pretty respectable. But it exists solely to display data from the [Dark Sky API](https://darksky.net/dev), which is something that a web browser is also capable of doing, thus raising the question: why install anything?

About a month ago I simply bookmarked [Dark Sky](https://darksky.net/)'s website and had [Firefox](https://www.mozilla.org/en-US/firefox/mobile/) add a shortcut to that bookmark on my home screen. Dark Sky's website is responsive, so it works fine in any viewport size. I bookmarked the URL for my home location, allowing me to see weather at home in a single tap. Elsewhere, it required two taps: one tap to open the bookmark, and one tap on their geolocation icon to get the correct forecast for my current location.

I find Dark Sky's data to be great for reporting on the hyper-local now. For reports that are wider in scope -- either in terms of time or space -- nothing beats the [National Weather Service](https://www.weather.gov/). They provide a [mobile specific site](https://mobile.weather.gov/) that is perfectly usable on small viewports. Annoyingly, they don't make use of the [web geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API), instead requiring users to manually enter a location. When travelling I may not know what zip code I'm in or have a nearby address. To work around this I created a shim with a few lines of Javascript that geolocates the user, uses the resulting coordinates to build the proper NWS URL, and redirects the user to that URL. I also added support for building a Dark Sky URL so that I could avoid that second tap when not at home.

    :::html
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Geoweather</title>
            <link rel="icon" type="image/ico" href="https://www.weather.gov/favicon.ico">
            <script>
                function geoWeather() {
                    navigator.geolocation.getCurrentPosition(function(pos) {
                        var currentURL = new URL(window.location.href);
                        if (currentURL.searchParams.has('darksky')) {
                            var forecastURL = 'https://darksky.net/forecast/' + pos.coords.latitude + ',' + pos.coords.longitude;
                        } else if (window.screen.width < 800) {
                            var forecastURL = 'https://mobile.weather.gov/index.php?lat=' + pos.coords.latitude + '&lon=' + pos.coords.longitude;
                        } else {
                            var forecastURL = 'https://forecast.weather.gov/MapClick.php?lat=' + pos.coords.latitude + '&lon=' + pos.coords.longitude;
                        }
                        var el = document.getElementById('result');
                        el.innerHTML = '<p>Forecast URL is <a href="' + forecastURL + '"> ' + forecastURL + '</a></p>';
                        window.location.replace(forecastURL);
                    });
                }
                window.onload = geoWeather;
            </script>
        </head>
        <body>
            <div id="result"></div>
        </body>
    </html>

Now I have two URLs bookmarked on my home screen that accomplish everything I need: [one for NWS](https://havenaut.net/weather/) and [one for Dark Sky](https://havenaut.net/weather/?darksky).

Shortly after creating this shim I discovered that the NWS has a [beta website](https://forecast-v3.weather.gov/) that is intended to replace both the current mobile and standard sites with a consistent interface. This site does make use of the geolocation API, requiring the user to click an icon to get the current location. It is unclear why they have yet to deploy this to their main domain. It's been [available since August 2017](http://www.nws.noaa.gov/os/notification/scn16-55forecast_govaae.htm) and the [data on the beta site](https://forecast-v3.weather.gov/point/37.7602,-122.3941) seems to be the same as the [data on the standard site](https://forecast.weather.gov/MapClick.php?lat=37.76022&lon=-122.3941) and the [data on the mobile site](https://mobile.weather.gov/index.php?lat=37.76022&lon=-122.3941). For now I'm sticking with the officially supported domains in my shim.

A locally installed weather program is useful if your requirements include lock screen widgets or notifications of hazardous conditions. Mine do not. These two bookmarks provide all the weather information I need on my telephone, and do so in a way that does not expand my attack surface in the way installing software does. They are indicative of the usefulness of this [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web) thing --  an emerging technology that I intend to watch with great interest. I think it'll go places.