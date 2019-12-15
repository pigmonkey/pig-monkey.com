Title: Personal Information Management
Date: 2019-12-14
Tags: toolchain, linux, shell

[pimutils](https://pimutils.org/) is a collection of software for personal information management. The core piece is [vdirsyncer](https://vdirsyncer.pimutils.org/), which synchronizes calendars and contacts between the local filesystem and CalDav and CardDAV servers. Calendars may then be interacted with via [khal](https://lostpackets.de/khal/), and contacts via [khard](https://github.com/scheibler/khard/). There's not much to say about these three programs, other than they all just work. Having offline access to my calendars and contacts is critical, as is the ability to synchronize that data across machines.

Khard integrates easily with [mutt](https://neomutt.org/) to provide autocomplete when composing emails. I find its interface for creating, editing and reading contacts to be intuitive. It can also output a calendar of birthdays, which can then be imported into khal.

Khal's interface for adding new calendar events is much simpler and quicker than all the mousing required by GUI calendar programs.

    $ khal new 2019-11-16 21:30 5h Alessandro Cortini at Public Works :: 161 Erie St

There are times when a more complex user interface makes calendaring tasks easier. For this Khal offers the [interactive option](https://lostpackets.de/khal/usage.html#interactive), which provides a [TUI](https://en.wikipedia.org/wiki/Text-based_user_interface) for creating, editing and reading events.

Khal can also [import](https://lostpackets.de/khal/usage.html#import) [iCalendar](https://en.wikipedia.org/wiki/ICalendar) files, which is a simple way of getting existing events into my world.

    $ khal import invite.ics

Vdirsyncer has [maintenance problems](https://github.com/pimutils/vdirsyncer/issues/790) that may call its future into question, but the whole point of modular tools that operate on open data formats is that they are replaceable.

I have a simple and often used script which calls `khal calendar` and `task list` (the latter command being [taskwarrior](https://taskwarrior.org/)), answering the question: what am I supposed to be doing right now?
