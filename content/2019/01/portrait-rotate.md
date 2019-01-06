Title: The Kindle is a terrible device for reading comics.
Date: 2019-01-05
Tags: micro, books, hardware

It's the wrong size. The E Ink display is greyscale. Zooming and panning are disruptive. A tablet probably works great, but I don't know -- I've never owned one. I solved the problem a while back when I discovered that I could simply rotate my laptop's display via [xrandr](https://wiki.archlinux.org/index.php/Xrandr).

    $ xrandr --output eDP-1 --rotate right --pos 0x0

Adding an [autorandr profile](https://github.com/pigmonkey/dotfiles/commit/25f88620930f3962db73a984a55b3c51e9cab647) for this makes it easy to jump to portrait mode. This is useful for reading any long-form content on the X260. Typing (or mousing) on the rotated device is difficult, so I'll sometimes plug in my external keyboard if I want to do more than just page through a document.

<a href="https://www.flickr.com/photos/pigmonkey/46570367582/in/dateposted/" title="X260 Portrait Mode"><img src="https://farm8.staticflickr.com/7871/46570367582_efa665e74c_c.jpg" width="800" height="450" alt="X260 Portrait Mode"></a>
