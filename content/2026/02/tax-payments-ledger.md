Title: Tax Payments with Ledger
Date: 2026-02-11
Tags: finance, plaintextaccounting

How I record taxes in [Ledger](https://www.ledger-cli.org/) is pretty simple. In my demonstration of [how I record salary payments](/2026/02/salary-ledger/) the example entry included tax deductions that show the basic account structure.

    2025-12-26 Acme Inc
        Assets:Bank:Checking                    $1000.00
        Expenses:Tax:Federal:FY2025              $200.00
        Expenses:Tax:State:FY2025                 $50.00
        Expenses:Insurance:Medical                $20.00
        Income:Salary

I pay state and federal taxes, so I have two main accounts: `Expenses:Tax:Federal` and `Expenses:Tax:State`.

Tax payments (and refunds for overpayments) can occur in years other than the tax years that the payments are related to. This requires some way to query transactions by tax years rather than just the posting date. You could do this by tagging the transactions, but I prefer to use a fourth account level to indicate the fiscal year. Thus my 2025 taxes live in `Expenses:Tax:Federal:FY2025` and `Expenses:Tax:State:FY2025`.

If I pay an accountant to help me file taxes, I will log the payment against the `Expenses:Tax:Preparation` account, which uses the same fiscal year subaccount.

    2026-02-01 The Accountant
        Expenses:Tax:Preparation:FY2025          $100.00
        Assets:Bank:Checking

If I receive a federal refund in March, I will debit it out of the appropriate tax account. I also tag these transactions with `refund-tax` so I can easily query them later.

    2026-03-15 IRS
        ; 2025 Tax Refund
        ; :refund-tax:
        Assets:Bank:Checking                    $1000.00
        Expenses:Tax:Federal:FY2025

If instead I discover that I still owe federal taxes in March, I will credit the payment into the appropriate tax account. I tag these transactions with `final-tax` so I can easily query them later.

    2026-03-15 IRS
        ; 2025 Federal Taxes
        ; :final-tax:
        Expenses:Tax:Federal:FY2025             $1000.00
        Assets:Bank:Checking

Some years I have made quarterly estimated tax payments instead of having taxes withheld from my paycheck. These entries look as you would expect, but I tag them with `estimated-tax` as well as the quarter number for future queries.

    2025-09-02 IRS
        ; 2025 Q3 Estimated Tax
        ; :estimated-tax:q3:
        Expenses:Tax:Federal:FY2025             $1000.00
        Assets:Bank:Checking


The bottom line with all of this is that I can do a simple `ledger balance fy2025` and see a complete and easy to understand picture of my 2025 taxes. Or I can run `ledger balance expenses:tax:federal` to see what I've paid in federal taxes over the past 14 years, broken out by year.

As with most things related to Ledger, this seems like pretty basic stuff when you're doing it but becomes a superpower when you realize how most of the rest of the world lives.
