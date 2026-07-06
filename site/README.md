# joshkrilov.com — v3.0 (bright + automated intake)

Single-file static site. One dependency (Google Fonts: Fraunces). Deploys anywhere.

## Deploy checklist

1. **Domain** — buy joshkrilov.com at Cloudflare Registrar or Porkbun (~$10/yr).
2. **Host** — deploy to **Netlify** (drag the `site/` folder onto https://app.netlify.com/drop). Netlify specifically, because the intake form uses Netlify Forms — zero backend needed.
3. **DNS** — add your custom domain in Netlify; copy its two DNS records into your registrar.
4. **Forms** — the intake form (`name="intake"`) is auto-detected by Netlify on deploy. In Netlify: Site settings → Forms → add an email notification to krilov@gmail.com. Then add the attribute `data-live` to the `<form id="intake-form">` tag so it posts for real instead of demo mode. (On Vercel instead: swap the form action to a free Formspree endpoint — instructions in the HTML comment above the form.)
5. **Analytics** — paste a Plausible or GoatCounter script line before `</body>`. Skip Google Analytics for v1.

## How the intake automation works

- Visitor picks a path: **Train my team** / **Free workshop** / **Not sure**.
- Each path asks only what Josh needs to qualify and reply asynchronously:
  - Training: org, size, pain point, and a **budget acknowledgment checkbox** ($4,500 / $3,000 nonprofit) — self-qualifies before you spend a minute.
  - Workshop: audience size, timing, and a required **multi-org checkbox** (enforces the free-only-for-multi-org-rooms rule).
  - Not sure: email capture for the full AI Opportunity Scorecard.
- Submissions land in Netlify Forms → email notification → Josh replies with a plan/proposal on his own schedule. No live calls.

## Scorecard delivery

The full AI Opportunity Scorecard is in `scorecard.html`. When someone chooses "Not sure yet" and submits their email, Josh should reply with this link (or a PDF version):

- **For email delivery:** Save `scorecard.html` as a PDF (Ctrl+P / Cmd+P in browser, "Save as PDF"), then attach to the reply. Or use a free HTML-to-PDF tool (e.g., pdfcrowd.com, convertio.co) to automate.
- **For link delivery:** Upload `scorecard.html` somewhere publicly accessible and email a direct link (e.g., `joshkrilov.com/scorecard/`).

The scorecard is department-by-department (marketing, ops, programs, fundraising, leadership) with scoring guidance, first-90-days roadmaps, and interpretation rules. It's sized to print on A4/letter.

## Placeholders to swap

- Add `data-live` to the intake `<form>` after wiring Netlify/Formspree (until then it runs in demo mode)
- Footer LinkedIn URL
