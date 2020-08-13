Title: Tracking My Phone Bill with Ledger
Date: 2020-08-12
Tags: finance, plaintextaccounting, telephone

Back in 2013 I bought my first smartphone and signed up for a T-Mobile prepaid plan, referred to at the time as the ["Walmart Plan"](https://blog.bn.ee/posts/ice-cream-sandwich-for-30month). The plan cost $30 per month, was intended for new customers only, and was supposed to only be available to those who purchased the SIM card at a Walmart. It offered a small amount of voice minutes and a large amount of data, which struck me as what one would want with one of these newfangled computer-phones. I bought a SIM card, figured out how to get T-Mobile to sign me up on the plan despite not stepping foot into a Walmart, and haven't looked back since.

One of the things that appeals to me about the setup is the level of separation it gives me from the service provider. I purchased the phone from the manufacturer and the SIM card I bought with cash. I fund the plan by purchasing refill cards from third-party vendors. I have never provided T-Mobile with any financial information. They have no ability to take any money from me, except what I give them when trading in the refill cards. Obviously, the primary business of any mobile communications provider is location tracking, so I can't refer to my relationship with them as "privacy preserving", but I like to think it does allow me to retain some level of agency that is lost in a more traditional relationship.

If there is a downside to this setup, it is that it can be difficult to understand what I actually pay per month. The plan costs $30. There is some limit to the number of SMS messages, but I have no idea what it is. Data is "unlimited", which means throttled over 4GB, but I don't think I've ever approached even half that limit. Minutes are limited, and if I go over the allotment I'm charged a higher rate, but the service continues as long as the balance of the account remains positive.

I always want to keep more than $30 in the account, in case I do go over the allotted minutes. So I buy $50 refill cards. They have $50 of value, and are supposed to cost me $50. But the vendor I tend to by them from charges a $1 service fee, offers a points program that sometimes results in a discount being applied, and frequently has sales that offer a couple dollars off. So I end up paying something like $48-51. If I do exceed the limits of the plan, I may end up buying a $50 card one month and the next. More often, I buy a $50 card one month and have enough left over in the account that I do not need to refill it the following month. My plan renews on the 5th of the month, so some months I may end up spending $100 by buying one refill card on the first day of the month and another on the last in anticipation of the following month's renewal.

All of that is to say that it is difficult to have an intuitive feel for what my average monthly phone expense is, but it's important that I can get that number so that I can determine if the plan is still working or if I should look for a better offer. Fortunately, this is a thing that [Ledger](https://www.ledger-cli.org/) makes extremely simple.

Whenever I purchase a refill card, I log the transaction in the `Expenses:Utilities:Phone` account. With that done, I can ask Ledger to report on all transactions in that account, grouped by month, with a running average in the final column.

    $ ledger register utilities:phone --monthly --average --begin 2019-08
    2019-09-01 - 2019-09-30     Expenses:Utilities:Phone    $48.50      $48.50
    2019-10-01 - 2019-10-31     <None>                      0           $24.25
    2019-11-01 - 2019-11-30     Expenses:Utilities:Phone    $46.50      $31.67
    2019-12-01 - 2019-12-31     <None>                      0           $23.75
    2020-01-01 - 2020-01-31     Expenses:Utilities:Phone    $51.00      $29.20
    2020-02-01 - 2020-02-29     <None>                      0           $24.33
    2020-03-01 - 2020-03-31     Expenses:Utilities:Phone    $48.50      $27.79
    2020-04-01 - 2020-04-30     <None>                      0           $24.31
    2020-05-01 - 2020-05-31     Expenses:Utilities:Phone    $48.50      $27.00
    2020-06-01 - 2020-06-30     Expenses:Utilities:Phone    $46.50      $28.95
    2020-07-01 - 2020-07-31     <None>                      0           $26.32
    2020-08-01 - 2020-08-31     Expenses:Utilities:Phone    $51.00      $28.38

Over the past 12 months, I have spent an average of $28.38 per month on phone service. I'm ok with that.
