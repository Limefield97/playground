# SWR Series Part 4: Social Security and Pensions — earlyretirementnow.com

_Title Picture credit:[Flickr](https://www.flickr.com/photos/68751915@N05/6280517815)_

### Update: We posted the results from parts 1 through 8 as a Social Science Research Network (SSRN) working paper in pdf format:

### [Safe Withdrawal Rates: A Guide for Early Retirees (SSRN WP#2920322)](http://ssrn.com/abstract=2920322)

After a one-week hiatus over the holidays when we wrote about a lighter topic (dealing with [debt, booze, and cigarettes](http://earlyretirementnow.com/2016/12/28/seven-reasons-in-defense-of-debt-and-leverage/), go figure), let’s return to the safe withdrawal rate topic. We’ve already looked at:

  * the sustainable withdrawal rates over 30 vs. 60-year windows ([part 1](http://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/)),
  * capital depletion vs. preservation ([part 2](http://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/))
  * and the current expensive equity valuations ([part 3](http://earlyretirementnow.com/2016/12/21/the-ultimate-guide-to-safe-withdrawal-rates-part-3-equity-valuation/)).



The bad news was that after all that number-crunching, the sensible safe withdrawal rate with an acceptable success rate melted down all the way to 3.25%. So much for the 4% safe withdrawal rate! That 25x annual spending target for retirement savings just went up to 1/0.0325=30.77 times. Ouch! Sorry for being a Grinch right around Christmas time!

But not all is lost! Social Security to the rescue! We could afford lower withdrawals later in retirement and, in turn, scale up the initial withdrawals a bit, see chart below. How much? We have to get the simulation engine out again!

![swr-part4-chart2](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/01/swr-part4-chart2.png?resize=590%2C273&ssl=1)With Social Security (and/or a pension) later during retirement, we can afford higher initial withdrawal rates!

### Our personal situation

Under the current Social Security setup, Mr. ERN is eligible for Social Security at age 62, which is 18 years after the planned retirement. But we will likely wait until Mr. ERN is in his late 60s to maximize the Social Security benefit. That’s roughly 25 years into our 60-year retirement. Together with the benefit from Mrs. ERN and a small legacy pension for Mr. ERN, we expect a total combined annual benefit of about 0.01 times our financial net worth at the start of our retirement. That’s all under the (rosy?) assumption that there are no benefit cuts in Social Security, whether through adjustments in the benefits formula, changes in the retirement age or some form of means-testing. The likelihood of benefit cuts is a whole separate topic for a future post, though.

So, 35 years worth of 1% extra income during a 60-year retirement horizon affords us a 1% / 60 x 35 = 0.583% extra withdrawal, right? Withdraw 3.25%+0.583%=3.833% for the first 25 years and 2.833% for the next 35 years, which combined with the social security benefit generates a fixed real consumption path of 3.833% of initial net-worth. Almost back to 4%, how cool is that? Almost too good to be true! Well, unfortunately, this back-of-the-envelope calculation **is** too good to be true. The time value of money messes up the entire calculation! In other words, Social Security benefits many years in the future are going to be worth a lot less in today’s dollars. And even worse, the dreaded Sequence of Return Risk (SoRR) comes into play here again because we front-load the withdrawals. How much of a haircut do we have to apply to our calculation? We need to look at our simulations to find out.

### SWR simulations: 1871-2015

The baseline simulation (more scenarios below), is what we call “25Y-1%” where we start with a withdrawal rate x% in the first year, inflation-adjust over time and take the withdrawals from the portfolio down by 1 percentage point (also adjusted for inflation) once we draw Social Security benefits. For each possible starting date, we solve for the withdrawal rate that _exactly matches_ our final value target (50% of beginning value, in real terms) after 60 years.

In the scatterplot below we do the usual analysis as before: Compare SWRs in two different scenarios: No Social Security (x-axis) vs. our likely Social Security benefits (y-axis). Of course, all dots are above the 45-degree line indicating a higher SWR, but not by much.

![swr-part4-chart7](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/01/swr-part4-chart7.png?resize=836%2C753&ssl=1)Safe Withdrawal Rates over a 60-year horizon for a 100% Equity portfolio: Baseline (no Social Security) (x-axis) vs. Social Security Benefits after 25 years, amounting to 1% of T=0 Net Worth (y-axis). Blue line = 45-degree line.

Because the scatterplot above was so hard to decipher, let’s plot the **increase** in the SWR due to the Social Security benefits on the y-axis, see chart below. I do this for all months, but I also mark the dots when the CAPE ratio was between 20 and 30 (12/31/2016 CAPE is around 28, according to [Professor Shiller](http://www.econ.yale.edu/~shiller/data.htm), page accessed on January 2, 2017). The increase in the SWR from our Social Security assumption is a lot leaner than the back-of-the-envelope calculation. Bummer! The SWR increase ranges from about 0.12% to just under 0.25%, with a median of around 0.18%. This will not bring our SWR back to 4%!

![swr-part4-chart8](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/01/swr-part4-chart8.png?resize=828%2C753&ssl=1)Safe Withdrawal Rates over a 60-year horizon for a 100% Equity portfolio: Baseline (no Social Security) (x-axis) vs. increase in SWR due to Social Security Benefits after 25 years.

![swr-part4-chart8b](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/01/swr-part4-chart8b.png?resize=863%2C661&ssl=1)

Same chart as above, but as a time-series chart. Increase in SWR due to Social Security Benefits after 25 years.

### How about other Social Security and Pension assumptions?

We look at a total six scenarios, three starting dates: 20, 25, and 30 years into retirement and two different benefit levels: 1% and 2% of the initial retirement nest egg. So, for example, if you have a $1,000,000 portfolio and expect $20,000 in benefits after 30 years you’d look at the 30Y-2% model. As we mentioned above, our own personal situation comes closest to the 25Y-1% model.

Instead of plotting the scatterplots above, let’s just display one summary statistics table about how much the different Social Security / Pension models increase the SWR, see table below, specifically the median increase. Note that the order is from the smallest to the largest discounted sum of benefits (30Y-25Y-20Y). We calculate the median increase for all months, for months with a CAPE between 20 and 30, and also for months when the CAPE was between 20 and 30 and the baseline SWR was below 4%. We calculated the latter because we wanted to see how much of a difference our Social Security would have made when we really have to rely on it due to bad financial market performance.

![swr-part4-chart9](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/01/swr-part4-chart9.png?resize=536%2C207&ssl=1)Median Increase in the SWR from getting Social Security benefits. 100% equity weight, 60-year horizon.

In our personal situation, we’d expect a 0.191% increase not conditioning on the CAPE regime, 0.179% for today’s CAPE regime, and 0.164% conditional on actually having to rely on Social Security. Hmmm, slightly disappointing. What’s particularly unfortunate in our calculations is that the increase in the SWR is lower when we need it the most, namely when the CAPE is high and the baseline SWR is already below 4%. Unless you expect very generous benefits, Social Security will not serve as a panacea for the 4% rule!

_**A little side note:** Do you notice something in that table above? The incremental effect on the SWR exactly doubles when going from 1% to 2% worth of Social Security benefits. That’s no coincidence. It’s a mathematical result. So if you happen to expect Social Security and/or Pension benefits amounting to, say, 1.3% of your initial net worth, simply take the 1% figure above and multiply by 1.3. I don’t want to bore everybody with the arithmetics behind our calculations, but maybe in a future post, we will do a mathematical appendix, gasp!!! Stay tuned!_

### Failure rates of different SWRs

We can also look at the failure rates of different withdrawal rates between 3 and 4% in 25bps steps, see table below.

![swr-part4-chart9b](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/01/swr-part4-chart9b.png?resize=681%2C345&ssl=1)Failure Rates of different initial SWRs (columns) under two CAPE regimes (top=current, bottom=all months), Social Security parameters (rows), 60-year horizon, 50% final asset value target, 100% equity weight.

Bottom line: If you’re unlucky and face adverse capital marker returns early on in retirement and you keep withdrawing your initial rate then your portfolio will be so compromised by the time you reach your Social Security age that it won’t make much of a difference anymore.

So, in today’s environment, the highest withdrawal rate we’d personally be comfortable with is 3.5%. That has a 3.9% failure rate. The 4% SWR would have had a 28.8% failure rate in the absence of Social Security and only a pretty generous benefit worth 2% p.a. and 20 years after the retirement would significantly reduce the failure rate to 11.7%. Under all other parameterizations, the failure rates were still around 20%. Unacceptably high!

**Conclusion: Even before accounting for potential future benefit cuts, Social Security benefits will not make a huge difference in the Safe Withdrawal Rate and will most definitely not save the 4% rule!**

### 

### Appendix: Data, data, and more data

Let’s look at some more data tables that cover more assumptions. Hopefully, this can serve as a reference for readers who want to look beyond the ERN family assumptions and see how the failure rates would have looked like in their personal situation.

  * Retirement horizon: 60 years (first table) and 50 years (second table). We don’t even display anything below 50 years considering that most folks in the FIRE crowd will retire in their 30s, maybe early 40s.
  * Today’s CAPE regime (20-30) in the top half of each table vs. unconditional on CAPE regime in the bottom half of each table, just for reference.
  * Three different social security parameters: None at all, 1% benefits after 25 years (ERN family assumption), 2% benefits after 30 years (for example $1,000,000 portfolio and $20k in benefits after 30 years).
  * Four different equity shares: 70/80/90/100%. I don’t even go below 70% because the failure rates get so much worse. Also, recall that the bond index I use here is a 10y Treasury index with no credit risk. A 30% allocation to a safe government bond index plus 70% equities roughly corresponds to a 40% allocation to investment grade bonds plus 60% equities. We definitely do not recommend going below that equity allocation to preserve long-term sustainability of the portfolio.
  * Capital Depletion vs. 50% final asset target (left vs. right half of table)
  * Five different withdrawal rates between 3 and 4% in 0.25% steps.

![swr-part4-chart6](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/01/swr-part4-chart6.png?resize=863%2C738&ssl=1)60-Year horizon failure rates of different Withdrawal Rates (columns), with different final asset targets (left=capital depletion, right=50% FV target), for different CAPE regimes (top=current CAPE regime, bottom=all months), and Social Security assumptions and equity shares (rows). ![swr-part4-chart5](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/01/swr-part4-chart5.png?resize=863%2C738&ssl=1)50-Year horizon failure rates of different Withdrawal Rates (columns), with different final asset targets (left=capital depletion, right=50% FV target), for different CAPE regimes (top=current CAPE regime, bottom=all months), and Social Security assumptions and equity shares (rows).

### Thanks for stopping by today! Please leave your comments and suggestions below! Also, make sure you check out the other parts of the series, see [here for a guide to the different parts so far](https://earlyretirementnow.com/safe-withdrawal-rate-series/)!

### Share this:

  * [ Share on X (Opens in new window) X ](https://earlyretirementnow.com/2017/01/04/the-ultimate-guide-to-safe-withdrawal-rates-part-4-social-security-pensions/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://earlyretirementnow.com/2017/01/04/the-ultimate-guide-to-safe-withdrawal-rates-part-4-social-security-pensions/?share=facebook)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://earlyretirementnow.com/2017/01/04/the-ultimate-guide-to-safe-withdrawal-rates-part-4-social-security-pensions/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://earlyretirementnow.com/2017/01/04/the-ultimate-guide-to-safe-withdrawal-rates-part-4-social-security-pensions/?share=reddit)
  * 


### Like this:

Like Loading…

### _Related_
