Title: Terminal Calculations
Date: 2019-12-12
Tags: toolchain, linux, shell

[Qalculate!](https://qalculate.github.io/) is a well known GTK-based GUI calculator. For years I ignored it because I failed to realize that it included a terminal interface, `qalc`. Since learning about `qalc` last year it has become my go-to calculator. It supports [all the same features](https://qalculate.github.io/features.html) as the GUI, including [RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation) and unit conversions. I [primarily use GNU Units for unit wrangling](/2019/07/gnu-units/), but being able to perform unit conversions within my calculator is sometimes useful.

    $ qalc
    > 1EUR to USD
    It has been 20 day(s) since the exchange rates last were updated
    Do you wish to update the exchange rates now? y

      1 * euro = approx. $1.1137000

    > 32oC to oF

      32 * celsius = 89.6 oF

[The RPN mode](https://qalculate.github.io/manual/qalculate-mode.html#qalculate-rpn) is not quite as intuitive as a purpose built RPN calculator like [Orpie](https://github.com/pelzlpj/orpie), but it is adequate for my uses. My most frequent use of RPN mode is totaling a long list of numbers without bothering with all those tedious `+` symbols.

    > rpn on
    > stack
    The RPN stack is empty
    > 85

      85 = 85

    > 42

      42 = 42

    > 198

      198 = 198

    > 5

      5 = 5

    > 659

      659 = 659

    > stack

      1:    659
      2:    5
      3:    198
      4:    42
      5:    85

    > total

      total([659, 5, 198, 42, 85]) = 989

    > stack

      1:    989

Also provided are some basic [statistics functions](https://qalculate.github.io/manual/qalculate-definitions-functions.html#qalculate-definitions-functions-1-Statistics) that can help save time.

    > mean(2,12,5,3,1)
      mean([2, 12, 5, 3, 1]) = 4.6

And of course there are [the varaibles and constants you would expect](https://qalculate.github.io/manual/qalculate-definitions-variables.html)

    > 12+3*8)/2
      (12 + (3 * 8)) / 2 = 18
    > ans*pi
      ans * pi = 56.548668

I reach for `qalc` more frequently than alternative calculators like [bc](https://www.gnu.org/software/bc/), [insect](https://github.com/sharkdp/insect), or the Python shell.
