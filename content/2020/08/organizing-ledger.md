Title: Organizing Ledger
Date: 2020-08-03
Tags: toolchain, annex, finance, plaintextaccounting

[Ledger](https://www.ledger-cli.org/) is a [double-entry accounting system](https://en.wikipedia.org/wiki/Double-entry_bookkeeping) that stores data in plain text. I began using it in 2012. Almost every dollar that has passed through my world since then is tracked by Ledger.<sup class="footnote-ref" id="fnref:cash"><a rel="footnote" href="#fn:cash" title="see footnote">1</a></sup>

Ledger is not the only [plain text accounting system](https://plaintextaccounting.org/) out there. It has inspired others, such as [hledger](https://hledger.org/) and [beancount](http://furius.ca/beancount/). I began with Ledger for lack of a compelling argument in favor of the alternatives. After close to a decade of use, my only regret is that I didn't start using earlier.

My Ledger repository is stored at `~/library/ledger`. This repository contains a `data` directory, which includes yearly Ledger journal files such as `data/2019.ldg` and `data/2020.ldg`. Ledger files don't necessarily need to be split at all, but I like having one file per year. In January, after I clear the last transaction from the previous year, I know the year is locked and the file never gets touched again (unless I go back in to rejigger my account structure).

The root of the directory has a `.ledger` file which includes all of these data files, plus a special journal file with periodic transactions that I sometimes use for budgeting. My `~/.ledgerrc` file tells Ledger to use the `.ledger` file as the primary journal, which has the effect of including all the yearly files.

    $ cat ~/.ledgerrc
    --file ~/library/ledger/.ledger
    --date-format=%Y-%m-%d

    $ cat ~/library/ledger/.ledger
    include data/periodic.ldg
    include data/2012.ldg
    include data/2013.ldg
    include data/2014.ldg
    include data/2015.ldg
    include data/2016.ldg
    include data/2017.ldg
    include data/2018.ldg
    include data/2019.ldg
    include data/2020.ldg

Ledger's include format does support globbing (ie `include data/*.ldg`) but the ordering of the transactions can get weird, so I prefer to be explicit.

The repository also contains receipts in the `receipts` directory, invoices in the `invoices` directory, scans of checks (remember those?) in the `checks` directory, and CSV dumps from banks in the `dump` directory.

    $ tree -d ~/library/ledger
    /home/pigmonkey/library/ledger
    ├── checks
    ├── data
    ├── dump
    ├── invoices
    └── receipts

    5 directories

The repository is managed using a mix of vanilla git and [git-annex](https://git-annex.branchable.com/).<sup class="footnote-ref" id="fnref:annex"><a rel="footnote" href="#fn:annex" title="see footnote">2</a></sup> It is important to me that the Ledger journal files in the `data` directory are stored directly in git. I want the ability to diff changes before committing them, and to be able to pull the history of those files. Every other file I want stored in git-annex. I don't care about the history of files like PDF receipts. They never change. In fact, I want to make them read-only so I can't accidentally change them. I want encrypted versions of them distributed to my numerous [special remotes](/2016/08/rclone/) for safekeeping, and someday I may even want to drop old receipts or invoices from my local store so that they don't take up disk space until I actually need to read them. That sounds like asking a lot, but git-annex magically solves all the problems with its [`largefiles` configuration option](https://git-annex.branchable.com/tips/largefiles/).

    $ cat ~/library/ledger.gitattributes
    *.ldg annex.largefiles=nothing

This tells git-annex that any file ending with `*.ldg` should not be treated as a "large file", which means it should be added directly to git. Any other file should be added to git-annex and [locked](https://git-annex.branchable.com/git-annex-lock/), making it read-only. Having this configured means that I can just blindly `git annex add .` or `git add .` within the repository and git-annex will always do the right thing.

I don't run the [git-annex assistant](https://git-annex.branchable.com/assistant/) in this repository because I don't want any automatic commits. Like a traditional git repository, I only commit changes to Ledger's journal files after reviewing the diffs, and I want those commits to have meaningful messages.


<div id="footnotes">
    <h2>Notes</h2>
    <ol>
        <li id="fn:cash"><a rev="footnote" href="#fnref:cash" class="footnote-return" title="return to article">&crarr;</a> I do not always track miscellaneous cash transactions less than $20. If a thing costs more than that, it is worth tracking, regardless of what it is or how it was purchased. If it costs less than that, and it isn't part of a meaningful expense account, I'll probably let laziness win out. If I buy a $8 sandwich for lunch with cash, it'll get logged, because I care about tracking dining expenses. If I buy a $1 pencil erasure, I probably won't log it, because it isn't part of an account worth considering.</li>
        <li id="fn:annex"><a rev="footnote" href="#fnref:annex" class="footnote-return" title="return to article">&crarr;</a> I bet you <a href="/tag/annex/">saw that coming</a>.</li>
    </ol>
</div>
