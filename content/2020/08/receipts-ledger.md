Title: Receipts and Ledger
Date: 2020-08-05
Tags: finance, plaintextaccounting

As [previously mentioned](/2020/08/organizing-ledger/), I store receipts in the same repository as my [Ledger](https://www.ledger-cli.org/) data files.

Purchasing something online automatically generates a receipt; it's just a simple matter of saving the confirmation web page or email as a PDF and moving it into the proper directory with the proper filename. That's a low enough bar that I cannot justify not storing them. I have a receipt for every digital transaction I have made since I began using Ledger in 2012.

I'm less strict about storing receipts for transactions that occur in meatspace. These transactions usually result in a paper receipt (which may not be initially even be offered), which then requires scanning or photographing. That is just enough effort that I don't always want to do it. I'll store the receipt for a meatspace transaction if the amount is greater than $100, or if I think it might be tax deductible, or if I think I might make a warranty claim. But if the transaction is a $10 sandwich for lunch, I probably won't bother storing the receipt.

My naming scheme for the receipt files consists of the date of the transaction, the amount, and the payee. This is enough information to go from a Ledger journal entry to a receipt, or from a receipt to a Ledger journal entry. For example, consider a transaction with a journal entry like this:

    2020-07-14 Acme Widgets
        Expenses:Bicycle:Parts                    $23.72
        Assets:PayPal

The receipt for that transaction will be at `receipts/20200714_23.72-acme_widgets.pdf`.

When I first began using Ledger and came up with this file naming scheme, I figured I would write some sort of script that would parse the components of a journal entry and generate the expected receipt filename so that I could quickly jump from one to the other. What I found is that the scheme is simple enough to make such a script unnecessary. When I look at a journal entry I intuitively know what the receipt filename is, and when I look at a receipt filename I intuitively know what the journal entry is. Writing a simple script to generate one from the other would take more energy than I have collectively spent over the past eight years solving the problem manually. So I never wrote it.

I also store invoices in the same repository, in a directory creatively named `invoices`. These are invoices that vendors send me -- primarily things like rent statements and utility bills -- not invoices that I send to people. The naming scheme is the same as what I use for receipts, except in this case the date in the filename is the date the vendor included on the invoice rather than the date I received it or paid it. I chose this because if I ever need to dispute a charge or a payment, this date is an easy way for both the vendor and I to quickly verify that we are discussing the same thing. Each invoice will of course have an associated receipt in the `receipts` directory after I pay it, and the date on this file will be the date on which I submitted the payment.

Every now and then I need to write someone an old-fashioned paper check. These get scanned and stored in a `checks` directory. The file naming scheme for these is similar to that of receipts, except that in addition to the date, amount and payee, I also include the check number. Ledger supports [including the check number in the journal entry](https://www.ledger-cli.org/3.0/doc/ledger3.html#Codes), so including it in the filename provides another way to link the two things. For example, back in 2015 I renewed my passport book and bought a passport card:

    2015-11-09=2015-10-31 * (#1047) US Department of State
        ; Passport Book Renewal
        ; Passport Card Purchase
        Expenses:Travel:Documentation            $140.00
        Assets:Bank:Checking

The scan of the check from that transaction lives at `checks/20151031_140.00-1047-us_department_of_state.pdf`.
