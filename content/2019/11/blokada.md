Title: I use Blokada to reduce the amount of advertisements on my telephone.
Date: 2019-11-04
Tags: micro, telephone, toolchain

[Blokada](https://blokada.org/) registers itself as a VPN service on the phone so that it can intercept all network traffic. It then downloads filter lists to route the domains of known advertisers, trackers, etc to a black hole, exactly like what I do on my real computer with [hostsctl](https://github.com/pigmonkey/hostsctl). For me it has had no noticeable impact on battery life. I have found it especially useful when travelling internationally and purchasing cellular plans with small data caps. The only disadvantage I have found is that Blokada must be disabled when I want to connect to a real VPN via WireGuard or OpenVPN.

Blokada must be installed [via F-Droid](https://f-droid.org/en/packages/org.blokada.alarm/) (or directly through the APK) because Google frowns upon blocking advertisements (but at least Google allows you to install software on your telephone outside of their walled garden, [unlike their competitor](https://en.wikipedia.org/wiki/HKmap.live#iOS_app)).
