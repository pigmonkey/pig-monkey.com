Title: Unit Wrangling
Date: 2019-07-24
Tags: toolchain, linux, shell

I use [GNU Units](https://www.gnu.org/software/units/) to convert measurements.

The program knows about many obscure and antiquated units, but I mostly use it for boring things like converting currencies and between metric and imperial units. It can be used directly from the command line, or via a prompted interactive mode.

    $ units 57EUR USD
            * 63.526262
            / 0.015741521

    $ units
    Currency exchange rates from FloatRates (USD base) on 2019-07-24
    3460 units, 109 prefixes, 109 nonlinear units

    You have: 16 floz
    You want: ml
            * 473.17647
            / 0.0021133764
    You have: tempC(30)
    You want: tempF
            86

GNU Units is picky about its unit definitions, and they are case sensitive. For example, it knows what `USD` is, but `usd` is undefined. It supports tab completion of units in interactive mode, which can be helpful. It knows the difference between a US fluid ounce and a British fluid ounce.

    $ units "1 usfloz" ml
            * 29.57353
            / 0.033814023

    $ units "1 brfloz" ml
            * 28.413063
            / 0.03519508

The unit definitions are stored at `/usr/share/units/definitions.units`. Occasionally I'll need to peruse through this file to find the correct formatting for the unit I'm interested in. Sometimes when doing this I'll run into one of the more obscure definitions, such as `beespace`. Apparently this unit is used in beekeeping when designing hive boxes. It is described in the definition file thusly: "Bees will fill any space that is smaller than the bee space and leave open spaces that are larger. The size of the space varies with species."

    $ units 12inches beespace
            * 48
            / 0.020833333

Every so often you need to know how many Earth days are in one Martian year. With GNU Units that information is a few keystrokes away.

    $ units 1marsyear days
            * 686.97959
            / 0.0014556473

Currency definitions are stored in `/var/lib/units/currency.units`. They are updated using the `units_cur` program. In the past I would update currencies whenever I needed them, but recently I [setup a systemd timer](https://github.com/pigmonkey/spark/commit/24ef24c34aad89a0f9beb907de51b4aad16adff6) to update these definitions roughly once per day (depending on network connectivity). This provides me with conversion rates that are current enough for my own use, which I can take advantage of even when offline, and does not require me to let a third party know which currencies or quantities I am interested in.

Astute readers will have noted that I am big on this offline computing thing.
