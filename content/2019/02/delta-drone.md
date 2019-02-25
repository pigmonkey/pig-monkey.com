Title: Delta Drone
Date: 2019-02-24
Tags: audio, sleep, shell

Last year [BoingBoing linked to a video](https://boingboing.net/2017/02/06/10-hours-of-ambient-noise-from.html) featuring [delta waves](https://en.wikipedia.org/wiki/Delta_wave) produced by the idling engine of an ice breaker in the arctic. I found it to be a useful tool, so [downloaded it](https://rg3.github.io/youtube-dl/) for offline access. Later, I decided I wanted the audio on my phone. The video is a 10 hour loop, resulting in too large a file for mobile storage. To turn it into something reasonable for a phone, I used ffmpeg to extract the audio, chop it down to 3 hours, and add a 10 second fade on either end.

    $ ffmpeg \
        -i ~/library/video/web/White\ Noise\ Sounds\ of\ Frozen\ Arctic\ Ocean\ with\ Polar\ Icebreaker\ Idling\ -\ Creating\ Delta\ Waves-gpW7iYfuGDU.webm \
        -vn \
        -ss 00:00:00 \
        -t 03:00:00 \
        -af afade=in:st=0:d=10,afade=out:st=10790:d=10 \
        ~/library/audio/misc/soundscape/arctic_white_noise.mp3

I then added ID3 tags from the metadata of the original video.

    $ id3tag \
        --artist="Relax Sleep ASMR" \
        --song="White Noise Sounds of Frozen Arctic Ocean with Polar Icebreaker Idling - Creating Delta Waves" \
        --year=2017 \
        ~/library/audio/misc/soundscape/arctic_white_noise.mp3

The result is a 165 MB file of loopable delta waves, perfect for drowning out the world.

The original video has since been deleted (a reminder to download any data that you find to be useful), but [is available at the Internet Archive](https://archive.org/details/youtube-gpW7iYfuGDU).

<a href="/media/images/delta_waves.jpg"><img src="/media/images/delta_waves-thumb.jpg" width=800 alt="Delta Waves"></a>

The above spectrogram of the file is produced by [Spek](http://spek.cc/).
