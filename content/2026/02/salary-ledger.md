Title: Salary Tracking with Ledger
Date: 2026-02-10
Tags: finance, plaintextaccounting

In my previous [descriptions of how I perform plain text accounting](/tag/plaintextaccounting/) I did not discuss logging salary income with [Ledger](https://www.ledger-cli.org/). My basic strategy is to create an entry with all the same data that appears on the paystub. The only number that actually matters to me is whatever amount ends up in my bank account, but it is still important to have withholdings documented for later querying.

A simplified entry would look like this:

    2025-12-26 Acme Inc
        Assets:Bank:Checking                    $1000.00
        Expenses:Tax:Federal:FY2025              $200.00
        Expenses:Tax:State:FY2025                 $50.00
        Expenses:Insurance:Medical                $20.00
        Income:Salary

At the time of entry, I store a PDF of the paystub [just like a receipt](/2020/08/receipts-ledger/). (In Ye Olden Days this came from scanning a piece of paper, but now I just download the PDF from a web site.) This entry will be [reconciled](/2020/08/reconciling-ledger/) and get cleared with the `*` mark the next time I login to the bank account and verify the amount I received.

If I want to know how much money the employer or a government thinks I made last year, I can just ask Ledger for the balance of the `Income:Salary` account.

    $ ledger balance income:salary --period 2025
            $-1270.00   Income:Salary

However, this number has no real bearing on my reality. What is much more useful to me is the ability to query how much money I actually received last year, e.g. my take-home pay. I can do this by asking Ledger to show the balance of the bank account, limiting it to postings that involved the `Income:Salary` account.

    $ ledger balance assets:bank:checking -l "any(account =~ /Income:Salary/)" --period 2025
            $1000.00    Assets:Bank:Checking

If the only financial relationship you have with your employer is them giving you money in the form of a salary, then you could simplify this by just asking Ledger for the balance of transactions in the bank account from that payee.

    $ ledger balance assets:bank:checking and "@Acme Inc" --period 2025

However, my employer sells stuff, and sometimes I buy that stuff, so for me the above query would show me my salary less my employee purchases. Which is mostly worthless.

When I receive a W-2 after the end of the year, I check all of its entries -- gross pay, pre- and post-tax deductions, etc -- against Ledger with a simple `ledger balance "@Acme Inc" --period 2025`. Having all this data stored locally in queryable plain text, rather than needing to access some web portal or read through various PDFs like a prehistoric savage, is a key life strategy for me.
