Title: The Things I Do for Time
Date: 2024-02-14
Tags: linux

I am a believer in the sacred word as defined in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), and the later revelations such as [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339). Numerical dates should be formatted as YYYY-MM-DD. Hours should be written in 24-hour time. I will die on this hill.

Since time immemorial, this has been accomplished on Linux systems by setting `LC_TIME` to the en_DK locale. More specifically, the git history for glibc shows that en_DK was added (with ISO 8601 date formatting) by Ulrich Drepper on 1997-03-05.

A few years ago, this stopped working in Firefox. Instead Firefox started to think that numerical dates were supposed to be formatted as DD/MM/YYYY, which is at least as asinine as the typical American MM-DD-YYYY format. I finally got fed up with this and decided to investigate.

The best discussion of the issue is in [Thunderbird bug 1426907](https://bugzilla.mozilla.org/show_bug.cgi?id=1426907). Here I learned that the problem is caused by Thunderbird (and by extension Firefox) no longer respecting glibc locales. Mozilla software simply takes the name of the system locale, ignores its definition, and looks up formatting in the [Unicode CLDR](https://cldr.unicode.org/). The CLDR has [redefined en_DK](https://www.localeplanet.com/icu/en-DK/index.html) to use DD/MM/YYYY<sup class="footnote-ref" id="fnref:endk"><a rel="footnote" href="#fn:endk" title="see footnote">1</a></sup>.

The hack to address the problem was also documented in the Thunderbird bug report. The CLDR includes [a definition for en_SE](https://www.localeplanet.com/icu/en-SE/index.html) which uses YYYY-MM-DD<sup class="footnote-ref" id="fnref:ense"><a rel="footnote" href="#fn:ense" title="see footnote">2</a></sup> and 24-hour time. (It also separates the time from the date with a comma, which is weird, but Sweden is weird, so I'll allow it.) There is no en_SE locale in glibc. But it can be created by linking to the en_DK locale. This new locale can then be used for `LC_TIME`.

    $ sudo ln -s /usr/share/i18n/locales/en_DK /usr/share/i18n/locales/en_SE
    $ echo 'en_SE.UTF-8 UTF-8' | sudo tee -a /etc/locale.gen
    $ sudo locale-gen
    $ sed -i 's/^LC_TIME=.*/LC_TIME=en_SE.UTF-8/' /etc/locale.conf

Now anything that respects glibc locales will effectively use en_DK, albeit under a different name. Anything that uses CLDR will just see that it is supposed to use a locale named en_SE, which still results in sane formatting. Thus one can use [HTML date input fields](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date) without going crazy.

<div id="footnotes">
    <h2>Notes</h2>
    <ol>
        <li id="fn:endk"><a rev="footnote" href="#fnref:endk" class="footnote-return" title="return to article">&crarr;</a> The Unicode specification defines this pattern as "dd/MM/y", which is rather unintuitive, but worth including here for search engines.</li>
        <li id="fn:ense"><a rev="footnote" href="#fnref:ense" class="footnote-return" title="return to article">&crarr;</a> The Unicode specification defines this pattern as "y-MM-DD".</li>
    </ol>
</div>
