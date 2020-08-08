Title: Adding Metadata to Ledger
Date: 2020-08-07
Tags: finance, plaintextaccounting

As [mentioned previously](/2020/08/reconciling-ledger/), two of the primary reasons I use [Ledger](https://www.ledger-cli.org/) are the intimate awareness it provides of how money is moving, and its timely representation of current balances. The third primary reason I use the tool is for the activity history it provides.

Recording almost every transaction I make (excepting only some [small petty cash](/2020/08/ledger-cash/)) allows me to look at years past and build an accurate picture of what I was doing. Most activities leave some sort of financial record, even if the transaction is only tangential to the activity itself. This is the sort of information that I would be extremely uncomfortable providing to a [third-party](https://www.intuit.com/), but is quite useful to have myself.

[Storing receipts](/2020/08/receipts-ledger/) provides an additional layer of detail to the history created in the Ledger journal. As an intermediate between the full receipt and the basic journal entry, I find it is extremely valuable to use [comments](https://www.ledger-cli.org/3.0/doc/ledger3.html#Commenting-on-your-Journal) and [tags](https://www.ledger-cli.org/3.0/doc/ledger3.html#Metadata-tags) within the journal. Almost every transaction in my Ledger journal that is not for food has a comment describing what goods or service was purchased.

In Ledger, comments begin with a semicolon. I store them below the first line of the transaction. When placed here, Ledger refers to these comments as [notes](https://www.ledger-cli.org/3.0/doc/ledger3.html#Transaction-notes). When purchasing goods, I add one comment -- or note -- for each unique item on the transaction. For instance, I might buy socks:

    2018-07-02=2018-07-01 * Socks Addict
        ; Darn Tough Light Cushion No Show Tab, Black/Grey, Large, 2x
        Expenses:Clothing:Footwear                $33.40
        Liabilities:Bank:Visa

The comment tells me exactly what was purchased. More importantly, it tells me the model name, the color, and the size of the item. If I want to purchase another pair of identical socks, I can do so easily. This seems like a minor thing, but when it is applied to everything I buy, it is hard to overstate how greatly this ability has improved my quality of life over the past decade.

In Ledger, comments are searchable. Say I want to list every transaction where I purchased a pair of Darn Tough socks. I buy them from different retailers, so I can't filter by the payee. All the transactions are in the `Expenses:Clothing:Footwear` category, but that category includes socks from other manufacturers and well as other things that go on my feet, so I can't filter by that. But I can query all transactions with a note which includes the string "darn tough".

    $ ledger register note darn tough

A tag is a special kind of comment. Tags are useful if you have the foresight to realize that a particular transaction should be grouped with other transactions, but that transactions within the group will likely have different payees or accounts. Tags start and end with a `:`. Multiple tags can be chained together.

I use tags for vacations. Expenses related to any vacation are tagged with two tags: a generic `:vacation:` tag, and a tag specific to the vacation. This allows me to easily see what I spend on vacations in general, or any one vacation specifically. For example, in 2018 I took a 24-hour trip to Las Vegas [to see Nine Inch Nails](/2018/12/reflecting-chrome/). That trip included numerous transactions in unrelated accounts: concert tickets, airline tickets, accommodations, ground transport, food, etc. All transactions were tagged with `:vacation:` and `:nin-vegas-2018:`. As an example, here is the transaction for purchasing the concert tickets:

    2018-03-30=2018-03-28 * AXS
        ; Nine Inch Nails at The Joint, Las Vegas
        ; :nin-vegas-2018:vacation:
        Expenses:Entertainment:Performance        $95.50
        Assets:Bank:Checking

Ledger makes it easy to see all the expenses associated with that trip, both in total and broken out into different expense accounts.

    $ ledger balance expense and %nin-vegas-2018

I also use tags to indicate transactions that occur via the same merchant system but have different payees. Specifically, things I buy on Etsy are tagged `:esty:` and things I buy on eBay are tagged `:ebay:`. Without these tags I would have no way to list all the Etsy purchases I have made, since I send the money to individual sellers and not Etsy itself.

I also use tags to indicate transactions related to keeping my apartment. Rent goes to the `Expenses:Rent` account. Electricity charges go to `Expenses:Utilities:Electric`. Gas charges go to `Expenses:Utilities:Gas`. My cell phone payment goes to `Expenses:Utilities:Phone`. The first three charges I consider apartment expenses. My cell phone is not. By tagging the first three with `:apt:` I can easily see the total monthly cost of keeping my apartment, without a bunch of complicated querying to exclude things like the cell phone bill.

My final use for tags is indicating transactions that I think should be deducted from my taxes. Some people do this with accounts, but I find that with the account structure that makes sense to me I often end up with a mix of deductible and non-deductible transactions within a single account. Tagging deductible transactions with `:deduct:` makes it easy to dump a list of all transactions that should be considered when completing yearly taxes.
