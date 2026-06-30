# SWR Series Part 9: Guyton-Klinger Dynamic Withdrawals — earlyretirementnow.com

The number one suggestion from readers for future projects in our [Safe Withdrawal Rate Series](http://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/): look into _dynamic_ withdrawal rates, especially the Guyton-Klinger (GK) withdrawal rate rules. The interest in dynamic rate rules is understandable. Setting one initial withdrawal amount and then stubbornly adjusting it for CPI inflation regardless of what the portfolio does over the next 50-60 years seems wrong (despite the extremely [simple and beautiful withdrawal rate arithmetic](http://earlyretirementnow.com/2017/02/01/the-ultimate-guide-to-safe-withdrawal-rates-part-8-technical-appendix/) we pointed out last week).

So, here we go, our take on the dynamic withdrawal rates. Jonathan Guyton and William Klinger proposed a dynamic strategy that starts out just like the good old static withdrawal rate strategies, namely, setting one initial withdrawal amount and adjusting it for inflation. However, once the withdrawal rate (expressed as current withdrawal rate divided by the current portfolio value) wanders off too far from the target, the investor makes adjustments. Also, notice that this works both ways: You increase your withdrawals if the portfolio appreciated by a certain amount relative to your withdrawals and you decrease your withdrawals if the portfolio is lagging behind significantly. Think of this as **guardrails** on a road; you let the observed withdrawal rates wander off in either direction, for a while at least, but the guardrails prevent the withdrawal rate from wandering off too far, see chart below. It’s all pretty intuitive stuff, though, as we will see later, the devil is in the details.

![swr-part9-chart1](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part9-chart1.png?resize=863%2C475&ssl=1)Guyton-Klinger Guardrails explained: Make the usual CPI adjustments to the withdrawals as long as the proposed withdrawal rate stays within the guardrails. If the withdrawal rate crosses one the guard rails make the necessary adjustment.

The Wall Street Journal calls this methodology “[A Better Way to Tap Your Retirement Savings](https://www.wsj.com/articles/a-better-way-to-tap-your-retirement-savings-1432836119)” because it allows _higher_(!) withdrawal rates than the traditional 4% rule. As you probably know by now, we’re no fans of the 4% rule and if people claim that we can push the envelope even further by just applying some “magic dynamic” we are very suspicious. Specifically, we believe that the GK methodology has (at least) one flaw and we like to showcase it here.

### Guyton-Klinger basics

See a [nice summary here](http://www.finalytiq.co.uk/guyton-klinger-sustainable-withdrawal-rules/) and the [original paper here](http://cornerstonewealthadvisors.com/wp-content/uploads/2014/09/08-06_WebsiteArticle.pdf). An interesting link with lots of calculations, examples and an Excel Spreadsheet with sample calculations is [here](https://jsevy.com/wordpress/index.php/finance-and-retirement/retirement-withdrawal-strategies-guyton-klinger-as-a-happy-medium/). [cFIREsim](http://cfiresim.com/) also simulates the GK method! In any case, the Guyton-Klinger method has four major ingredients, of which three are essential and the fourth seems to be there mostly for “cosmetic” reasons:

  1. Forego the CPI-adjustment in withdrawals when the nominal portfolio return was negative. Even when doing the CPI-adjustment following a positive return, cap it at 6%, which seems somewhat arbitrary to us.
  2. (Guard Rail 1) If the withdrawal rate (current withdrawal amount divided by current portfolio value) is greater than 1.2 times the initial withdrawal rate then cut the withdrawal amount by 10%.
  3. (Guard Rail 2) If the withdrawal rate (current withdrawal amount divided by current portfolio value) is smaller than 0.8 times the initial withdrawal rate then increase the withdrawal amount by 10%.
  4. Some pretty convoluted mumbo-jumbo on the withdrawal mechanics, e.g., which assets to draw down first, a process they call the **Portfolio Management Rule**. To us, this seems like a slightly infantile description of a portfolio rebalance back to target weights, i.e., draw down the assets with the highest returns first because they are the ones with the largest overweights relative to the target weights. Why not just do a simple rebalance to target weights then? There are only two possibilities: a) There is **no gain** from their procedure relative to a plain rebalance, then why do it the complicated way? b) There **is an advantage** relative to a simple rebalance but given the ad-hoc nature of their rules, we would argue that any advantage is likely a fluke. In fact, by GK’s own admission (Table 2 in [their paper](http://cornerstonewealthadvisors.com/wp-content/uploads/2014/09/08-06_WebsiteArticle.pdf)), their portfolio management rule doesn’t add anything when targeting a 90% probability of success and adds only marginally when targeting a 95% probability of success.



### The way we model the dynamic rule is a simplified (decluttered) version of Guyton-Klinger:

  1. Run simulations at a **monthly** frequency, rather than annual, to be consistent with our other research on the topic and, of course, for the plain and simple reason that once we are retired we don’t like a whole year worth of withdrawals sitting around in cash every January. We hate leaving money on the table, as you may know from [our post on emergency funds](http://earlyretirementnow.com/2016/05/05/emergency-fund/).
  2. Since we don’t have all the different equity asset class returns going back to 1871 we simply assume that there is one single equity index (U.S. Large Cap) and one single bond asset (10-year Benchmark U.S. Treasury Bond) as in our previous research, again consistent with our earlier research based on a simple Stock-Bond portfolio
  3. We discard GK’s convoluted portfolio management rule. We have only two assets (stocks and bonds) and simply assume that the portfolio is rebalanced back to the target weights every month. It’s simpler to model and calculate in our number-crunching software: a simple matrix algebra operation, i.e., we multiply the Tx2 matrix of stock/bond returns with a 2×1 vector of asset weights. Done! No need to carry around time-varying portfolio weights.
  4. If the 12-month trailing (real) return was negative, then forego the inflation adjustment, i.e., shrink the real withdrawal by the CPI-rate that month. If the 12-month trailing return was positive, then do the CPI-adjustment. We don’t use the Guyton-Klinger 6% cap on the CPI-adjustment, which seems pretty arbitrary and also causes a big loss of purchasing power in the 1970s.
  5. If the withdrawal rate (current withdrawal amount divided by current portfolio value) is greater than (1+g) times the initial withdrawal rate then cut the withdrawal amount by x. It’s the same setup as in Guyton-Klinger.
  6. If the withdrawal rate (current withdrawal amount divided by current portfolio value) is smaller than (1-g) times the initial withdrawal rate then increase the withdrawal amount by x. Again, the same as in Guyton-Klinger.



Our take on Guyton-Klinger captures the main ingredients: the guardrails and a decision rule for making vs. skipping the CPI-adjustments, without the baggage of their complicated and likely useless portfolio management rule.

### Results

Let’s start with the **good news**. The number one reason we like the GK-rule: If done right it’s (almost) impossible to run out of money with the GK rule (in very stark contrast to the non-trivial probabilities of depleting the portfolio under the naive static withdrawal rule, see [our previous research](http://earlyretirementnow.com/2016/12/14/the-ultimate-guide-to-safe-withdrawal-rates-part-2-capital-preservation-vs-capital-depletion/)). You heard that right! Our simulations show that if we set the initial withdrawal not too crazy high and we use a tight enough guard rail parameter (g=20%) and aggressive enough adjustment parameter (x=10%) then even under adverse market conditions (e.g., the January 1966 retirement cohort) we won’t run out of money. _(side note: this requires to do the guardrail adjustments throughout retirement, while GK stop doing the adjustments 15 years before the end of the retirement horizon, in which case you do face the risk of running out of money)_

Now for the bad news. We identified one reason to be skeptical, very skeptical, about the Guyton-Klinger rule:

### Under Guyton-Klinger you may have to curb your consumption. **By a lot more than you think!**

Let’s make this more fun and let me first present the GK simulation results in a very deceptive way to make the dynamic GK rules appear much better than they really are. Let’s see who can spot the deception…

Let’s present a **1966 case study** , the last time in recent history when the 4% rule failed (though you may remember [our 2000-2016 case study](http://earlyretirementnow.com/2017/01/18/the-ultimate-guide-to-safe-withdrawal-rates-part-6-a-2000-2016-case-study/), where we showed that the 4% rule also looks pretty shaky for the January 2000 retirement cohort). If Guyton-Klinger can succeed here it will succeed almost anywhere! Throughout, we assume an 80%/20% Stock/Bond portfolio and the same return assumptions as outlined [in part 1 of this series](http://earlyretirementnow.com/2016/12/07/the-ultimate-guide-to-safe-withdrawal-rates-part-1-intro/). We consider 4 different withdrawal strategies:

  1. The good old 4% rule: set the initial monthly withdrawal rate to 0.333% (=4% p.a.) and then adjust the withdrawals by CPI regardless of the portfolio performance. This method depletes the portfolio after 28 years.
  2. Guyton-Klinger with +/-20% guardrails and 10% adjustments and a 4% p.a. initial withdrawal rate
  3. Same as 2, but with a 5% initial withdrawal rate
  4. Same as 2, but with a 6% (!) initial withdrawal rate



The time series chart of the real, CPI-adjusted portfolio value (normalized to 100 in January 1966) is below:

![swr-part9-chart2](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part9-chart2.png?resize=863%2C545&ssl=1)Portfolio values (adjusted for CPI) of the January 1966 retirement cohort: Static 4% rule vs. Guyton-Klinger Dynamic rules (20%/10%), 80%/20% S/B portfolios, rebalanced monthly.

Holy Mackerel!!! GK beats the 4% rule and it’s not even close. The GK-4% has surpassed the initial $100 (adjusted for CPI!) after 26 years while the old 4% has gone bankrupt after 28 years. The 5% rule is almost back to normal and the 6% rule is hanging in there pretty well, too. Talking about withdrawal percentages, let’s look at those as well, see picture below:

![swr-part9-chart4](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part9-chart4.png?resize=863%2C543&ssl=1)Withdrawal rates of the January 1966 retirement cohort: Static 4% rule vs. Guyton-Klinger Dynamic rules (20%/10%), 80%/20% S/B portfolios, rebalanced monthly.

Amazing! Look at the 5% Guyton-Klinger rule. By construction, it stays between 4% and 6% (=5% times 1+0.2 and 1-0.2, respectively), so it never falls below 4% due to the guardrails. Moreover, it has a higher initial withdrawal and a higher final value! It appears to beat the static 4% withdrawal rate in _every_ dimension we care about. It looks like the occasional 10% cuts in withdrawals haven’t hurt us too much. Amazing! Have we just found a Safe Withdrawal Rate Nirvana? Let’s nominate Guyton and Klinger for the Nobel Prize! Economics or Peace? Heck, both, of course, and in the same year to save them the travel expenses to Stockholm!

But before you open the champagne bottles, let’s bring us all back to planet earth. **I just scammed you all!** To be sure, the numbers are 100% correct, but the way I presented them was false advertising, even borderline fraudulent.

**Where was the deception I mentioned above?**

Pay close attention to what I **didn’t show** you yet! I never showed you the actual inflation-adjusted withdrawal **amounts**. Who cares about **percentages** of the portfolio value when the portfolio value is a moving target? I want to know the **dollar amounts**. It’s called “Show me the **money** ” and not “Show me the **percentages** ,” after all. So, how much in CPI-adjusted dollars can I withdraw under the different rules and, specifically, by how much do I have to curb my consumption during retirement due to the withdrawal cuts once we hit the guard rails? That’s displayed in the chart below:

![swr-part9-chart3](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2017/02/swr-part9-chart3.png?resize=863%2C549&ssl=1)Real withdrawal values (per $100 of initial portfolio value) of the January 1966 retirement cohort: Static 4% rule vs. Guyton-Klinger Dynamic rules (20%/10%), 80%/20% S/B portfolios, rebalanced monthly.

What a disappointment! That’s where the Guyton-Klinger skeletons are hidden. Sure, when your initial withdrawal rate is 5% you never drop below a 4% withdrawal _rate_ (due to the guardrail), but it’s 4% of a much-depleted portfolio value, not 4% of the _initial value_. That subtle distinction makes a huge difference. For example, the average withdrawal values for GK under the 4/5/6% initial withdrawal rates are only 2.74%, 3.02%, and 3.22% of the initial portfolio value, respectively. Well, it’s no longer a surprise that we have a higher final value than under the static 4% rule because we withdrew so much less! The advertised 5% withdrawal was only 3.02% withdrawal. What a scam!

Talking about skeletons, here’s more data from the GK horror show: The decline of withdrawals from peak to bottom is a staggering 59%, 66%, and 69%, respectively. Ouch! If you thought that the $1,000,000 portfolio can afford you a $50,000 per year lifestyle using GK, you better plan for a few sub-$20k years and an entire decade (!) of sub-$25k p.a. withdrawals. Suddenly the Guyton-Klinger method doesn’t look so hot anymore.

How is it possible to experience such massive declines in the withdrawals? The GK-rules hide this drop behind the +/-20% guardrails and +/-10% withdrawal adjustments (not to mention the distraction in the form of the asinine “portfolio management rule”) that make it sound like we only suffer relatively minor and temporary decreases in purchasing power. But the 0.2 guardrail is **on top of the drop in the portfolio**. If the portfolio is down by 50% and you hit the lower guardrail, the drop in the withdrawal is (1-0.5)x(1-0.2)=0.4 = 60% under the initial withdrawal. Hence, the large reduction in withdrawals! Skipping the CPI-adjustment in some of the years also erodes the purchasing power.

The claim that we can afford a higher initial withdrawal rate than under the fixed withdrawal rules is a pretty blatant case of false advertising. In fact, this claim has about the same ring to it as the good old “You can afford that big McMansion” or “You can afford that suped-up brand new car.” A 5% initial withdrawal rate may seem nice in the beginning but reality will catch up eventually. The higher you set the initial withdrawal rate the more of a drop in your consumption pattern you might suffer if the market doesn’t cooperate.

### Conclusion

We actually have a lot more material and have to defer all of that to a future post. We’re already past 2,000 words and have only scratched the surface. We prepared another case study (the dreaded January 2000 retirement cohort), more comprehensive historical simulations (including the likelihood of a significant long-lasting drop in purchasing power for different CAPE regimes), and like to show several other smaller flaws in the GK methodology. Probably next week!

To wrap up today’s post, the initial question was: Is the Guyton-Klinger method overrated? False advertising sounds more appropriate. The GK-type rules seem to imply that they can offer higher initial withdrawal rates and better long-term success rates. True, but all that comes at the cost of potentially **massive** reductions in withdrawals (50%+ below the initial).

Oh well, what did we all expect? The GK rules can’t square the circle by offering higher withdrawal rates and lower failure rates. If we wanted to be sarcastic, we’d point out that GK won’t cure athletes’ feet, either. If you want to use GK yourself, make sure you’re aware of the downside (literally!), i.e., be prepared to curb consumption by 50% if things don’t work out. And that’s not just for a year or two, but potentially for a decade or more! That may be doable if your initial withdrawal is $80k or $100k and there is enough downside cushion. But for the folks with a tighter budget, GK would imply a significant probability of returning to work during early retirement!

**Update (2/20/2024):**

A reader pointed out in the [comments section](https://earlyretirementnow.com/2017/02/08/the-ultimate-guide-to-safe-withdrawal-rates-part-9-guyton-klinger/comment-page-2/#comment-33058) that you would have gotten different results if you didn’t adjust as rapidly downward (10%) but instead transformed the 10% GK adjustment to a monthly value of 1.10^(1/12)=0.00797=0.797%. Does that change anything in this case study? Would this change make the GK simulations look more appealing? No. It’s like squeezing a balloon. You will indeed soften the drop in withdrawal amounts. You will undoubtedly lower the volatility of monthly withdrawal changes. But because you delay the inevitable and necessary fall in consumption, you also create some new headaches!

In the two charts below, I present you the withdrawal amounts (for a $100 initial portfolio). I use the same scale for easier comparison. True, because of the rapid triggering of the GK rule, the fall is very swift in the baseline simulation (top) and more gradual in the new method (bottom). But I also noticed that because the withdrawal cut under the new method was less reactive, the portfolio depletion was worse, and thus, the withdrawal cut lasted a few years longer. And the eventual recovery in withdrawals was also slower. So, there is no escaping the mathematical realities of Sequence Risk when using this more gradual GK adjustment parameter. The trough consumption level is about the same using the new method. Shockingly, the volatility of retirement withdrawal levels would have been higher (worse) than in the baseline for the 5% and 6% GK rule. That’s because the spending trough lasted longer, and the recovery was more gradual. 

![](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2024/02/SWR-Part9-Chart6.png?resize=863%2C628&ssl=1)Real withdrawal values (per $100 of initial portfolio value) of the January 1966 retirement cohort: Static 4% rule vs. Guyton-Klinger Dynamic rules (20%/10%), 80%/20% S/B portfolios, rebalances monthly. **GK step = 10.00% monthly** (=my initial assumption)

![](https://i0.wp.com/earlyretirementnow.com/wp-content/uploads/2024/02/SWR-Part9-Chart5.png?resize=863%2C620&ssl=1)Real withdrawal values (per $100 of initial portfolio value) of the January 1966 retirement cohort: Static 4% rule vs. Guyton-Klinger Dynamic rules (20%/10%), 80%/20% S/B portfolios, rebalances monthly. **GK step = 0.797% monthly** (=10% p.a. transformed to monthly, i.e., 1.1^(1/12)-1=0.00797=0.797%, as suggested by a commenter)

The volatility of annualized spending levels over the 30-year retirement, assuming a $1,000,000 initial portfolio (rounded to the closest $100):

  * Baseline: $7,600, $9,600, 12,200 for GK 4%, 5%, 6%.
  * New method with gradual GK adjustments: $7300, $10,400, $14,400 for GK 4%, 5%, 6%.



### Thanks for stopping by today! Please leave your comments and suggestions below! Also, make sure you check out the other parts of the series, see [here for a guide to the different parts so far](https://earlyretirementnow.com/safe-withdrawal-rate-series/)!

### Share this:

  * [ Share on X (Opens in new window) X ](https://earlyretirementnow.com/2017/02/08/the-ultimate-guide-to-safe-withdrawal-rates-part-9-guyton-klinger/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://earlyretirementnow.com/2017/02/08/the-ultimate-guide-to-safe-withdrawal-rates-part-9-guyton-klinger/?share=facebook)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://earlyretirementnow.com/2017/02/08/the-ultimate-guide-to-safe-withdrawal-rates-part-9-guyton-klinger/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://earlyretirementnow.com/2017/02/08/the-ultimate-guide-to-safe-withdrawal-rates-part-9-guyton-klinger/?share=reddit)
  * 


### Like this:

Like Loading…

### _Related_
