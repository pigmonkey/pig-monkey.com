Title: Resilient Communications with Continuous Wave Radio
Date: 2012-11-18
Modified: 2012-11-18
Tags: radio, censorship, morse
Slug: resilient-communications-continuous-wave-radio

[Codegroup](http://www.fourmilab.ch/codegroup/) is a program written by [John Walker](http://en.wikipedia.org/wiki/John_Walker_(programmer)) that encodes and decodes any file into groups of five letters. For example, take an image, run it through codegroup, and this is what you get:

    $ cat avatar.jpg | codegroup | head -n 4
    ZZZZZ YPPNI PPOAA ABAEK EGEJE GAAAB ABAAA AABAA ABAAA APPPO
    AADLE DFCEF EBFEE PFCDK YCAGH GECNG KHAGF GHCAH GDBCO DACAC
    IHFHD GJGOG HCAEJ EKEHC AEKFA EFEHC AHGDG YDCCJ CMCAH BHFGB
    GMGJH EHJCA DNCAD JDAAK PPNLA AEDAA ADACA CADAC ACADA DADAD

The resulting code groups lend themselves to being transmitted via low-tech, resilient means, such as continuous wave radio. The ability to do this with any file is a simple but amazingly powerful concept.

I discovered codegroup around the same time that I was [learning Morse code](http://pig-monkey.com/2011/09/16/learning-morse-code/). I decided to take advantage of codegroup and put what I was learning into practice. This led to the development of [morse.py](https://github.com/pigmonkey/ham/blob/master/morse.py).

With codegroup, I end up with a series of ASCII characters. I wanted to be able to feed those characters into a program which would convert them to Morse. The program should display the dits and dahs, but more importantly: it should beep them out.

`morse.py` is a simple script which does just that. It accepts ASCII input and encodes it to [International Morse Code](https://en.wikipedia.org/wiki/Morse_code#International_Morse_Code). The Morse is printed to the screen, in case you want to key it out yourself. Johnathan Nightingale's [beep.c](http://www.johnath.com/beep/) is used to play the beeps with the terminal bell. The length of dits, dahs, and the pauses in between are configurable, but the defaults conform to International Morse. The input can be a file, but if no file is specified the script simply reads from standard input, which allows it to be piped together with codegroup.

    $ morse.py --help
    usage: morse.py [-h] [-b BEEP] [-s SPEED] [-f FILE] [-q]

    Convert an ASCII file to International Morse Code and play it with system
    beeps.

    optional arguments:
      -h, --help            show this help message and exit
      -b BEEP, --beep BEEP  The location of the program that plays the beeps. This
                            script is intended to be used with Johnathan
                            Nightingale's beep: http://www.johnath.com/beep/
      -s SPEED, --speed SPEED
                            Reduce the pauses between message characters by the
                            given amount.
      -f FILE, --file FILE  The location of the ASCII file to convert.
      -q, --quiet           Do not print the dots and dashes.

What is the application? Suppose your government has shut down your internet access. You want to send a map to an acquaintance. With these tools, you can encode the map with codegroup, pass the result to morse.py, hold your radio up to your speakers and key the mic. That's it. Censorship bypassed.

    $ cat map.pdf | codegroup | morse.py -b ~/src/beep/beep

On the receiving end, the Morse needs to be translated back to ASCII characters, which can then be decoded with codegroup. It's a slow process, but resilient. To speed things up, the file being transmitted can be compressed before being passed to codegroup. (And if privacy is a concern, the file can also be encrypted, but that would be [illegal](http://www.gpo.gov/fdsys/pkg/CFR-2000-title47-vol5/xml/CFR-2000-title47-vol5-sec97-113.xml) unless you are doing so to [protect life or property](http://www.gpo.gov/fdsys/pkg/CFR-2011-title47-vol5/xml/CFR-2011-title47-vol5-sec97-403.xml).)
