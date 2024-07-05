Title: Wherein the Author Learns to Compact Borg Archives
Date: 2024-07-05
tags: backups, linux

I noticed that my [Borg](https://www.borgbackup.org/) directory on [The Cloud](https://www.rsync.net/products/borg.html) was 239 GB. This struck me as problematic, as I could see in my local logs that Borg itself reported the deduplicated size of all archives to be 86 GB.

A web search revealed [`borg compact`](https://borgbackup.readthedocs.io/en/stable/usage/compact.html), which apparently I have been meant to run manually [since 2019](https://borgbackup.readthedocs.io/en/stable/changes.html#version-1-2-0a2-and-earlier-2019-02-24). Oops. After compacting, the directory dropped from 239 GB to 81 GB.

My borg wrapper script now looks like this:

    #!/bin/sh
    source ~/.keys/borg.sh
    export BORG_REPO='borg-rsync:borg/nous'
    export BORG_REMOTE_PATH='borg1'

    # Create backups
    echo "Creating backups..."
    borg create --verbose --stats --compression=lz4             \
        --exclude ~/projects/foo/bar/baz                        \
        --exclude ~/projects/xyz/bigfatbinaries                 \
        ::'{hostname}-{user}-{utcnow:%Y-%m-%dT%H:%M:%S}'        \
        ~/documents                                             \
        ~/projects                                              \
        ~/mail                                                  \
        # ...etc

    # Prune
    echo "Pruning backups..."
    borg prune --verbose --list --glob-archives '{hostname}-{user}-*'   \
        --keep-within=1d                                                \
        --keep-daily=14                                                 \
        --keep-weekly=8                                                 \
        --keep-monthly=12                                               \

    # Compact
    echo "Compacting repository..."
    backitup                                \
        -p 604800                           \
        -l ~/.borg_compact-repo.lastrun     \
        -b "borg compact --verbose"         \

    # Check
    echo "Checking repository..."
    backitup -a                                                         \
        -p 172800                                                       \
        -l ~/.borg_check-repo.lastrun                                   \
        -b "borg check --verbose --repository-only --max-duration=1200" \

    echo "Checking archives..."
    backitup -a                                             \
        -p 259200                                           \
        -l ~/.borg_check-arch.lastrun                       \
        -b "borg check --verbose --archives-only --last 18" \

Other than the addition of a weekly `compact`, my setup is the [same as it ever was](/2017/07/borg/).
