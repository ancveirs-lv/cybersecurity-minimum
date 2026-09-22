# Cybersecurity Minimum

[Latviski](README.lv.md) · **English**

**25 practical rules for protecting accounts, devices, data and money.**

This is a public-interest cybersecurity baseline for everyday digital life. The **English edition is global**: it does not assume Latvian institutions, law or services. The Latvian edition keeps the same control IDs but localises selected implementation details, including CERT.LV incident reporting and the CERT.LV/NIC.LV DNS firewall.

> **Universal principle:** do not let other people control where you sign in, what you install, or where your money goes.

## Universal decision algorithm

`STOP → verify the source → open the official service yourself → verify through another channel → only then act`

## The 25-rule baseline

### 01–06 · Think before you act

- 01. Start important actions yourself.
- 02. Verify the payment recipient.
- 03. Urgency means pause.
- 04. Verify unusual requests another way.
- 05. A message does not prove who sent it.
- 06. When in doubt, verify first.

### 07–14 · Protect accounts

- 07. Never share passwords, PINs or verification codes.
- 08. Use a unique password for every account.
- 09. Use a long passphrase or generated password.
- 10. Store passwords safely.
- 11. Use passkeys or multi-factor authentication.
- 12. Protect your primary email account.
- 13. Review important account security settings.
- 14. Remove old devices and unnecessary access.

### 15–20 · Protect devices and networks

- 15. Lock phones and computers.
- 16. Keep devices and software updated.
- 17. Keep built-in protection enabled.
- 18. Secure home Wi-Fi and the router.
- 19. Make backups you can restore.
- 20. Consider protective DNS or equivalent network filtering.

### 21–24 · Recognise fraud

- 21. Treat unexpected attachments and QR codes with caution.
- 22. Do not install remote-access software because a stranger tells you to.
- 23. Polished design is not proof of trust.
- 24. Be cautious with too-good-to-be-true offers and emotional stories.

### 25 · Know what to do

- 25. Report and respond quickly.

Full explanations are in [the global English guide](docs/en/cybersecurity-minimum.md).

## Localisation model

`global control ID → global guidance → local implementation note`

EN and LV keep the same 25 control IDs. Local details may differ where the responsible institution, reporting path or protective service is jurisdiction-specific. The project does **not** pretend that a Latvian service is a global recommendation.

## Evidence model

`source → control → localised guidance → validation`

The machine-readable rules live in `data/minimum.en.json` and `data/minimum.lv.json`; sources are registered in `data/sources.json`. CI verifies ID parity, source references and localisation boundaries.

## Sources

The global baseline uses ENISA, CISA, UK NCSC and NIST. The Latvian localisation additionally uses CERT.LV for local reporting and protective-DNS guidance.

## Scope

This is practical public guidance, not a substitute for an organisation-specific security programme, incident-response plan, legal advice or sector regulation.

## Author

**Zigmārs Ancveirs** — technology leader, software engineer and independent cybersecurity researcher.

## Licence

Documentation and data: **CC BY 4.0**. Code and automation: **MIT**. See [LICENSE.md](LICENSE.md).
