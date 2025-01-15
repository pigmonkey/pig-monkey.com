Title: Optimizing Local Munitions
Date: 2025-01-14
tags: linux, backups

As previously mentioned, [I use myrepos to keep local copies of useful code repositories](/2017/06/repos/). While working with backups yesterday I noticed that this directory had gotten quite large. I realized that in the 8 years that I've been using this system, I've never once run [git gc](https://git-scm.com/docs/git-gc) in any of the repos.

Fortunately this is the sort of thing that myrepos makes simple -- even [providing it as an example on its homepage](https://myrepos.branchable.com/). I added two new lines to the `[DEFAULT]` section of my `~/library/src/myrepos.conf` file: one telling it that it can run 3 parallel jobs, and one teaching it how to run `git gc`.

    [DEFAULT]
    skip = [ "$1" = update ] && ! hours_since "$1" 24
    jobs = 3
    git_gc = git gc "$@"

That allowed me to use my existing `lmr` alias to clean up all the git repositories. The software knows which repositories are git, and only attempts to run the command in those.

    $ lmr gc

After completing this process -- which burned through a lot of CPU -- my `~/library/src` directory dropped from 70 GB to 15 GB.

So that helped.
