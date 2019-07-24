Title: Undertime
Date: 2019-07-23
Tags: toolchain, linux, shell

[Undertime](https://gitlab.com/anarcat/undertime) is a simple program that assists in coordinating events across time zones. It prints a table of your system's local time zone, along with other any other specified zones. The output is colorized based on the start and end hour of the working day. If you want to talk to someone in Paris tomorrow, and you want the conversation to happen at an hour that is reasonable for both parties, Undertime can help.

![Undertime Paris Meeting Example](/media/images/undertime.png)

I often find myself converting between local time and UTC. Usually this happens when working with system logs. If I have a specific date and time I want to translate, I'll use `date`.

    # Convert a time from PDT to UTC:
    $ env TZ="UTC" date -d "2016-03-25T11:33 PDT"
    # Convert a time from UTC to local:
    $ date -d '2016-03-24T12:00 UTC'

If I'm not looking to convert an exact time, but just want to answer a more generalized question like "Approximately when was 14:00 UTC?" without doing the mental math, I find that Undertime is the quickest solution.

    $ undertime UTC
    ╔═══════╦═══════╗
    ║  PDT  ║  UTC  ║
    ╠═══════╬═══════╣
    ║ 00:00 ║ 07:00 ║
    ║ 01:00 ║ 08:00 ║
    ║ 02:00 ║ 09:00 ║
    ║ 03:00 ║ 10:00 ║
    ║ 04:00 ║ 11:00 ║
    ║ 05:00 ║ 12:00 ║
    ║ 06:00 ║ 13:00 ║
    ║ 07:00 ║ 14:00 ║
    ║ 08:00 ║ 15:00 ║
    ║ 09:00 ║ 16:00 ║
    ║ 10:00 ║ 17:00 ║
    ║ 11:00 ║ 18:00 ║
    ║ 12:00 ║ 19:00 ║
    ║ 13:00 ║ 20:00 ║
    ║ 14:00 ║ 21:00 ║
    ║ 15:00 ║ 22:00 ║
    ║ 16:00 ║ 23:00 ║
    ║ 17:00 ║ 00:00 ║
    ║ 18:00 ║ 01:00 ║
    ║ 19:00 ║ 02:00 ║
    ║ 19:04 ║ 02:04 ║
    ║ 20:00 ║ 03:00 ║
    ║ 21:00 ║ 04:00 ║
    ║ 22:00 ║ 05:00 ║
    ║ 23:00 ║ 06:00 ║
    ╚═══════╩═══════╝
    Table generated for time: 2019-07-23 19:04:00-07:00
