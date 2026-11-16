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

The public GIFs and still previews have baked-in blurring over terminal account names, matching home-directory usernames, window titles, and tabs. The local source MP4s remain unredacted and excluded from deployment. `tools/redact_demos.py` documents the redaction process; run it only on original GIFs, with Pillow, NumPy, and SciPy installed.

## Web vision video demonstrations

The demonstration section follows the framework figure and precedes Overview. Google Cloud Vision is split at 14 seconds; Gemini is split at 17 seconds. In each source, the first segment shows the benign input and the second shows its adversarial counterpart. Four H.264 MP4 clips with native playback/fullscreen controls and static posters accompany the two redacted terminal animations. The full uploaded source recordings remain local and are excluded from Git. Body text uses improved line wrapping and headings use balanced wrapping.

The four web vision demos now display as looping GIFs at original speed (960 pixels wide, 10 fps), with click-to-enlarge and the shared stop/play control. Reduced-motion mode uses their static posters. The MP4 clips are retained as source assets.
