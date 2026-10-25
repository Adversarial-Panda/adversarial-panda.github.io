# DES-Adv paper website

Paper project page for **One Ensemble Does Not Fit All: Rethinking Query-Free Attacks on Web Vision Services**.

Live URL: https://adversarial-panda.github.io/

Static HTML, CSS, and JavaScript; no build dependencies. Open `index.html` locally or run `python3 -m http.server 8000`.

## Content

- `index.html`: paper text, summary, method, results, and resource links.
- `style.css`: responsive layout and typography.
- `script.js`: accessible figure enlargement, with direct image links as fallback.
- `assets/`: optimized figures, favicon, and the supplied paper PDF.

The supplied manuscript lists anonymous authors. Replace that attribution when a public author list is ready. No conference acceptance, code release, DOI, or author details are assumed.

## Deployment

GitHub Pages deploys from `main` via `.github/workflows/pages.yml`. Set the repository Pages source to **GitHub Actions**. The workflow packages only the public website assets. Push changes to `main` to update the website.

The visual structure is inspired by https://crossdomain-ensembles.epfl.ch/; the implementation is original.
