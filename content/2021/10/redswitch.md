Title: Redswitch
Date: 2021-10-17
Tags: toolchain, linux, shell

[Redshift](http://jonls.dk/redshift/) is a program that adjusts the color temperature of the screen based on time and location. It can automatically fetch one's location via [GeoClue](https://gitlab.freedesktop.org/geoclue/geoclue/-/wikis/home). I've used it for years. It works most of the time. But, more often than I'd like, it fails to fetch my location from GeoClue. When this happens, I find GeoClue impossible to debug. Redshift [does not cache location information](https://github.com/jonls/redshift/issues/393), so when it fails to fetch my location the result is an eye-meltingly bright screen at night. To address this, I wrote a small shell script to avoid GeoClue entirely.

[Redswitch](https://github.com/pigmonkey/redswitch) fetches the current location via the [Mozilla Location Service](https://location.services.mozilla.com/) (using GeoClue's API key, which [may go away](https://gitlab.freedesktop.org/geoclue/geoclue/-/issues/136)). The result is stored and compared against the previous location to determine if the device has moved. If a change in location is detected, Redshift is killed and relaunched with the new location (this will result in a noticeable flash, but there seems to be no alternative since [Redshift cannot reload its settings while running](https://github.com/jonls/redshift/pull/96)). If Redshift is not running, it is launched. If no change in location is detected and Redshift is already running, nothing happens. Because the location information is stored, this can safely be used to launch Redshift when the machine is offline (or when the Mozilla Location Service API is down or rate-limited).

My laptop does not experience frequent, drastic changes in location. I find that having the script automatically execute once upon login is adequate for my needs. If you're jetting around the world, you could periodically execute the script via cron or a systemd timer.

This solves all my problems with Redshift. I can go back to forgetting about its existence, which is my goal for software of this sort.
