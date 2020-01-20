Title: New Year, New Drive
Date: 2020-01-19
Tags: backups, hardware

My first solid state drive was a [Samsung 850 Pro 1TB](https://www.samsung.com/us/computing/memory-storage/solid-state-drives/ssd-850-pro-2-5-sata-iii-1tb-mz-7ke1t0bw/) purchased in 2015. Originally I installed it in my T430s. The following year it migrated to my new [X260](/2016/04/x260/), where it has served admirably ever since. It still seems healthy, as best as I can tell. Sometime ago I found [a script for measuring the health of Samsung SSDs](http://www.jdgleaver.co.uk/blog/2014/05/23/samsung_ssds_reading_total_bytes_written_under_linux.html). It reports:

    ------------------------------
     SSD Status:   /dev/sda
    ------------------------------
     On time:      17,277 hr
    ------------------------------
     Data written:
               MB: 47,420,539.560
               GB: 46,309.120
               TB: 45.223
    ------------------------------
     Mean write rate:
            MB/hr: 2,744.720
    ------------------------------
     Drive health: 98 %
    ------------------------------

The 1 terabyte of storage has begun to feel tight over the past couple of years. I'm not sure where it all goes, but I regularly only have about 100GB free, which is not much of a buffer. I've had my eye on a [Samsung 860 Evo 2TB](https://www.samsung.com/us/computing/memory-storage/solid-state-drives/ssd-860-evo-2-5--sata-iii-2tb-mz-76e2t0b-am/) as a replacement. Last November [my price monitoring tool](https://camelcamelcamel.com/product/B0786QNSBD) notified me of a significant price drop for this new drive, so I snatched one up. This weekend I finally got around to installing it.

The health script reports that my new drive is, in fact, both new and healthy:

    ------------------------------
     SSD Status:   /dev/sda
    ------------------------------
     On time:      17 hr
    ------------------------------
     Data written:
               MB: 872,835.635
               GB: 852.378
               TB: .832
    ------------------------------
     Mean write rate:
            MB/hr: 51,343.272
    ------------------------------
     Drive health: 100 %
    ------------------------------

When migrating to a new drive, the simple solution is to just copy the complete contents of the old drive. I usually do not take this approach. Instead I prefer to imagine that the old drive is lost, and use the migration as an exercise to ensure that my [excessive backup strategies](/tag/backups/) and [OS provisioning system](https://github.com/pigmonkey/spark) are both fully operational. Successfully rebuilding my laptop like this, with a minimum expenditure of time and effort -- and no data loss -- makes me feel good about my backup and recovery tooling.
