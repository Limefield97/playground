# SWR Series Part 2: Capital Preservation vs. Capital Depletion — earlyretirementnow.com

### Update: We posted the results from parts 1 through 8 as a Social Science Research Network (SSRN) working paper in pdf format:

### [Safe Withdrawal Rates: A Guide for Early Retirees (SSRN WP#2920322)](http://ssrn.com/abstract=2920322)

Welcome back! This is our **50th post** , as I just learned from WordPress. Cheers to that and thanks to our readers for coming back every week! As promised in [last week’s introductory post](http://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/), we present some additional results about safe withdrawal rates for early retirees. Today’s post deals with an important issue that all retirees (whether retiring early or in their mid-60s) should ask themselves:

**Do we want to deplete our savings or maintain a certain minimum real value of the principal to bequeath to our heirs?**

We are amazed by how little discussion there is in the personal finance community about this. Hence, today’s topic:

### **Capital Preservation vs. Capital Depletion**

  1. **capital preservation** : target a certain minimum asset level (as % of the initial value) at the end of the retirement horizon. Under full capital preservation we’d aim to keep the real, inflation-adjusted value constant, by consuming “only” the capital gains, dividends, and interest over time, while keeping the principal (plus inflation-adjustment!) in place.
  2. **capital depletion** : target a zero (or at least positive) final portfolio value, by consuming gains as well as principal over time



Needless to say, the [Trinity Study](https://www.onefpa.org/journal/Pages/Portfolio%20Success%20Rates%20Where%20to%20Draw%20the%20Line.aspx) does its calculations according to strategy 2. In other words, a “success” per Trinity is to not run out of money before the end of year 30. Whether at a 30-year or 60-year horizon, the idea of depleting capital has at least two unsettling features for us:

  * We like to leave a bequest to our daughter (and future grandchildren) and several charitable causes.
  * We are uncomfortable with the idea of running out of money in our late 80s and being forced to live a less than dignified final years of our retirement or becoming a burden to our daughter.



### **The fallacy of extrapolating from 30-year to 60-year windows**

It doesn’t take a rocket scientist to realize that capital preservation allows you to withdraw less than capital depletion. How much? That depends on the portfolio returns and the investment/retirement horizon. We found surprisingly little work in the FIRE community dealing with this issue, hence we got the computer running to do some research on our own.

One advantage of targeting capital preservation is that if your withdrawal strategy  _preserves_ capital for one 30-year window it will likely do so for a second 30-year window. But, if you  _deplete_ your capital after 30 years, then you cannot keep the same withdrawal rate for another 30 years. This is almost too trivial to point out, but you’ll be amazed how often you hear folks on the web mixing up the two. The extrapolation fallacy usually works like this:

_“There is a small probability of running out of money after 30 years. But the median final value after 30 years is likely much higher than even the starting value, even adjusted for inflation. So, let’s just extrapolate 30-year window to a 60-year window.”_

Huh? Do you see the fallacy here? The Trinity Study is not about the _median_ retiree. It’s about the probability of _tail events_. We already know that a median retiree has nothing to worry about if the real withdrawal rate is roughly the same as the real capital market return. But after 30 years, there will be a significant percentage of retirees who will not be counted as a failure in the Trinity Study (portfolio value >0) but their portfolio might have been compromised enough to run dry after another 5 or 10 years. They are the people who will not be able to do a net worth “reset” back to the median after 30 years. That makes this extrapolation fallacy so dangerous.

### **Warmup: Some simple calculations**

Before we even jump into the simulations, let’s do a little warm-up exercise. To gain some insights into why the 60-year withdrawal rates are likely significantly lower than the 30-year rates, let’s do some simple calculations in Excel.

Let’s assume a constant 4% p.a. real (inflation-adjusted) portfolio return. A retiree with a $1,000,000 portfolio withdraws a fixed amount at the beginning of the first month and then inflation-adjusts the withdrawals every month. Let’s calculate how much the retiree can withdraw under the following withdrawal strategies:

  1. Capital Preservation: 3.92%. Why not 4.00%? That’s because the initial withdrawal takes place at the beginning, not the end of the month. Who knew that such a trivial difference can make a 0.08% difference in the SWR?
  2. Target 50% remaining net worth after 60 years: 4.12%. Amazing, how a 0.20% difference in the withdrawal rate ($167 in the first month) makes a huge difference after 60 years. But then again, that’s 60 years of compound interest for you!
  3. Target capital depletion after 60 years: 4.33%. Only another 0.21% increase in the withdrawal rate and we wipe out the capital after 60 years.
  4. Target 50% remaining net worth after 30 years: 4.79%. If you wonder how long would the remaining half million last at that withdrawal rate: 13 years (to be precise, 160 months, for a total of 520 months).
  5. Deplete the entire portfolio after 30 years (Trinity Study assumption): 5.66%. That’s a whopping 1.74 percentage points above the capital preservation rate!

![swr-part2-chart2](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part2-chart2.png?resize=863%2C626&ssl=1)Different withdrawal strategies imply very different maximum withdrawal rates!

What we find intriguing about these numbers is that over a 30-year horizon, the benefit of capital depletion adds 1.74% to your safe withdrawal rate, while over a 60-year horizon depleting your capital adds only 0.41%. That’s one of the reasons we believe the Trinity Study is so flawed when applied to the early retirement community; a 60- year retirement horizon is a completely different animal from the Trinity Study 30-year horizon.

### **Simulations**

The calculations above are all nice, but they are really only relevant for the median retiree. We don’t want to commit that same flaw we pointed out above. To determine the _tail event_ probabilities, we again have to employ our simulation framework, using monthly asset returns since 1871 to see how different retirement cohorts would have fared under different assumptions. The table below is an extension of the [results from last week](http://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/). We report success probabilities over 30 and 60-year horizons (we leave out the 40 and 50-year figures to keep the table size manageable). The new feature in this table is that we calculate success probabilities not just for a capital depletion target but also for maintaining 25%, 50%, 75%, and 100% of the capital after 30 and 60 years. Note that the success criterion applies only to the _final_ period. You could temporarily fall below that target, but as long as you finish above the target, we call it a success.

As we already saw last week, for a 60-year horizon, a withdrawal rate of 3.5% or below and an equity weight of 75% yielded excellent success probabilities. The good news is that targeting a higher final asset value does not mess up our success probabilities much. For example, at 100% stocks and 3.5% withdrawal rate, the success rate drops from 98% to 96% when going from capital depletion to a 100% final target value. Still acceptable! For a 30-year horizon, it’s a very different story. At 4% withdrawal rate and 100% equity weight you have a 97% success rate when targeting capital depletion but only 80% success rate when targeting 100% capital preservation. The intuition goes back to the simple Excel calculations: Over 30 years, capital depletion gives you such a big boost to the allowable withdrawal rate because the horizon is so much shorter. Hence, to achieve capital preservation we’d have to either seriously cut our withdrawal rate or accept much lower success rates.

![swr-part2-table1](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part2-table1.png?resize=780%2C1762&ssl=1)Success Probabilities for different Withdrawal Rates, Equity Shares, Retirement Horizons and Final Asset Target Values

We also found some interesting insights when plotting the success probabilities of different withdrawal strategies as a function of the equity weight, see chart below. It’s basically some of the same information as in the table above, but easier to visualize. The top chart is for a 3.5% withdrawal rate and the bottom chart for the 4% rate. Each chart has 4 lines for the different combinations of 30-year and 60-year retirement horizons, each with capital depletion (FV=0%) and capital preservation (FV=100%).

![swr-part2-chart1](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part2-chart11.png?resize=813%2C861&ssl=1)How to trash the Trinity Study with one single chart: Success probabilities as a function of the equity share (x-axis), two different withdrawal rates (top/bottom chart) for four different withdrawal strategies.

The dark blue line (30Y horizon, capital depletion) is what the Trinity Study is all about. And, according to this chart, it’s a completely different animal (probably a different animal from a different continent) from the other three lines:

  * Success rates are significantly higher under the Trinity Study assumptions than under the other, FIRE-relevant parameterizations. At 3.5% withdrawal rates, the 30-year, FV=0 rule is pretty much fool-proof even at equity shares significantly below 50%. Not so over the 60-year horizon or for a 30-year horizon with capital preservation. For equity weights between 50% and 100% we face success rates that can be quite a bit lower. For example, look at the 65% success rate vs. 95% success rate for capital depletion, 50% equity weight, and 4% withdrawal rate.
  * The retirement horizon has implications for the **portfolio allocation**. While the Trinity Study suggested that pretty much any equity share between 50% and 100% is close to foolproof (and we confirmed that result) the simulations over 60-year horizons suggest that the success probability is monotonically increasing in the equity weight. Even more importantly, the success probabilities seem to drop off quite significantly when going below 70% equity weight. Over longer horizons, bonds are bad!



Another intriguing result from this chart: The 60-year capital preservation rule had a slightly _higher_ (!) success rate than the 30-year capital preservation rule, at least for high enough equity shares. How is that possible? It’s quite intuitive: If your portfolio value was, say, 90% after 30 years, then you would have failed the 30-year capital preservation condition. But with the average portfolio return above 4% for a high enough equity share, you can likely get above the 100% target again over the next 30 years.

### **Capital Depletion vs. Preservation Scatter Plots**

Just like [last week](http://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/), let’s create a scatter plot of the maximum allowable withdrawal rates under two different withdrawal strategies. Here are two charts, each with the SWR under capital depletion (FV=0) on the x-axis and under capital preservation (FV=100%) on the y-axis. The first chart for a 30-year horizon and the second chart for a 60-year horizon.

![swr-part2-chart3](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part2-chart3.png?resize=863%2C654&ssl=1)Safe Withdrawal Rates over a 30-year horizon for an 80/20 portfolio: Capital Depletion (x-axis) vs. Capital Preservation (y-axis). Blue line = 45-degree line ![swr-part2-chart4](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part2-chart4.png?resize=863%2C665&ssl=1)Safe Withdrawal Rates over a 60-year horizon for an 80/20 portfolio: Capital Depletion (x-axis) vs. Capital Preservation (y-axis). Blue line = 45-degree line

For a 30-year horizon, the dots tend to fall significantly below the 45-degree line. The median distance is about 1.25%. So, to preserve capital over a 30-year horizon you’d have to cut your SWR by about 1.25 percentage points. Ouch! In contrast, over a 60-year horizon, there is only a relatively tiny distance between the dots and the 45-degree line, only about 0.19%. Lowering the withdrawal rate by less than one-fifth of a percentage point can make the difference between running dry after 60 years and capital preservation. That’s good news and bad news at the same time. If you care about leaving a bequest you don’t have to curb your consumption by much to ensure maintaining your portfolio value for 60 years. But the bad news is that over a 60-year horizon, small changes in the withdrawal rate can have huge consequences on final outcomes.

**Summary**

  * Safe withdrawal rules _can_ be extrapolated when the success criterion is capital preservation, at least if the equity share is high enough.
  * If the success criterion is capital depletion, as in the Trinity Study, we should not extrapolate safe withdrawal rules to longer horizons. Our simulations show that your failure rates grow significantly when going from 30 to 60-year horizons. You’d have to apply a 0.50% haircut to the withdrawal rate to achieve the same success rate again.
  * Bonds may look attractive in the Trinity Study setting but due to their low expected return (only 2.6% real over the entire time period since 1871), they pose a significant risk of running out of money in the long-run. This is consistent with our [earlier post on the long-term risks of low bond returns](http://earlyretirementnow.com/2016/05/19/bond-vs-stock-risk/).



**Update 7/26/2023:** People occasionally ask me how the simulation results change if we use updated data to include the 2020 pandemic and the 2022/23 bear market. Please see the table below: not much of a difference! That’s because the worst-case retirement cohorts in have either no impact from new data (1929) or very little impact only at the backend when adding new data in years 55+ or retirement. So, we can still reliably use the tables above.

![](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2023/07/SWR-Series-Part02-Table01-updated.png?resize=863%2C569&ssl=1)SWR stats, updated to include data to 2023.

### Thanks for stopping by today! Please leave your comments and suggestions below! Also, make sure you check out the other parts of the series, see [here for a guide to the different parts so far](https://earlyretirementnow.com/safe-withdrawal-rate-series/)!

### Share this:

  * [ Share on X (Opens in new window) X ](https://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/?share=facebook)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/?share=reddit)
  * 


### Like this:

Like Loading…

### _Related_
