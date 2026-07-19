# joshkrilov.com — v4.0 (simple one-pager)

Single-file static site. One dependency (Google Fonts: Roboto). Deploys anywhere.

Built to rank for **"AI trainer New Orleans"** and **"AI consultant New Orleans"**:
keyword-targeted title/meta/H1, ProfessionalService + FAQPage structured data,
and New Orleans mentioned naturally throughout the copy.

## Deploy checklist

1. **Domain** — buy joshkrilov.com at Cloudflare Registrar or Porkbun (~$10/yr).
2. **Host** — deploy to **Netlify** (drag the `site/` folder onto https://app.netlify.com/drop). Netlify specifically, because the contact form uses Netlify Forms — zero backend needed.
3. **DNS** — add your custom domain in Netlify; copy its two DNS records into your registrar.
4. **Forms** — the contact form (`name="contact"`) is auto-detected by Netlify on deploy. In Netlify: Site settings → Forms → add an email notification to krilov@gmail.com. Then add the attribute `data-live` to the `<form id="contact-form">` tag so it posts for real instead of demo mode. (On Vercel instead: swap the form action to a free Formspree endpoint — instructions in the HTML comment above the form.)
5. **Google** — set up Google Search Console for joshkrilov.com and submit the URL, and create a free **Google Business Profile** (category: "Consultant" / "Training provider", city: New Orleans). For local queries like "AI consultant New Orleans," the Business Profile matters as much as the site itself.
6. **Analytics** — paste a Plausible or GoatCounter script line before `</body>`. Skip Google Analytics for v1.

## Placeholders to swap

- Add `data-live` to the contact `<form>` after wiring Netlify/Formspree (until then it runs in demo mode)
- Footer LinkedIn URL

## Also in this folder

`scorecard.html` — the full AI Opportunity Scorecard from a previous version.
No longer linked from the homepage; keep it as a lead-magnet PDF/link to send
by email if useful.
