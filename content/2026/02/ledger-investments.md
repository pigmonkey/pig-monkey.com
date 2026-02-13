Title: Tracking Investments with Ledger
Date: 2026-02-12
Tags: finance, plaintextaccounting

I have a few investment accounts I track with [Ledger](https://www.ledger-cli.org/). Ledger has [ways of tracking commodities](https://ledger-cli.org/doc/ledger3.html#Currency-and-Commodities) that are too complex for me. My investments are index funds of different flavors. I neither know nor care to know what individual components they consist of. They mostly manage themselves. I do want to know their balance, but I do not care to think about them more than a few times per year, so the up-to-date-ness factor can be pretty low (which is the complete opposite of everything else that I track in Ledger).

I represent these things in Ledger using an asset account for the fund, with subaccounts for contributions, earnings, and fees.

Contributions into the accounts are entered as soon as they happen, since those contributions are being debited out of an account where the up-to-date-ness factor is critical. So a transfer from my bank account to my Roth IRA may look like this:

    2025-02-01 Investment Company
        Assets:Invest:RothIRA:Contributions     $1000.00
        Assets:Bank:Checking

Earnings and fees are tracked, but I only make those entries about once per quarter. However, the investment companies provide monthly statements. That level of granularity can be useful to have stored. So when I perform my quarterly updates, I'll download each of the monthly statements from the past quarter and use them to make three sets of entries -- two per month for the three months in the quarter. For example, in January 2026 I might make entries for the 2025 Q4 activity such as:

    2025-10-31 * Investment Company
        Assets:Invest:RothIRA:Earnings            $79.05
        Income:Invest:Earnings

    2025-10-31 * Investment Company
        Expenses:Fees:Invest                       $1.05
        Assets:Invest:RothIRA:Fees

    2025-11-30 * Investment Company
        Assets:Invest:RothIRA:Earnings           $103.25
        Income:Invest:Earnings

    2025-11-30 * Investment Company
        Expenses:Fees:Invest                       $2.20
        Assets:Invest:RothIRA:Fees

    2025-12-31 * Investment Company
        Assets:Invest:RothIRA:Earnings           $-13.82
        Income:Invest:Earnings

    2025-12-31 * Investment Company
        Expenses:Fees:Invest                       $1.31
        Assets:Invest:RothIRA:Fees

Before making the first entry, I will ask Ledger for the balance of `Assets:Invest:RothIRA` as of 2025-10-01 and confirm that the value matches the October statement's opening balance. I will then read the total earnings and fees from the October statement and make the two October entries in my journal. Then I ask Ledger for the balance of the account as of 2025-10-31 and make sure the reported value matches the statement's closing balance. Rinse and repeat for the next two months. I can ignore any contributions mentioned on the statement because those entries were already entered in my journal whenever I made the contribution.

These transactions are marked as cleared with the `*` symbol as I write the entry because the data comes direct from the statement of past activity. There is no separate [reconciliation process](/2020/08/reconciling-ledger/).

The PDF statements themselves then get stored, but (unlike [receipts, invoices, and checks](/2020/08/receipts-ledger/)) that happens in a different repository.

Doing things this way allows me to query for the value of the accounts (as of the last quarter or so), have some idea of how they are performing, and keep track of fees. I don't really care to know any more details than this, nor do I care to think about these accounts with any more frequency than this.
