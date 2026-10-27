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

## CAPTCHA demonstration GIFs

The benign and adversarial GIFs in `assets/` use the first 60 seconds of the supplied recordings at 2× speed. Each loops over 30 seconds at 800 × 450 pixels and 10 fps. The original MP4 recordings remain local and are excluded from Git. The page includes a stop/play control and starts with still images when reduced motion is preferred.
