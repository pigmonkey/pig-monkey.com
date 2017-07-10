Title: An Inbox for Taskwarrior
Date: 2017-07-09
tags: linux

My experience with all task managements systems -- whether software or otherwise -- is that the more you put into them, the more useful they become. Not only adding as many tasks as possible, however small they may be, but also enriching the tasks with as much metadata as possible. When I began using [taskwarrior](https://taskwarrior.org/), one of the problems I encountered was how to address this effectively.

Throughout the day I'll be working on something when I receive an unrelated request. I want to log those requests so that I remember them and eventually complete them, but I don't want to break from whatever I'm currently doing and take the time to mark these tasks up with the full metadata they eventually need. Context switching is expensive.

To address this, I've introduced the idea of a task inbox. I have [an alias](https://github.com/pigmonkey/dotfiles/blob/master/aliases#L44) to add a task to taskwarrior with a due date of tomorrow and a tag of `inbox`.

    alias ti='task add due:tomorrow tag:inbox'
    
This allows me to very quickly add a task without needing to think about it.

    $ ti do something important
    
Each morning I run `task ls`. The tasks which were previously added to my inbox are at the top, overdue with a high priority. At this point I'll modify each of them, removing the inbox tag, setting a real due date, and assigning them to a project. If they are more complex, I may also add annotations or [notes](https://github.com/ValiValpas/taskopen), or build the task out with dependencies. If the task is simple -- something that may only take a minute or two -- I'll just complete it immediately and mark it as done without bothering to remove the inbox tag.

This alias lowers the barrier of entry enough that I am likely to log even the smallest of tasks, while the inbox concept provides a framework for me to later make the tasks rich in a way that allows me to take advantage of the power that taskwarrior provides.
