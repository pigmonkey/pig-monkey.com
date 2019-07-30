Title: Date Manipulation
Date: 2019-07-29
Tags: toolchain, linux, shell

[Dateutils](http://www.fresse.org/dateutils/) is a collection of tools for the quick manipulation of dates. The tool I use most frequently is `datediff`. This program answers questions like: "How many days has it been since a date?" or "How many days are left in summer?"

    $ datediff 2019-03-21 now
    131
    $ datediff now 2019-09-23
    55

My second most frequently used program is `dateadd`, which is used to add a duration to a date. It can answer questions like: "What will the date be in 3 weeks?"

    $ dateadd now +3w
    2019-08-20T02:02:23

The tools are much more powerful than these examples, but hardly a week goes by when I don't use `datediff` or `dateadd` for simple tasks like this.
