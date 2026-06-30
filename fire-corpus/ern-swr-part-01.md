# SWR Series Part 1: Introduction — earlyretirementnow.com

Welcome! You probably landed on this page because you clicked someone’s link to my **Safe Withdrawal Rate Series**. Thanks for stopping by! This series has now grown to 30+ parts and if you are looking for a **less technical** summary before jumping into the nitty-gritty details, I recommend you check out the new “landing page” to my series first:

**[The Safe Withdrawal Rate Series – A Guide for First-Time Readers](https://earlyretirementnow.com/safe-withdrawal-rate-series/)**

But if you got an appetite for the technical details after that I suggest you check out all the other parts as well! Also, I posted the results from parts 1 through 8 as a Social Science Research Network (SSRN) working paper in pdf format:

[**Safe Withdrawal Rates: A Guide for Early Retirees (SSRN WP#2920322)**](http://ssrn.com/abstract=2920322)

**But without further ado, here’s Part 1 of the Series:**

We just calculated over 6.5 million safe withdrawal rates. Well, not by hand, of course, but by writing a computer program that loops over all possible combinations of retirement dates, and other model parameters. Not a big surprise here, but it took a lot of work to put this together. We can’t possibly fit all results into one single post, so we publish our results in multiple parts. Today, we briefly introduce our research and some baseline results. Stay tuned for more to come in the next few weeks/months:

The plan to work on this research came after one of those moments when we realized that if you want something done right and exactly applicable to our own situation, we just have to do it ourselves. We wanted to do a lot more robustness analysis than we had seen anywhere in the blogging world.

### Nonconformist among the nonconformists

Intriguingly, very few early retirement planners or bloggers question the validity of the 4% safe withdrawal rate rule. When you retire in your 30s or even 40s you are by nature nonconformist. You question the consensus, the people with the McMansions and the full-size SUVs in the driveway. People who are otherwise extremely suspicious about everything consensus suddenly eat up the 4% rule without much questioning or checking under the hood:

  * People take the [Trinity Study](https://www.aaii.com/files/pdf/6794_retirement-savings-choosing-a-withdrawal-rate-that-is-sustainable.pdf) at face value and extrapolate the 30-year windows from Trinity to 50+ years for the early retirement crowd (bad, bad, bad idea, see [Part 2 of our series](http://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/)!!!),
  * It’s probably not a good idea to use a withdrawal rate calibrated to the average retiree since 1926 when today’s equity valuation is much less attractive than the average since 1926, see [Part 3 of this series](http://earlyretirementnow.com/2016/12/21/the-ultimate-guide-to-safe-withdrawal-rates-part-3-equity-valuation/).
  * Social Security will also save your behind come age 67 (uuhhhm, good luck with that, see [Part 4 of this series](http://earlyretirementnow.com/2017/01/04/the-ultimate-guide-to-safe-withdrawal-rates-part-4-social-security-pensions/)!).
  * Folks wave their hands about how one can just slow consumption growth (it’s not that easy, see [Part 5 of this series!](http://earlyretirementnow.com/2017/01/11/the-ultimate-guide-to-safe-withdrawal-rates-part-5-cost-of-living-adjustments/)),
  * and wave their hands about how the 4% rule did just fine in 2001 and 2008 (believe me, it didn’t; see [Part 6 of this series!](http://earlyretirementnow.com/2017/01/18/the-ultimate-guide-to-safe-withdrawal-rates-part-6-a-2000-2016-case-study/))



Has anybody actually done some _serious_ simulations that are truly applicable to the FIRE community? Something comparable to the original [Trinity Study](https://www.onefpa.org/journal/Pages/Portfolio%20Success%20Rates%20Where%20to%20Draw%20the%20Line.aspx), but with more bells-and-whistles and robustness checks applicable to the FIRE community? I don’t like the “hand-me-down” research targeted at my parents’ retirement. So, when you want something done, and done right, you gotta do it yourself! Which is what we did with the 6.5 million safe withdrawal rates.

### What we do to be more relevant for early retirees

  1. The study is done at a monthly frequency (not just annual like cFIREsim), starting with equity and bond returns in January 1871 and going through September 2016. It would be unrealistic for us to withdraw funds only once per year at the beginning of the year and have – on average – 6 months of cash sitting around in our checking account.
  2. We look at the sustainable withdrawal rates over 30, 40, 50, and 60-year windows. It’s still a good idea to keep the 30-year window for comparison, though this window length is simply too short for us in the early retirement community.
  3. We look at different target final values, i.e., calibrate maximum withdrawal rates to deplete the capital (final value=0), preserve the inflation-adjusted initial capital (final value=100% of initial value) and some steps in between (final value=25%, 50%, 75% of inflation-adjusted initial value). This is useful for retirees who are uncomfortable with the idea of running out of money at some future date and/or plan to leave a bequest to their children, grandchildren, and charitable organizations.
  4. We extrapolate past the current history and append equity and bond returns after September 2016. To this end, we assume long-term average returns for equities going forward (about 6.6% real p.a.). For bonds, we assume a low real return over the first 10 years: only 0% real p.a., which is actually slightly above the 9/30/2016 10Y yield (1.61%) minus the inflation expectation at the time (~2%). After the initial 10 years, bonds too will return their long-term average of 2.6% real per year. We should note that these return assumptions are likely going to generate higher sustainable withdrawal rates due to the absence of return volatility.
  5. We study how different the safe withdrawal rates and success probabilities were in various equity valuation regimes. Specifically, how do safe withdrawal rates and success probabilities look like for different [Shiller CAPE](http://www.econ.yale.edu/~shiller/data.htm) ratio regimes? We did a [similar study before](http://earlyretirementnow.com/2016/03/24/the-4-is-not-as-good-as-i-hoped/) using [cFIREsim.com](http://cFIREsim.com), but now we can rely on our own monthly simulations and easily loop over all sorts of other model parameter values.
  6. We can study the impact of reducing the monthly withdrawals over time. This mimics the assumption that some people consume less as they age. Or we can take into account the impact of lower withdrawals once retirees start collecting Social Security.
  7. We study how alternative withdrawal strategies, e.g., dynamic withdrawal rules rates based on equity valuation (Shiller CAPE) would have performed during this time.



### Methodology in detail

We use monthly total return data (including dividends/interest) for the S&P500 and 10-year Treasury Bonds from January 1871 to September 2016. We realize that some other researchers use slightly higher yielding corporate bonds. Notice, though, that this higher yield comes at the price of higher correlation with equities and thus less diversification. Our analysis yielded that the exposure in the LQD ETF (iShares investment-grade corporate bonds) has roughly the exposure of 75% government bonds (IEF = 7-10-year US Treasuries) and 25% US equities (VTI = Vanguard US Total Equity Market ETF). So, a 60% equities 40% corporate bond portfolio has about the same return characteristics as a 70% equities, 30% government bond portfolio if you like to translate our portfolio weights into a Stock vs. Corporate Bond portfolio. The Barclays Agg (iShares ticker AGG) is somewhere in between.  
Monthly returns and monthly CPI inflation are translated into monthly real returns. We assume that the retiree has withdrawn an initial amount equal to one-twelfth of the targeted withdrawal rate at the market closing price of the previous month. The remainder of the portfolio grows at the real market return during the current month. At the end of the month the retiree withdrawals the next monthly installment and rebalances the portfolio weights to the target equity and bond shares. We assume that the portfolio is subject to a 0.05% drag from fees for low-cost mutual funds.

### Why 6.5 Million Safe Withdrawal rates?

We calculate safe withdrawal rates for **all possible combinations** of 1) starting dates, 2) retirement horizons, 3) equity weights, 4) final asset values and 5) withdrawal patterns:

  * 1739 possible retirement start dates between February 1, 1871, and December 1, 2016.
  * 4 different retirement horizons: 30, 40, 50, and 60 years
  * 21 different equity weights from 0% to 100% in 5% steps (bond weight = 100%-equity weight)
  * 5 different final asset value targets: 0%, 25%, 50%, 75% and 100% of real inflation adjusted initial asset value
  * 9 different withdrawal patterns. The baseline assumes that withdrawals are adjusted in line with CPI inflation, but we also allow for slower than CPI-growth. We also check how lower withdrawal rates 20 or 30 years after the retirement start date (to account for Social Security income) will impact the maximum sustainable withdrawal rates.



Hence, we calculate 1739 x 4 x 21 x 5 x 9 = 6,573,420 different safe withdrawal rates.

### Base Case Results

Here’s a table, roughly the same structure as they use in the Trinity Study. Major changes:

  1. we use retirement lengths of 30-60 years and
  2. withdrawal rates only between 3% and 5% in 25 basis point step. No serious long-term retirement planner with a horizon of 50-60 years would ever even consider a withdrawal rate above 5%, anyway, given that equities return “only” about 6.6% and you have to account for volatility and sequence of return risk.



The success criterion is a final asset value of zero as in the Trinity Study.

![swr-part1-table1](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/11/swr-part1-table1.png?resize=764%2C500&ssl=1)Success Rates for different SWRs, by equity share and retirement horizon (1871-2015)

A few conclusions from this table:

  * The success rates for a 30-year horizon are roughly consistent with the Trinity study.
  * Success probabilities stay very high at all horizons when using 75-100% equity shares and withdrawal rates of 3.5% and under.
  * Success probabilities deteriorate quite a bit when the retirement horizon goes from 30 to 60 years.
  * It may be true that for a 30-year horizon, an equity share of 50-100% gives consistently high success rates if the withdrawal rate is 4% or lower. Essentially the main result of the Trinity Study! But for longer horizons, 100% stocks gives the highest success rate. This goes back to our earlier research that showed that [over long horizons bonds can have extended drought periods](http://earlyretirementnow.com/2016/05/19/bond-vs-stock-risk/) and only equity-like returns are a guarantee for not running out of money over long horizons. For example, a 4% withdrawal rate has a 95% success probability in a 50%/50% over 30 years, but only 65% over 60 years. The failure probability is 7 times higher over the 60-year horizon!
  * A 5% withdrawal rate would have an unacceptably low success rate even after 30 years, and certainly after 60 years. As stated above, no early retiree should get anywhere close to a 5% withdrawal rate.



Another way to look at the data: Plot a time series chart of different safe withdrawal rates over time both for 30-year and 60-year horizons. In the chart below I use an 80% equity weight and 20% bond weight, pretty common among bloggers. Unsurprisingly, the 60-year withdrawal rates are significantly below the 30-year rates. There are only a few occasions where the 30-year SWR drops below 4%, but a 60-year retirement horizon has a few stubbornly long episodes with 3.5-4% withdrawal rates. So, 3.5% is the new 4%! What’s worse, in future posts, we will show that you’d likely have to reduce the 3.5% even further to account for a) today’s high CAPE ratio and b) a higher final asset target!!!

![swr-part1-chart1](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part1-chart1.png?resize=806%2C660&ssl=1)Safe Withdrawal Rates: 30 vs. 60-year horizons: 80% Stocks, 20% Bonds

Another way to slice the data; same chart but as a scatter plot instead of time series chart, see below. The 30-year safe withdrawal rate is on the x-axis and 60-year withdrawal rate is on the y-axis. The dots are all under the 45-degree line, no surprise here! On average, the 60-year SWR are more than a full percentage point below the 30-year SWR (below the 45-degree line), but in the region where it really matters, when the SWRs are low, the difference is “only” about 0.5%.

![swr-part1-chart2](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part1-chart2.png?resize=863%2C708&ssl=1)Safe Withdrawal Rates: 30-year horizon (x-axis) vs. 60-year horizon (y-axis). Blue line = 45-degree line

### Thanks for stopping by today! Please leave your comments and suggestions below! Also, make sure you check out the other parts of the series, see [here for a guide to the different parts so far](https://earlyretirementnow.com/safe-withdrawal-rate-series/)!

### Share this:

  * [ Share on X (Opens in new window) X ](https://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/?share=facebook)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/?share=reddit)
  * 


### Like this:

Like Loading…

### _Related_
