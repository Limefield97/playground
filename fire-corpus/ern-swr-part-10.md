# SWR Series Part 10: Debunking Guyton-Klinger Some More — earlyretirementnow.com

[Last week’s post](http://earlyretirementnow.com/2017/02/08/the-ultimate-guide-to-safe-withdrawal-rates-part-9-guyton-klinger/) about the [Guyton-Klinger Dynamic Withdrawal Rule](http://cornerstonewealthadvisors.com/wp-content/uploads/2014/09/08-06_WebsiteArticle.pdf) only scratched the surface and we ran out of time and space. So, today we like to present some additional and detailed simulation data to present at least four areas where Guyton and Klinger are quite confusing and misleading:

  1. The ambiguity between withdrawal _rates_ and withdrawal _amounts_. A casual reader might overlook the fact that the withdrawal _amounts_ may very well fall outside a guardrail range. Inexplicably, Guyton and Klinger are very stingy with providing information on withdrawal amounts over time. There aren’t any time series charts of actual withdrawals in [their paper](http://cornerstonewealthadvisors.com/wp-content/uploads/2014/09/08-06_WebsiteArticle.pdf).
  2. True, Klinger shows time series charts in [this ](http://www.schulmerichandassoc.com/using_decision_rules_to_create_retirement_withdrawal_profiles.pdf)[paper](http://www.schulmerichandassoc.com/using_decision_rules_to_create_retirement_withdrawal_profiles.pdf), but they are only for the _median_ retiree. Does anyone else see a problem with that? The good old 4% rule did splendidly for the median retiree since 1871 so I haven’t really learned anything by looking at the median. [Wade Pfau showed](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2579123) (with a Monte-Carlo study) that the GK rule has a 10% chance of cutting withdrawals by 84% after 30 years. It’s very suspicious that the inventors of the rule don’t show more details about the distribution of withdrawals. You could call this either deception or invoke [Hanlon’s Razor](https://en.wikipedia.org/wiki/Hanlon's_razor) and blame it on sloppiness and incompetence, and both options are not very flattering.
  3. The Guyton-Klinger rule (even with a 4% initial withdrawal rate) is very susceptible to equity valuations. Results look much worse if you look at the average past retiree with an elevated CAPE ratio (20-30).
  4. Guyton-Klinger doesn’t afford you to miraculously increase your withdrawal amount without any drawback. The higher the initial withdrawal amount the higher the risk of massive spending cuts in the future.



So, let’s get cranking! We present another case study, the dreaded January 2000 retirement cohort, and also subject the Guyton-Klinger Rule to the whole ERN retirement withdrawal simulation engine to see how all the different retirement cohorts going back to 1871 would have fared. That’s over 1,700 cohorts because we insist on doing our simulations monthly, not annually.  


### 2000-2016 case study

We use real, CPI-adjusted returns for stocks and bonds up to December 2016 and then extrapolate equity and bond returns the same way we described in our [initial SWR post](http://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/) and in the [2000-2016 case study](http://earlyretirementnow.com/2017/01/18/the-ultimate-guide-to-safe-withdrawal-rates-part-6-a-2000-2016-case-study/). If you don’t like that extrapolation exercise up to December 2019, feel free to ignore those data points.

In the chart below we plot the CPI-adjusted real portfolio values under the static 4% rule and the three different Guyton-Klinger rules. The same parameters as last week. The 4% rule looks pretty grim, having exhausted more than 50% of its initial value and quickly depleting more even if equities continue with 6.6% real returns for the next few years.

Not so the GK rules: The 4% rule is now back to over 80% and could as well grow back to 90% of the initial value. The GK-5% rule is hanging in there pretty well and only the GK-6% rule looks a little bit shaky, in that it’s stuck at only 60% of the initial real value and not able to recover even if returns are average the above average priced S&P500 index.

![swr-part10-chart02b](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart02b.png?resize=729%2C525&ssl=1)Portfolio values (adjusted for CPI) of the January 2000 retirement cohort: Static 4% rule vs. Guyton-Klinger Dynamic rules (20%/10%), 80%/20% S/B portfolios, rebalanced monthly. Year 17-20 (Post-2016) returns extrapolated with average stock returns and 0.5% real bond return.

So far, so good. But just as last week, the time series of actual withdrawal amounts looks not so appetizing. Specifically, all of the GK rules experienced a 50%+ drop in their actual withdrawals and by the end of 2016, they are still between 30 and 40% below their initial withdrawal amount. What’s worse, even with pretty decent extrapolated returns going forward in 2017-2019, withdrawals are stuck at that reduced level.

![swr-part10-chart02](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart02.png?resize=863%2C658&ssl=1)Real withdrawal values (per $100 of initial portfolio value) of the January 2000 retirement cohort: Static 4% rule vs. Guyton-Klinger Dynamic rules (20%/10%), 80%/20% S/B portfolios, rebalanced monthly. Year 17-20 (Post-2016) returns extrapolated with average stock returns and 0.5% real bond return.

So, Guyton-Klinger would have been a major letdown for the January 2000 retirement cohort. Especially the initial withdrawal rates above 4% would have caused large and permanent declines in real withdrawal amounts.

### 1871-2015 retirement cohorts: All CAPE regimes

Of course, we can go only so far with case studies, so we were curious how all the different retirees between 1871 and 2015 would have fared with the Guyton-Klinger rule. Probably better than the crazy worst case scenarios of 1966 and 2000, but how much better?

Let’s look at how the GK rule with a 4% initial withdrawal rate would have fared for retirees between 1871 and 2015. This is for all retirees regardless of initial CAPE Ratio. Also, we don’t want to show just the median but also some left tail stats, namely the minimum withdrawal, the 10th percentile and the 25th percentile. See chart below:

![swr-part10-chart03](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart031.png?resize=863%2C646&ssl=1)Distribution of real, CPI-adjusted withdrawal amounts using Guyton-Klinger for 1871-2015 retirement cohorts: 4% initial withdrawal, 30-year retirement, all CAPE regimes, 80% stocks, 20% bonds.

It turns out the median hardly sees any spending cut. The 25th percentile suffers a 20% cut and manages to recover back to 100% after 19 years. The 10th percentile sees a 40% cut and no recovery back to the initial CPI-adjusted amount within 30 years. Just for the record, I find the GK rule better than the static 4% rule because I’d rather cut my consumption by 40% with a 10% probability than run out of money with a 5% probability. But the tail risk scenarios are not appetizing. And we’re not talking about the 0.00001% tail event, but the 10% lower tail! I would consider myself quite risk averse and if the 10th percentile looks awful this rule would be a non-starter. Even folks who are less risk-averse should probably worry at least about the 25th percentile.

[Last week](http://earlyretirementnow.com/2017/02/01/the-ultimate-guide-to-safe-withdrawal-rates-part-8-technical-appendix/) we also pointed out the crucial distinction between real inflation-adjusted withdrawal amounts and the withdrawal rates. Withdrawal amounts can have wide swings, while withdrawal rates stay inside the Guyton-Klinger guardrails for the most part.

_(side note: There is one exception namely when a market move is large enough that even the x=0.10 adjustment will not take the observed withdrawal rate back inside the guardrails and it takes two months of adjustments to accomplish that. So, don’t be surprised to see a very small percentage of months with rates outside the guardrails.)_

In any case, let’s look at the distribution of (real) withdrawal amounts and withdrawal rates over the entire 360 months and all 1,700+ cohorts, see chart below. The top portion is what we really care about, how much we can consume, specifically the percentage of observations that fall into various buckets. The bottom portion is the less-informative figure because that % is multiplied by the current portfolio value, i.e., a moving target. Also, I added three dividers to split the buckets into four sections: Below the lower guardrail (<3.2% in this example), between the lower guardrail and the initial withdrawal rate (3.2-4.0%), between the initial withdrawal amount and the upper guardrail (4.0-4.8%) and above the upper guardrail (4.8%+).

![swr-part10-chart04](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart041.png?resize=863%2C627&ssl=1)Distribution of real, CPI-adjusted withdrawal amounts (top) and rates (bottom) over the entire 30-year window using Guyton-Klinger for 1871-2015 retirement cohorts: 4% initial withdrawal, all CAPE regimes, 80% stocks, 20% bonds.

The good news: Guyton-Klinger will likely generate higher withdrawal amounts than the initial. 48.1% of the time we’d even be above 1.2-times above the initial amount. That’s as expected because we already know that the naive 4% rule would have created massive over-accumulation of wealth and the GK rule simply harvests the excess gains.

But GK also forces your withdrawals to below the initial value with a significant probability. 15% probability to withdraw less than 80% of the initial (again, there ‘s no guardrail for the withdrawal _amounts_ , only for the _rates_). 20.9% probability of falling into the 0.8 to 1.0-times the initial amount.

### 1871-2015 retirement cohorts: CAPE between 20 and 30

As we pointed out in [our post on equity valuations](http://earlyretirementnow.com/2016/12/21/the-ultimate-guide-to-safe-withdrawal-rates-part-3-equity-valuation/), it’s risky to average over all equity valuation regimes when we already know that today we’re in a world of much more expensive equities relative to earnings. So, let’s run the 4%-GK rule only in the months when we had Shiller CAPE ratios of between 20 and 30 (Current CAPE is at 28!).

The chart with the withdrawal amounts doesn’t look so appealing anymore. Sure, the median is hanging in there pretty well; it dips slightly below 4, but recovers by year 16 only to increase substantially after that to more than 50% above the initial withdrawal amount by year 30. Guyton-Klinger did exactly what it was designed to do: scale up the withdrawals when the market cooperates.

![swr-part10-chart05](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart051.png?resize=863%2C665&ssl=1)Distribution of real, CPI-adjusted withdrawal amounts using Guyton-Klinger for 1871-2015 retirement cohorts: 4% initial withdrawal, 30-year retirement, CAPE between 20 and 30, 80% Stocks, 20% Bonds.

But the less fortunate cohorts do much worse. The 25th percentile suffers about two decades of 25% decline of purchasing power. The 10th percentile drops to around 50% below for an entire decade. Of course, both recover back to their original withdrawal amounts but only after 26 and 29 years after retirement, respectively. Ouch!

The same distribution chart as before, see below. You now have a higher than 50% chance of consuming less than the original amount, even a 23.5% percent chance of consuming less than 0.8-times the original amount. All the while, of course, the withdrawal rates stay nicely inside the GK guardrails.

![swr-part10-chart06](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart061.png?resize=863%2C637&ssl=1)Distribution of real, CPI-adjusted withdrawal amounts (top) and rates (bottom) over the entire 30-year window using Guyton-Klinger for 1871-2015 retirement cohorts: 4% initial withdrawal, CAPE between 20 and 30, 80% Stocks, 20% Bonds.

### What if we increase the withdrawal rate to 5%?

Well, the GK rule was invented to increase the initial withdrawal rate, so let’s see what happens when we push the initial annualized withdrawal to 5% of the portfolio. In the chart below we see that not even the median withdrawal amount can keep up. It drops by a moderate amount, 18% below the initial but it takes almost a quarter century to get back to the initial withdrawal amount. Now even the 25th percentile faces a 50% drop in withdrawals and only recovers after 30 years. The 10th percentile saw a close to 60% drop in consumption and no recovery within 30 years. Not a pretty picture.

![swr-part10-chart07](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart071.png?resize=863%2C660&ssl=1)Distribution of real, CPI-adjusted withdrawal amounts using Guyton-Klinger for 1871-2015 retirement cohorts: 5% initial withdrawal, 30-year retirement, CAPE between 20 and 30, 80% Stocks, 20% Bonds.

The same distribution chart as above, but now looking even grimmer. We spend about one-third of the time withdrawing less than 0.8 times the initial amount, one-third of the time between 0.8 and 1.0 times the initial amount and another one-third above the “promised” 5%. Not a very pretty picture. Does anyone still claim that we can hack our initial withdrawal rate to 5% or more in today’s CAPE regime?

![swr-part10-chart08](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart081.png?resize=863%2C644&ssl=1)Distribution of real, CPI-adjusted withdrawal amounts (top) and rates (bottom) over the entire 30-year window using Guyton-Klinger for 1871-2015 retirement cohorts: 5% initial withdrawal, CAPE between 20 and 30, 80% Stocks, 20% Bonds.

### Another reason we’re no fans of Guyton-Klinger: It’s a “**dumb”** rule

Ok, to be sure, I’m not saying that Messrs. Guyton and Klinger or the folks who are using the rule are dumb. I’m sure they are all very smart individuals. I’m just saying that the GK method leaves me just as clueless about what’s a safe and appropriate withdrawal rate than before I started working on this topic. We saw above that the rule is quite susceptible to the equity valuation regime (just like the dumb static 4% rule).

To see how fundamentally “dumb” the GK rule actually is, let’s try to do the following thought experiment. Imagine we start GK with a withdrawal rate that’s clearly way too low, say 2% p.a. Nobody has ever depleted a portfolio with such a low target withdrawal rate. In fact, even your truly, your crazy cranky Uncle Ern curmudgeon would not argue for a withdrawal rate lower than 2%. Why would anyone cut the withdrawals below the initial amount? It’s completely uncalled for? But that’s what happens in a non-trivial percentage of cohorts, see chart below:

![swr-part10-chart09](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart09.png?resize=863%2C669&ssl=1)Distribution of real, CPI-adjusted withdrawal amounts using Guyton-Klinger for 1871-2015 retirement cohorts: 2% initial withdrawal, 30-year retirement, all CAPE regimes.

True, you’d eventually withdraw much more. There’s a close to 50% chance of a 60%+ rise in the withdrawal amount, but you’d also have a 20% chance of withdrawals falling below the initial amount. That’s unnecessary!

![swr-part10-chart10](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part10-chart10.png?resize=863%2C641&ssl=1)Distribution of real, CPI-adjusted withdrawal amounts (top) and rates (bottom) over the entire 30-year window using Guyton-Klinger for 1871-2015 retirement cohorts: 2% initial withdrawal, all CAPE regimes.

### Conclusion

For full disclosure, we say it again: We like the Guyton-Klinger Rule slightly better than a naive static withdrawal policy like the 4% rule. But Guyton-Klinger suffers from the exact same problems as the 4%: It’s not safe. You replace the small risk of running out of money with the 4% rule with a moderate risk of large spending cuts throughout many years of your retirement with Guyton-Klinger.

As if Guyton-Klinger wasn’t already bad enough with a 4% initial withdrawal rate, jacking up the initial withdrawal rate to 5% or more as GK recommend, especially in today’s environment of expensive equities and low bond yields, would be particularly irresponsible. It’s a bit like sending a novice skier down a double black diamond slope. The helmet (=equivlanet of the guardrails) will likely ensure the poor guy won’t kill himself, but it won’t be a pleasant ride. For us, a dynamic withdrawal rule would have to be a lot smarter than Guyton-Klinger!

### Thanks for stopping by today! Please leave your comments and suggestions below! Also, make sure you check out the other parts of the series, see [here for a guide to the different parts so far](https://earlyretirementnow.com/safe-withdrawal-rate-series/)!

Title Picture Source: Pixabay.com

### Share this:

  * [ Share on X (Opens in new window) X ](https://earlyretirementnow.com/2017/02/15/the-ultimate-guide-to-safe-withdrawal-rates-part-10-guyton-klinger/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://earlyretirementnow.com/2017/02/15/the-ultimate-guide-to-safe-withdrawal-rates-part-10-guyton-klinger/?share=facebook)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://earlyretirementnow.com/2017/02/15/the-ultimate-guide-to-safe-withdrawal-rates-part-10-guyton-klinger/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://earlyretirementnow.com/2017/02/15/the-ultimate-guide-to-safe-withdrawal-rates-part-10-guyton-klinger/?share=reddit)
  * 


### Like this:

Like Loading…

### _Related_
