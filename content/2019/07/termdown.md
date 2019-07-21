Title: Terminal Countdown
Date: 2019-07-20
Tags: toolchain, linux, shell

[Termdown](https://github.com/trehn/termdown) is a program that provides a countdown timer and stopwatch in the terminal. It uses [FIGlet](http://www.figlet.org/) for its display. Its most attractive feature, I think, is the ability to [support arbitrary script execution](https://github.com/trehn/termdown/issues/44).

I use it most often as a countdown timer. One of my frequent applications is as a meditation timer. For this I want a 11 minute timer, with an alert at 10.5 minutes, 60 seconds, and 1 second. This gives me a 10 minute session with 30 seconds preparation and 30 seconds to return. Termdown makes this easy.

    $ termdown --exec-cmd "case {0} in 630|30) mpv ~/library/audio/sounds/bell.mp3;; 1) mpv ~/library/audio/sounds/ring.mp3;; esac" 11m
