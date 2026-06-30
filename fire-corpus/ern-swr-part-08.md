# SWR Series Part 8: Technical Appendix — earlyretirementnow.com

### Update: We posted the results from parts 1 through 8 as a Social Science Research Network (SSRN) working paper in pdf format:

### [Safe Withdrawal Rates: A Guide for Early Retirees (SSRN WP#2920322)](http://ssrn.com/abstract=2920322)

[Last week](http://earlyretirementnow.com/2017/01/25/the-ultimate-guide-to-safe-withdrawal-rates-part-7-toolbox/) we published a Google-Sheet that calculates safe withdrawal rates to exactly match a specified real final asset value target. For 1,700+ retirement cohorts (starting between 1871 and 2015)! How do we compute those safe withdrawal rates in practice? I hope we don’t lose half of our subscribers this week but I thought it would be a great idea to show the mathematics behind our calculations. It’s simple arithmetic that we can easily implement in Excel/GoogleSheets and Octave/Matlab. But despite the simplicity, I haven’t seen anyone else use this methodology. Everybody (Trinity Study, cFIREsim, etc.) seems to be using the brute-force simulation technique of iterating portfolio values while applying withdrawals and returns over time. That’s an inefficient approach and we developed a more elegant technique. 

### Safe Withdrawal Rate basics

We start with an initial real portfolio value, for simplicity scaled to one, make monthly withdrawals, potentially pay or receive some supplemental cash flows (i.e., consulting income during early retirement, social security and pensions later in retirement, health care expenditures later in life, etc.) and then receive a certain stream of capital market returns over time. Given a withdrawal rate, we can easily calculate the final net worth, simply by iterating forward the portfolio value until the final month. But that’s not how we want to compute it. Recall, we target a certain final asset value and desire to calculate the withdrawal rate to exactly match that final value, not the other way around!

One way to calculate the withdrawal rate would be to guess the withdrawal rate, iterate forward, see by how much we miss the target final value and then adjust the withdrawal rate until we hit the desired target. That would work well if we had to calculate one single safe withdrawal rate. But remember: we want to calculate several million safe withdrawal rates (all combinations of starting dates, equity weights, final asset values, retirement horizon, and other parameters), so the trial and error method or even a [Newton-Raphson](https://en.wikipedia.org/wiki/Newton's_method) method seem a little bit cumbersome. There is a more elegant method. Much more elegant!

### Deriving SWRs analytically

First, let’s define variable _Ct_ as the total cumulative return of one dollar invested between the beginning of month _t_ and the final period _T_ , which is the end of the retirement horizon, e.g., 720 months in our case, or 360 months in the Trinity Study. Think of this as an opportunity cost factors, the loss of each dollar of a withdrawal in period _t_ measured in period _T_ dollars. If the (real, inflation-adjusted) capital market returns are _r_ , then we can calculate this as:

![swr-part8-formula01](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part8-formula01.png?resize=221%2C78&ssl=1)

So, the _Ct_ are simply the cumulative capital market returns, but moving **backward** rather than forward. Also, note that _C1_ is the cumulative return of the initial principal if held over the entire retirement horizon. In other words,

![swr-part8-formula02](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part8-formula02.png?resize=345%2C195&ssl=1)

We can now calculate the final asset value of a portfolio with an initial value of one and withdrawals _w_ every month as:

![swr-part8-formula03](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part8-formula03.png?resize=225%2C92&ssl=1)

The first term on the right side is how much the portfolio would have grown in the absence of any withdrawals, and the second term is the total opportunity cost of all withdrawals translated into date _T_ dollars. Notice that even the final month’s withdrawal is subjected to a return _rT_ because the withdrawal comes out at the beginning of the month while the final asset value is marked at the end of the final month.

Now we can easily solve for the withdrawal rate w that generates the final value target as

![swr-part8-formula04](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part8-formula04.png?resize=203%2C82&ssl=1)

### Additional Cash Flows (Social Security, Pensions, Expenses, etc.)

We can also easily expand this analysis to include any sequence of additional cash flows independent of the investment portfolio, _p_ , to account for pensions (_p >0_) or even costs in retirement (e.g., kids’ college costs, higher health care costs when old, etc.) that need to be funded over and on top of the baseline withdrawals (_p <0_). Translating those additional flows into date _T_ dollars requires multiplying each by its opportunity cost factor and summing up. Hence,

![swr-part8-formula05](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part8-formula05.png?resize=342%2C84&ssl=1)

And thus,

![swr-part8-formula06](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part8-formula06.png?resize=567%2C75&ssl=1)

Notice how all three terms in the safe withdrawal rate are simply additive. Computationally, this is very easy to handle. For example, for any given retirement start date, horizon, and equity weight, we have to calculate the terms involving _C_ only once and simply read off the sustainable withdrawal rates for different values of FV with very little computational burden.

### Time-varying withdrawal rates

One additional complication we can model is to assume that the withdrawals have a specified scaling/shape over time, i.e.,

![swr-part8-formula08](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part8-formula08.png?resize=237%2C29&ssl=1)

and subsequent scaling factors

![swr-part8-formula09](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part8-formula09.png?resize=128%2C27&ssl=1)

can take any desired shape, e.g., an exponential increase over time (to model COLA=Cost-of-Living Adjustment above the CPI), or an exponential decay (COLA less than CPI), or any other shape over the retirement horizon. For example, constant for the first 30 years (in real terms) and then declining to account for less consumption demand when older. The SWR calculation is still really simple:

![swr-part8-formula07](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part8-formula07.png?resize=561%2C75&ssl=1)

### Why our methodology is more elegant than cFIREsim’s iterative methodology

  * We are interested in the failure probabilities of different withdrawal rates (say, all values from 3% to 5% in 0.25% steps). cFIREsim would have to calculate a whole new set of simulations with time series of portfolios for each alternative withdrawal rate. We compute one single safe withdrawal rate for each retirement cohort and then simply read off the percentage of our SWR values that were above or below a certain target level.
  * cFIREsim has the advantage that it calculates the entire time series of portfolio values. But if you’re only interested in the final portfolio value then it’s very easy to generate that distribution for alternative withdrawal rates without any new simulations. Simply construct the time series of final asset values by plugging in a specific w into one of the “FV=…” formulas above. And again we can do this for different values of w without ever going through the iterative process!



### Update (2/1/2017)

There are obviously others who have already used a similar technique to ours, i.e., computing safe withdrawal rates to hit a specific target:

  * For fixed returns, of course, Excel’s “pmt” function calculates a safe withdrawal rate. That’s because, for fixed returns, our formula simply reduces to the good old mortgage amortization math. For example: “=PMT(0.004,720,-1000000,500000,1)” calculates the safe withdrawal rate using 0.4% monthly returns, 720 months, a $1,000,000 initial portfolio (needs a minus operator!!!), with a $500,000 final target. The final argument is set to “1” to indicate that the withdrawals happen at the **beginning** of the month. Use “0” when the withdrawal happens at the end of the month.
  * Morningstar has a [white paper](https://corporate.morningstar.com/US/documents/ResearchPapers/OptimalWithdrawalStrategyRetirementIncomePortfolios.pdf), thanks to jp6v for pointing that out in the comments section. On page 4 of that document you get a formula similar to ours (though without the final value target FV). And their formula looks more convoluted than it needs to be, but maybe I’m just a math purist.
  * A paper [posted on SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2551370), thanks to jp6v for the reference. Their formula (3) is the same as our base case formula with a final value target. jp6v has a nice summary of that paper [on his own blog](https://medium.com/@justusjp/perfect-withdrawal-amount-and-modifying-the-initial-rate-a13ea4400d94#.bf6zmbxxz).
  * Another blogger, [gummy-stuff](http://www.gummy-stuff.org/sensible_withdrawals.htm) with similar formulas to ours and a spreadsheet with his calculations. Thanks again to jp6v for the link.



But we still have the two innovations that I haven’t seen anywhere else:

  * The supplemental cash flows, as used in [part 4 of the series (Social Security and Pensions)](http://earlyretirementnow.com/2017/01/04/the-ultimate-guide-to-safe-withdrawal-rates-part-4-social-security-pensions/).
  * The option to do different COLA adjustments, as used in [part 5 of the series](http://earlyretirementnow.com/2017/01/11/the-ultimate-guide-to-safe-withdrawal-rates-part-5-cost-of-living-adjustments/).



### Thanks for stopping by today! Please leave your comments and suggestions below! Also, make sure you check out the other parts of the series, see [here for a guide to the different parts so far](https://earlyretirementnow.com/safe-withdrawal-rate-series/)!

### Share this:

  * [ Share on X (Opens in new window) X ](https://earlyretirementnow.com/2017/02/01/the-ultimate-guide-to-safe-withdrawal-rates-part-8-technical-appendix/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://earlyretirementnow.com/2017/02/01/the-ultimate-guide-to-safe-withdrawal-rates-part-8-technical-appendix/?share=facebook)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://earlyretirementnow.com/2017/02/01/the-ultimate-guide-to-safe-withdrawal-rates-part-8-technical-appendix/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://earlyretirementnow.com/2017/02/01/the-ultimate-guide-to-safe-withdrawal-rates-part-8-technical-appendix/?share=reddit)
  * 


### Like this:

Like Loading…

### _Related_
