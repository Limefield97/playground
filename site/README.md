# joshkrilov.com — v2.0 (editorial redesign)

Single-file static site. No build step, no dependencies. Deploy the `site/` folder anywhere.

## Deploy checklist (today)

1. **Domain** — buy joshkrilov.com (or chosen name) at Cloudflare Registrar or Porkbun (~$10/yr, no upsells).
2. **Host** — drag the `site/` folder onto https://app.netlify.com/drop (or `vercel deploy site/`). Live URL in ~30 seconds.
3. **DNS** — in Netlify/Vercel, add your custom domain; copy the two DNS records they give you into your registrar. Propagates in minutes–hours.
4. **Forms** — create a ConvertKit (free tier) form for the cheat sheet; replace `PLACEHOLDER_FORM_ACTION` in `index.html` (search for it — the swap instructions are in a comment right above the form). Replace `YOUR-CALENDLY-USERNAME` with your Calendly link (also marked with a SWAP comment).
5. **Analytics** — add one line before `</body>`: Plausible or GoatCounter script tag (both free-ish, no cookie banner needed). Skip Google Analytics for v1.

## Placeholders to swap (search `index.html` for these)

- `PLACEHOLDER_FORM_ACTION` — email provider form action
- `YOUR-CALENDLY-USERNAME` — Calendly booking link
- Footer LinkedIn URL — currently points at linkedin.com root
