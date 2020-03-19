Title: Bleach has a shelf life of 6 to 12 months.
Date: 2020-03-18
tags: micro, ablution, medical

After one year [the sodium hypochlorite will have broken down into salt and water](https://www.clorox.com/how-to/laundry-basics/product-usage-guides/shelf-life/), which will not be helpful in your battle against the Black Death. According to the [University of Nebraska's guidelines on chemical disinfectants for biohazardous materials](https://ehs.unl.edu/sop/s-bio-disinfectants.pdf), "bleach loses 20-50% of its sodium hypochlorite concentration after 6 months".

Bottles of Clorox bleach are stamped with a date code which [when properly decoded](https://www.clorox.com/how-to/laundry-basics/bleach-101/clorox-regular-bleach-should-be-replaced-every-year-and-stored-as-directed-for-optimum-performance/) will indicate the date of manufacture. The first 7 characters in the label on one of my bottles are `A819275`, indicating that it was manufactured in plant A8 on the 275th day of 2019, or October 2nd. The [previously mentioned dateutils](https://pig-monkey.com/2019/07/dateutils/) proves its usefulness here.

    $ datediff 2019-275 now
    169
    $ datediff 2019-275 now -f "%m months, %d days"
    5 months, 17 days
