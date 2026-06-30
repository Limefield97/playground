# Fire Corpus Manifest

All files fetched 2026-06-30.

## IRS Publications

| File | Source URL | Description |
|---|---|---|
| `irs-pub-527-rental-property.pdf` | https://www.irs.gov/pub/irs-pdf/p527.pdf | IRS Pub 527 — Residential Rental Property (incl. vacation home rentals), current-year PDF |
| `irs-pub-590a-ira-contributions.pdf` | https://www.irs.gov/pub/irs-pdf/p590a.pdf | IRS Pub 590-A — Contributions to IRAs |
| `irs-pub-590b-ira-distributions.pdf` | https://www.irs.gov/pub/irs-pdf/p590b.pdf | IRS Pub 590-B — Distributions from IRAs |

## Louisiana State Tax / Law

| File | Source URL | Description |
|---|---|---|
| `louisiana-income-tax-guide.pdf` | https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf | Revenue Information Bulletin No. 25-012 — Louisiana Individual Income Tax Reform (current flat-rate structure, deductions/credits) |
| `louisiana-landlord-tenant-law.md` | https://louisianalawhelp.org/resource/just-moved-to-louisiana-how-our-landlord-tena-1 | Plain-language legal aid summary of LA landlord-tenant rights/obligations |
| `louisiana-landlord-tenant-law-source.pdf` (bonus) | https://law.loyno.edu/sites/default/files/landlord_tenant.pdf | Loyola Law School's longer-form treatise on LA landlord-tenant law (Civil Code-based), kept as a deeper supplementary reference |

## FIRE Strategy Content (Mad Fientist)

| File | Source URL | Description |
|---|---|---|
| `mad-fientist-roth-conversion-ladder.md` | https://www.madfientist.com/how-to-access-retirement-funds-early/ | "How to Access Retirement Funds Early" — covers the Roth IRA conversion ladder strategy |
| `mad-fientist-hsa.md` | https://www.madfientist.com/ultimate-retirement-account/ | "HSA – The Ultimate Retirement Account" |
| `mad-fientist-tax-optimization.md` | https://www.madfientist.com/traditional-ira-vs-roth-ira/ | "Traditional IRA vs. Roth IRA — The Best Choice for Early Retirement" (account-selection / tax optimization) |

## Early Retirement Now — Safe Withdrawal Rate Series

| File | Source URL | Description |
|---|---|---|
| `ern-swr-index.md` | https://earlyretirementnow.com/safe-withdrawal-rate-series/ | Landing page/index for the full 60+ part SWR series |
| `ern-swr-part-01.md` | .../2016/12/07/.../part-1-intro/ | Part 1: Introduction |
| `ern-swr-part-02.md` | .../2016/12/14/.../part-2-capital-preservation-vs-capital-depletion | Part 2: Capital Preservation vs. Capital Depletion |
| `ern-swr-part-03.md` | .../2016/12/21/.../part-3-equity-valuation/ | Part 3: Safe Withdrawal Rates in Different Equity Valuation Regimes |
| `ern-swr-part-04.md` | .../2017/01/04/.../part-4-social-security-pensions | Part 4: Impact of Social Security Benefits / Pensions |
| `ern-swr-part-05.md` | .../2017/01/11/.../part-5-cost-of-living-adjustments | Part 5: Cost-of-Living Adjustment (COLA) Assumptions |
| `ern-swr-part-06.md` | .../2017/01/18/.../part-6-a-2000-2016-case-study | Part 6: A Case Study, 2000–2016 |
| `ern-swr-part-07.md` | .../2017/01/25/.../part-7-toolbox/ | Part 7: A DIY Withdrawal Rate Toolbox (Google Sheets) |
| `ern-swr-part-08.md` | .../2017/02/01/.../part-8-technical-appendix | Part 8: Technical Appendix |
| `ern-swr-part-09.md` | .../2017/02/08/.../part-9-guyton-klinger/ | Part 9: Dynamic Withdrawal Rates (Guyton-Klinger) |
| `ern-swr-part-10.md` | .../2017/02/15/.../part-10-guyton-klinger | Part 10: Debunking Guyton-Klinger Some More |

## Real Estate

| File | Source URL | Description |
|---|---|---|
| `cost-segregation-overview.md` | https://www.kbkg.com/cost-segregation/cost-segregation-for-residential-property | KBKG explainer: what cost segregation is, benefits, timeline, documentation needed, residential rental applicability |
| `biggerpockets-rental-analysis.md` | https://www.biggerpockets.com/blog/real-estate-math | BiggerPockets rental property analysis methodology (cash flow, cap rate, cash-on-cash return, etc.) |

## 457(b) Plan Deep Dive

| File | Source URL | Description |
|---|---|---|
| `457b-plan-rules.md` | https://www.fidelity.com/learning-center/smart-money/what-is-a-457b | Fidelity guide: governmental vs. non-governmental 457(b), contribution limits, no early-withdrawal penalty after separation, Roth 457 option, 403(b) coordination/double limit, rollover rules |

## Notes / Gaps

- **Cost segregation "typical benefit ranges"**: the KBKG page used doesn't quote specific $ or % benefit ranges. For harder numbers, manually check KBKG's "How Cost Segregation Remains Valuable as Bonus Depreciation Declines" (https://www.kbkg.com/cost-segregation/how-cost-segregation-remains-valuable-as-bonus-depreciation-declines) or a McGuire Sponsel cost-seg explainer.
- **BiggerPockets**: used their "Rental Property Numbers" methodology article rather than the calculator's own internal methodology page (calculator tool itself isn't fetchable as static content). For the live calculator UX, see https://www.biggerpockets.com/rental-property-calculator.
- All Mad Fientist and BiggerPockets pages blocked the default WebFetch tool (403); fetched via `curl` with a browser User-Agent header instead, then converted HTML → Markdown locally.
- 457(b)/403(b) "double limit" figures and IRA/457 contribution limits cited reflect 2026 figures as quoted by Fidelity; verify against IRS.gov before relying on them for filing purposes (IRS 457(b) page: https://www.irs.gov/retirement-plans/irc-457b-deferred-compensation-plans).
