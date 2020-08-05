Title: Tracking Cash with Ledger
Date: 2020-08-04
Tags: finance, plaintextaccounting

In a double-entry accounting system like [Ledger](https://www.ledger-cli.org/), money always moves from one account to another. Money cannot be magicked in or out of existence.

Previously [I mentioned that I sometimes do not track cash transactions](/2020/08/organizing-ledger/#fn:cash). If the transaction is less than $20 and is not related to a category of expense I care about, I may not bother with it. At first glance, this may seem like it conflicts with the inability to magically disappear money. If I take cash out of my checking account, I have to represent that withdrawal or else the balance of the account will be screwy and I'll never be able to reconcile it against the bank's statement. Transforming money from electrons in a bank account to Federal Reserve Notes in my pocket has no impact on its value, so one's initial thought may to represent the cash as an asset account.

    2020-07-13 ATM
        Assets:Cash                               $40.00
        Assets:Bank:Checking

This would be technically correct, and the best way to do things if every last penny of that cash was going to be tracked. But logging the withdrawal that way will not work if, over some period of time, I spend the $40 cash in a serious of small, untracked transactions. In that case, my `Assets:Cash` account would show that I have $40 more than reality. When asset accounts are not accurate, the world ends.

The solution is to [treat cash as an expense account](https://www.ledger-cli.org/3.0/doc/ledger3.html#Dealing-with-Petty-Cash). The balance of an expense account is less important. It tells you how much money you've spent on that category of thing, but it doesn't represent money that you hold. Effectively, this is saying that the $40 was spent when it was withdrawn at the ATM. It no longer contributes to assets or net worth.

    2020-07-13 ATM
        Expenses:Cash                             $40.00
        Assets:Bank:Checking

The transaction would look similar if I asked for cash back while buying groceries.

    2020-03-20 Lucky Dragon Markets
        Expenses:Food:Groceries                   $58.89
        Expenses:Cash                             $40.00
        Assets:Bank:Checking

But the trick is that money doesn't have to move between an expense account and an asset account. Money can move between any accounts, including two expense accounts. I am strict about tracking food related expenses, so if I buy a burrito with that cash, I'll want to log it. I can do that like this:

    2020-07-18 A Taqueria
        Expenses:Food:Dining:Lunch                 $8.23
        Expenses:Cash

If part of your savings are in cash -- in a safe deposit box, stuffed in your mattress, buried in the hills, whatever -- you would want to treat it as an asset so that you can track the balance.

    2020-08-30 ATM
        Assets:Mattress                          $100.00
        Assets:Bank:Checking

To illustrate the degree to which I do track cash: Ledger currently reports the balance of `Expenses:Cash` to be $3797.29. I've certainly dealt with significantly more cash than that since 2012. The balance of that account is simply the amount of cash I have acquired but failed to log as spent.
