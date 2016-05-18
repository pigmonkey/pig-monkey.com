Title: Cryptographic Identity
Date: 2016-05-17
Tags: crypto, privacy

Despite its shortcomings, I think PGP is still one of the better ways to verify a person's identity. Because of this -- and because I use my PGP key daily<sup class="footnote-ref" id="fnref:key-use"><a rel="footnote" href="#fn:key-use" title="see footnote">1</a></sup> -- I make an effort to properly secure my private key. Verifying a PGP key is a fairly straightforward process for fellow PGP users, and my hope is that anyone who does verify my key can maintain a high confidence in its signature.

However, I also use other cryptographic channels to communicate -- XMPP/OTR and Signal chief among them. I consider these keys more transient than PGP. The OTR keys on my computer are backed up because it takes no effort to do so, but I have no qualms about creating new ones if I feel like it. I don't bother to port the same keys to other devices, like my phone. My Signal key is guaranteed to change anytime I rebuild or replace my phone. Given the nature of these keys and how I handle them, I don't expect others to put the same amount of effort into verifying their fingerprints.

The solution to this is to maintain a simple text file, signed via PGP, containing the fingerprints of my other keys. With a copy of the file and a trusted copy of my public PGP key, anyone can verify my identity on other networks or communication channels. If a key is replaced, I simply add the new fingerprint to the file, sign it and distribute. Contacts download the file, check its signature, and thus easily trust the new fingerprint without additional rigmarole.

The first examples of this that I saw were from [Yan](http://web.mit.edu/zyan/www/zyan.txt) and [Tom Lowenthal](https://tomlowenthal.com/id). I thought it seemed like a great idea and began to maintain a file with a list of examples whenever I stumbled across then, with a note that I should do that someday<sup class="footnote-ref" id="fnref:keybase"><a rel="footnote" href="#fn:keybase" title="see footnote">2</a></sup>.


Today I decided to stop procrastinating on this and create my own identity file. It is located at [pig-monkey.com/id.txt](https://pig-monkey.com/id.txt). The file, along with the rest of this website, is [in git](https://github.com/pigmonkey/pig-monkey.com/blob/master/content/id.txt) so that changes to it may be tracked over time.

Inspired by some of the examples I had collected, I added a couple pieces of related information to the file. The section on PGP key signing should provide others some context for what it means when they see my signature on a different key. Even if no one cares, I found it useful to enunciate the policy simply to clear up my own thinking about what the different certification levels should mean. Finally, the section on key management gives others a rough idea about how I manage my key, which should help them to maintain their confidence in it. If I verify that someone's identity and fingerprint match their key, I will have high confidence in its signature initially. But if I know that the person keeps their secret key on their daily driver machine without any additional effort to protect it, my confidence in it will degrade over time. Less so if I know that they take great care and handling in their key's protection.

A file like this should also provide a good mechanism for creating a transition and revocation statement for my PGP key, should the need arise. One hopes that it does not.


<div id="footnotes">
    <h2>Notes</h2>
    <ol>
        <li id="fn:key-use"><a rev="footnote" href="#fnref:key-use" class="footnote-return" title="return to article">&crarr;</a> Realistically, I use PGP multiple times per hour when I'm on my computer.</li>
        <li id="fn:keybase"><a rev="footnote" href="#fnref:keybase" class="footnote-return" title="return to article">&crarr;</a> Since I began my list, <a href="https://keybase.io/">Keybase</a> has become a thing. It addresses a similar problem, although seems to promote using services like Twitter as the root of trust. Assuming that you want to stubbornly stick with a PGP key as the root of trust, I don't see the advantage of using Keybase for this problem, except that it offers a centralized lookup repository.</li>
    </ol>
</div>
