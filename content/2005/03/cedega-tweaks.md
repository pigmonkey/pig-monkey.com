Title: Cedega Tweaks
Date: 2005-03-03
Modified: 2012-12-22
Tags: linux
Slug: cedega-tweaks

There's a nice <span class="removed_link">Cedega Tweaking Guide</span> over at LinuxGamers. It's meant for Half-Life 2, but most of the tweaks apply to all games. I did the following
<blockquote>Some distributions need to set up a System-Variable. First, you have to examine if it is set.
cat /proc/sys/vm/legacy_va_layout
No output means, that this Variable isn't set.

As root:
echo 1 > /proc/sys/vm/legacy_va_layout

This setting only survives up to the next reboot. To set up this Variable permanently, open your /etc/sysctl.conf and append
vm.legacy_va_layout = 1</blockquote>
<blockquote>VIDEORAM

Don't forget to set Videoram and AGPVertexRAM to the values of your graphics card. Read the description in the config file and in the release notes of Cedega.
The best value for Videocards with 256MB of Videoram is:
"VideoRam" = "256"
and
"AGPVertexRam" = "128"
Use adjusted values after this pattern for cards with less memory.


ALSA

If you have ALSA then use the winealsa.drv of Cedega. It will give you a small FPS boost.

Open ~/.transgaming/config or ~/.point2play//config and edit the [WinMM] section to

"Driver" = "winealsa.drv"</blockquote>
