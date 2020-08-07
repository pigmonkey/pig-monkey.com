Title: Reconciling Ledger
Date: 2020-08-06
Tags: finance, plaintextaccounting

For me, one of the primary appeals of using [Ledger](https://www.ledger-cli.org/) -- or really any accounting system -- is that it let's me know how much money I have (or don't have) *right now*. Other people's records lag behind reality.

If I submit an order for a $50 widget on a website today, I consider that $50 gone, even though the vendor likely didn't collect the money immediately. They probably placed a hold on the funds, but will not actually capture the money until they ship the order, which may take a couple days. When they do capture the funds, it may still be another day or two until that action posts to my online bank statement. Were I dependent on the bank, I could go a week thinking that I have $50 more than I actually have.

It is important to me that I log transactions without waiting for them to appear elsewhere, but at some point I do want to reconcile my records against what my bank believes. I accomplish this with [auxiliary dates](https://www.ledger-cli.org/3.0/doc/ledger3.html#Auxiliary-dates).

Were I to submit that order for a $50 widget today, I would create the entry using today's date. Even if it takes me a few days to actually record the entry, I will still use the date the order was submitted.

    2020-08-06 Acme, Inc
        Expenses:Misc                             $50.00
        Assets:Bank:Checking

Periodically, I will manually reconcile every transaction in my journal against my bank's online statements. Usually this happens every other week or so. Many people will simply dump a CSV from their bank and [use a script to parse and import the results into their journal](https://github.com/ledger/ledger/wiki/CSV-Import). I prefer to do it manually. This rarely takes more than 30 minutes, and for me it is one of the other primary appeals of using Ledger: it forces me to be intimately aware of how money is flowing in my life, and makes it extremely easy to spot problems or errors. It is difficult to accomplish that reliably without manually touching every transaction.

So a week or two later I'll login to the bank and make sure there is a $50 payment to Acme, Inc. If the date listed by the bank for that transaction is different from what I recorded -- which for online transactions is almost always the case -- I'll prepend that date to my entry.

    2020-08-10=2020-08-06 Acme, Inc
        Expenses:Misc                             $50.00
        Assets:Bank:Checking

When there are two dates, Ledger considers the date to the left of the `=` to be the primary date. The other date is the auxiliary date. Previously, when only one date was listed, it was the equivalent to `2020-08-06=2020-08-06`. By using the bank's date as the primary date, I know that the default output from a report like `ledger register assets:bank:checking` will match the bank's statements. If I want to report on what I consider to be the real dates of the transactions, I can pass the `--aux-date` flag.

The journal files themselves I edit manually in vim, with a little help from [vim-ledger](https://github.com/ledger/vim-ledger/). I have `<leader>t` [mapped to set today's date as the primary date of the current transaction](https://github.com/pigmonkey/dotfiles/blob/master/vim/ftplugin/ledger.vim#L20). Because I usually only reconcile two or three times a month, today's date is often not the date I actually want, but this shortcut allows me to immediately insert a new date in the correct format. I can then quickly change the day number to whatever it should actually be.

I consider the transaction to be cleared once the bank statement and the Ledger journal file agree on the date, payee, and dollar amount. In Ledger, transactions are marked as cleared by inserting an `*` between the date and the payee. In vim I [map this to `<leader>c`](https://github.com/pigmonkey/dotfiles/blob/master/vim/ftplugin/ledger.vim#L17). A complete transaction thus looks like this:

    2020-08-10=2020-08-06 * Acme, Inc
        Expenses:Misc                             $50.00
        Assets:Bank:Checking

Ledger defaults to including all transactions in its reporting and calculations. By passing the `--cleared` flag it will only include transactions that have been marked as cleared. So after I think I'm done reconciling all transactions against my bank statement, I will run `ledger balance assets:bank:checking --cleared` and verify that the resulting balance matches what the bank shows. If I want to know how much money I actually have in that account, I will run `ledger balance assets:bank:checking`. The output of this will likely include transactions that the bank hasn't caught on to yet.

If for some reason Ledger's output of the cleared balance does not agree with the bank, my first step will be to make sure that all transactions are sorted by their primary date. If I already have the file open in vim, I have [a shortcut for that](https://github.com/pigmonkey/dotfiles/blob/master/vim/ftplugin/ledger.vim#L28). Otherwise I keep a one-liner script called `ledger-sort` that takes the name of a ledger file as input, sorts it, and shows me the diff.

    #!/bin/sh

    ledger -f $1 print --sort d > $1.sort && mv $1{.sort,} && git diff

Checking the diff of the sorted output before continuing is important. Sometimes I'll make a silly mistake like typing the wrong year when entering the transaction. This sort of mistake is obvious when looking at the diff.

Once the file is sorted, I'll run `ledger register assets:bank:checking --cleared`. The final column in this output is a running total of the account balance. The only difference between the output and my bank statement should be the ordering of transactions within a day, which I do not care about.

I'll know that I last cleared my journal around a certain date, and that the account balance was accurate as of that date.<sup class="footnote-ref" id="fnref:assert"><a rel="footnote" href="#fn:assert" title="see footnote">1</a></sup> If I was doing this on 2020-08-06, I might say to myself "I know I cleared Ledger sometime in mid-July, so let's look at my account balance at end of day on 2020-07-15". If the bank and Ledger both agree on the balance at the end of day on that date (regardless of the ordering of the multiple transactions that may have occurred on the day), I'll know that the error is somewhere between 2020-07-16 and 2020-08-06. Next I'll jump to another random day in that period -- maybe 2020-07-22 -- and perform the same exercise. This is repeated until I find the first day where the two systems disagree on the ending balance. Then I look at every transaction on that day and find the error. Usually it will be a simple data entry error, such as me typing `$12.10` instead of `$12.01`. Having [my receipts stored](/2020/08/receipts-ledger/) allows me to verify that I did indeed agree to pay `$12.10` and that the error is mine rather than the payee's. This whole process of finding errors rarely requires more than two minutes, and occurs maybe once every three months.

Though I don't use CSV exports from my banks for anything, I do like to periodically download and archive them. When I generate the exports I ask for one file per month. I refer to these as "bank dumps" and store them in directory named `dump`. Each file is named for the account and month it represents. For example, an account named `Assets:Bank:Savings` will have last month's dump stored at `dump/assets-bank-savings-202007.csv`. I pretty much never open these files, but I like having them archived. They allow me to see how much money a bank thought I had at any point in time, even if the account is no longer open, and provide assurance that I can always true my records if I somehow mess them up.


<div id="footnotes">
    <h2>Notes</h2>
    <ol>
        <li id="fn:assert"><a rev="footnote" href="#fnref:assert" class="footnote-return" title="return to article">&crarr;</a> Ledger has the ability to <a href="https://www.ledger-cli.org/3.0/doc/ledger3.html#Balance-assertions">record assertions</a>. I have never used this feature, but I probably should.</li>
    </ol>
</div>
