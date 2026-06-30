# SWR Series Part 3: Equity Valuation Regimes — earlyretirementnow.com

### Update: We posted the results from parts 1 through 8 as a Social Science Research Network (SSRN) working paper in pdf format:

### [Safe Withdrawal Rates: A Guide for Early Retirees (SSRN WP#2920322)](http://ssrn.com/abstract=2920322)

Welcome back to our safe withdrawal rate series! Over the last two weeks, we already posted [part 1 (intro and pitfalls of going beyond a 30-year horizon)](http://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/) and [part 2 (capital preservation vs. capital depletion)](http://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/). Today’s post deals with yet another early retirement pet peeve: safe withdrawal rates are likely overestimated given today’s expensive equity valuations. We wrote a [similar piece about this issue before](http://earlyretirementnow.com/2016/03/24/the-4-is-not-as-good-as-i-hoped/), but that was based on [cFIREsim](http://cfiresim.com/) external simulation data. We prefer to run our own simulations to be able to dig much deeper into this issue.

So, the point we like to make today is that looking at long-term average equity returns to compute safe withdrawal rates might overstate the success probabilities considering that today’s equity valuations are much less attractive than the average during the 1926-current period ([Trinity Study](https://www.onefpa.org/journal/Pages/Portfolio%20Success%20Rates%20Where%20to%20Draw%20the%20Line.aspx)) and/or the period going back to 1871 that we use in our SWR study.

Thus, following the Trinity Study too religiously and ignoring equity valuations is a little bit like traveling to Minneapolis, MN and dressing for the **average** annual temperature (55F high and 37F low, see [source](http://www.currentresults.com/Weather/US/average-annual-temperatures-large-cities.php), which is 13 and 3 degrees Celsius, respectively). That may work out just fine in April and October when the average temperature is indeed pretty close to that annual average. But if we already know that we’ll visit in January and wear only long sleeves and a light jacket we should be prepared to freeze our butt off because the average low is 8F =-13C! Likewise, be prepared to work with lower withdrawal rates considering that we’re now 7+ years into the post-GFC-recovery with pretty lofty equity valuations.

How do we account for today’s equity valuations? Very simple, we run our simulations and then compute success probabilities, not just averaging over **all** observations but we also bucket the over 1,700 possible retirement start dates in our study by how cheap or expensive equities were at the time. We’ll do so by looking at the well-known **CAPE Ratio**.

### A quick CAPE ratio primer

The measure for equity valuation we use is the **CAPE ratio**. We are all familiar with the [PE ratio](https://en.wikipedia.org/wiki/Price%E2%80%93earnings_ratio). Price divided by earnings measures how much you’re paying per dollar of the current annual earnings (normally a four-quarter trailing E, though PE ratios based on estimates of future earnings are common, too). This is done both on the individual equity level, but also for an index, e.g., the S&P500.

[Robert Shiller](https://en.wikipedia.org/wiki/Robert_J._Shiller), who is one of the [2013 economics Nobel Prize](http://www.nobelprize.org/nobel_prizes/economic-sciences/laureates/2013/press.html) winners, introduced another interesting concept: The [cyclically-adjusted price earnings (CAPE) ratio](https://en.wikipedia.org/wiki/Cyclically_adjusted_price-to-earnings_ratio) (see [free data on Shiller’s site](http://www.econ.yale.edu/~shiller/data/ie_data.xls)). It divides today’s index level by a 10-year rolling **average** of real (CPI-adjusted) earnings. Think of it as the average real earnings over an entire business cycle. Shiller found that the usual PE ratio is a bit too noisy; remember, you divide two highly volatile series P and E. However, making the E portion of the PE less volatile apparently gives you a sharper predictor of future returns.

The median CAPE ratio is just about 15. Which is quite intriguing because if we were to invert that number 1/15=0.0667=6.67% (= CAE**Y** = cyclically-adjusted earnings **yield**) we’d land almost exactly at the long-term average real equity return of around 6.6% (see more details [here](http://earlyretirementnow.com/2016/05/19/bond-vs-stock-risk/)). That’s more than a coincidence because the real return on the index _should_ roughly equal the average real earnings yield in the index. Since 1871, the CAPE was anywhere between 5 when stocks are really cheap at or near the bottom of recessions/bear markets to over 40 at the height of the dot-com bubble. And most importantly:

**The Shiller CAPE is correlated with future equity returns**

That’s right, today’s CAPE ratio is pretty good at predicting future equity returns. Well, not perfectly but there seems to be a strong and statistically significant inverse relationship between the CAPE and forward-looking equity returns, see chart below where we plot the CAPE ratio versus the subsequent 10-year annualized S&P500 return. For something as ostensibly unpredictable as stock returns, this is truly amazing. Equity returns are not exactly a random-walk! If we split the CAPE into four regions we get pretty different average equity returns by bin:

  * CAPE below 15 (below the median): Average equity return of 9% real (!)
  * CAPE slightly elevated (15-20): Average equity return just under 6%, still very solid returns that will likely support a 4% safe withdrawal rate.
  * CAPE moderately elevated (20-30): Only about 3% real return (!) going forward. Today’s CAPE falls into this range. The 9/30/2016 level was at just under 27, and after the recent rally, it’s even a bit above 27.
  * CAPE severely elevated (30+): A below -1% real return over the next ten years. Bummer! Good luck starting your retirement in that environment!

![swr-part3-chart5](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part3-chart5.png?resize=845%2C705&ssl=1)Scatter Plot of Shiller CAPE (x-axis) vs. subsequent 10-year annualized real total return. Red lines = average in the bins CAPE<15, CAPE between 15 and 20, CAPE between 20 and 30, and CAPE above 30.

### Simulation results

Let’s look at the Success rates over 30-year (top panel) and 60-year horizons (bottom panel). The charts have the familiar format you might remember from before, plotting the success rates as a function of the portfolio equity share (rest invested in 10Y Treasury Bonds). In this chart, each line corresponds to the success rate of a different CAPE regime at the beginning of retirement.

![swr-part3-chart1](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part3-chart1.png?resize=815%2C865&ssl=1)Success Rates of the 4% Rule with capital depletion, as a function of the portfolio equity share for different CAPE regimes and different horizons (top=30Y, bottom=60Y)

Quite intriguingly, over the 30-year horizon (top panel) and for equity weights greater than 40%, every single failure of the 4% rule occurred when the CAPE was above 15 at the start of retirement. In contrast, for all CAPE<15 you have a 100% success rate. You get close to a 100% success rate with a 75+% equity portion and the CAPE<20\. I wish the original authors of the Trinity Study had dug deeper into when those failures occur.

Also, did we mention that a 30-year horizon is an entirely different animal from a 60-year horizon? Oh, yeah, [we pointed that out before](http://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/), but to state the obvious, success probabilities are much, much lower over the longer horizon.

Anyway, the current CAPE of 27 falls smack into the 20-30 region represented by the yellow line. At a 60-year horizon with capital depletion, we are now looking at a 72% success rate with 100% equities (much lower than the 89% success rate over 30 years). Quite amazingly, lowering your equity share in response to expensive equity valuations will actually _lower_ (!) your success probability. How crazy is that? True, for a seriously overvalued equity market (CAPE above 30) you do get a bit of a hump-shaped curve (see the maroon line in the bottom panel) with a sweet spot between 70 and 80% equity weight (same is true for the 30-year horizon with both the 20-30 CAPE and 30+ CAPE). But for the other three lines in the bottom chart, including the yellow line representing today’s regime, we see that the success probability is solidly increasing monotonically in the equity weight. **Equities rule when you’re looking at a 60-year horizon!** Again: due to the long horizon, investing in equities is the way to go even if they are overvalued in the short-term. Bonds with a 2.6% long-term real return just threaten your long-term sustainability [as we mentioned here](http://earlyretirementnow.com/2016/05/19/bond-vs-stock-risk/). (Of course, one solution would be to have a higher bond share only until equities return to a CAPE<20 and then increase the equity share again. But we haven’t calculated that yet.)

### Higher final value target

As we stated previously, a zero final asset value is not acceptable to us due to our strong desire to leave a bequest. As expected, once we target a higher than zero final asset value, the success probabilities diminish even more, as we [pointed out previously](http://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/). Below are the charts for targeting a 50% final asset value target.

![swr-part3-chart2](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part3-chart2.png?resize=811%2C855&ssl=1)Success Rates of the 4% Rule with a 50% final value target, as a function of the portfolio equity share for different CAPE regimes and different horizons (top=30Y, bottom=60Y)

Now even the CAPE regimes of below 15 or 15-20 no longer guarantee success over a 60-year horizon (or even a 30-year horizon for that matter). Bummer! The only good news is that the higher final asset target only lowers the success probability to 71%, from 72% (bottom chart, yellow line, 100% equities).

### Let’s lower the SWR to 3.5%

Lowering the withdrawal rate to 3.5% should improve the success rates, as we pointed out [last week:](http://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/) at 100% equity share we had a 96% success probability preserving 50% of the final value after 60 years. That rate goes down to 88% when the CAPE ratio is between 20 and 30. Of course, for CAPE values below 20, the 100% equity portfolio had a 100% success rate, both over 30 and 60-year horizons. Nice to know, but again, today’s CAPE is at 27. For me personally, a 12% failure probability is still a bit too high.

![swr-part3-chart3](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part3-chart3.png?resize=817%2C857&ssl=1)Success Rates of the 3.5% Rule with a 50% final value target, as a function of the portfolio equity share for different CAPE regimes and different horizons (top=30Y, bottom=60Y)

### How about 3.25%?

To insulate ourselves from running out of money we likely have to lower the SWR all the way to 3.25%. Now we can get all the way to 97% success probability with 100% equities and even close to 100% with an equity share of 80-90%, see chart below.

![swr-part3-chart4](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2016/12/swr-part3-chart4.png?resize=819%2C849&ssl=1)Success Rates of the 3.25% Rule with a 50% final value target, as a function of the portfolio equity share for different CAPE regimes and different horizons (top=30Y, bottom=60Y)

I wouldn’t want to get my hopes too high about the benefits of bonds, though. Despite the recent rally in bond yields (and the resulting pummeling of bond prices) since November 8, yields are still extremely low by historical standards. For example at 2% annual inflation and around 2.5-2.6% yield for the 10Y Treasury Bond, we are looking at 0.5-0.6% real yield. Much less than the average 2.6% real return!

**Update (2/7/2022):** As suggested by reader AndyG42, I should point out that over the years, my views on the 100% equity portfolio have evolved. It’s certainly true that the probability of failure is small but if you like to **eliminate** the chance of a failure in past historical cohorts, you’re better off with a lower-than-100% equity weight, likely somewhere around 70-80%.

### Conclusion

We face a triple-whammy of bad news when it comes to safe withdrawal rates and using the Trinity Study data for our purposes:

  1. We have a longer retirement horizon. My wife will be in her mid-30s when we retire and her family seems to have a longevity gene. We like the money to last until my wife is at least in her mid-90s. We face a 60-year retirement horizon, twice the longest horizon the Trinity Study considers.
  2. We like to leave a bequest
  3. Today’s equity expected returns could be low due to the current sky-high equity valuations



All of that does not bode well for the 4% rule. To push failure rates of the withdrawal strategy to a low enough level, we’d likely have to lower the SWR to 3.25%.

Quite intriguingly, bonds don’t offer much benefit for the success rates, unless stocks are wildly overvalued, with much higher CAPE ratios than today’s value (>30!). For CAPE ratios below 30, mixing in bonds has either only a marginal benefit or even  _lowers_ the success probability.

What we learned so far: The Trinity Study and many in the FIRE crowd seem to recommend a generous withdrawal rate and conservative stock vs. bond allocation. But with a 4% SWR and 70-80% equity weight you have a roughly 1 in 3 chance of wiping out your money after 60 years. We want to do the **opposite** : A conservative withdrawal rate (e.g. 3.25%) and a generous equity weight (e.g. 100%). Who would have thought!?

### Thanks for stopping by today! Please leave your comments and suggestions below! Also, make sure you check out the other parts of the series, see [here for a guide to the different parts so far](https://earlyretirementnow.com/safe-withdrawal-rate-series/)!

### Share this:

  * [ Share on X (Opens in new window) X ](https://earlyretirementnow.com/2016/12/21/the-ultimate-guide-to-safe-withdrawal-rates-part-3-equity-valuation/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://earlyretirementnow.com/2016/12/21/the-ultimate-guide-to-safe-withdrawal-rates-part-3-equity-valuation/?share=facebook)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://earlyretirementnow.com/2016/12/21/the-ultimate-guide-to-safe-withdrawal-rates-part-3-equity-valuation/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://earlyretirementnow.com/2016/12/21/the-ultimate-guide-to-safe-withdrawal-rates-part-3-equity-valuation/?share=reddit)
  * 


### Like this:

Like Loading…

### _Related_
