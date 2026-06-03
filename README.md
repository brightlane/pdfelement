# PDFToolGuide — PDFelement Affiliate Site

> 20-page static affiliate site promoting Wondershare PDFelement.
> Live at: **https://brightlane.github.io/pdfelement/**
> Affiliate URL: `https://www.linkconnector.com/ta.php?lc=007949093934004532&atid=WondersharePDFelementWeb`
> Target: Global audience

---

## Quick Start

```bash
git clone https://github.com/brightlane/pdfelement.git
cd pdfelement
python3 build.py
```

Push to `main` — GitHub Actions deploys automatically.

---

## Repo Structure

```
pdfelement/
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## Pages (20)

| Page | File | Target Keywords |
|------|------|-----------------|
| Homepage | index.html | pdfelement pdf editor |
| Review | pdfelement-review.html | pdfelement review 2026 |
| vs Adobe Acrobat | pdfelement-vs-adobe.html | pdfelement vs adobe acrobat |
| vs Foxit | pdfelement-vs-foxit.html | pdfelement vs foxit |
| Pricing | pdfelement-pricing.html | pdfelement pricing 2026 |
| Edit PDF | edit-pdf.html | how to edit pdf |
| Convert PDF | convert-pdf.html | convert pdf to word |
| Sign PDF | sign-pdf.html | how to sign pdf |
| Compress PDF | compress-pdf.html | compress pdf file |
| PDF Forms | pdf-forms.html | create pdf forms |
| PDF OCR | pdf-ocr.html | pdf ocr software |
| Business | pdf-for-business.html | pdf editor for business |
| Students | pdf-for-students.html | pdf editor for students |
| Mac Guide | pdfelement-mac.html | pdfelement for mac |
| Windows Guide | pdfelement-windows.html | pdfelement for windows |
| AI Tools | pdf-ai-tools.html | pdf ai tools 2026 |
| Merge & Split | merge-split-pdf.html | merge pdf files |
| Protect PDF | protect-pdf.html | password protect pdf |
| Promo Codes | promo-codes.html | pdfelement promo codes |
| About | about.html | about pdftoolguide |

---

## GitHub Pages Setup

1. Create repo `brightlane/pdfelement` on GitHub
2. Add `build.py` to repo root
3. Add `.github/workflows/deploy.yml`
4. Go to **Settings → Pages → Source → GitHub Actions**
5. Push to `main`
6. Live at `https://brightlane.github.io/pdfelement/`

---

## Customisation

### Update affiliate URL
```python
AFF = "https://www.linkconnector.com/ta.php?lc=007949093934004532&atid=WondersharePDFelementWeb"
```

### Update live URL
```python
BASE = "https://brightlane.github.io/pdfelement"
SUB  = "/pdfelement"
```

### Add a new how-to page
Use the `how_to_page()` helper:
```python
def page_yourguide():
    steps = [
        ("Step Title", "Step description text"),
        ...
    ]
    return how_to_page("Section Title", "Badge Text", "H1 Title", "Sub text", steps)
```

---

## Why This Site Makes Money

- **High buyer intent keywords** — "how to edit PDF", "convert PDF to Word", "PDF editor vs Adobe" are searched millions of times monthly by people actively looking for software
- **Global audience** — PDF editing is a universal need across every country and profession
- **Strong comparison pages** — vs Adobe Acrobat and vs Foxit capture users in purchase decision mode
- **Pricing page** — users searching for pricing are the closest to buying
- **15+ how-to pages** — long-tail keywords at high volume drive organic traffic
- **Perpetual license angle** — PDFelement's one-time purchase option is a compelling differentiator that converts well

---

## Tech Stack

- Python 3.8+ — zero external dependencies
- Static HTML/CSS — no JS frameworks
- Google Fonts — Outfit + Plus Jakarta Sans
- GitHub Pages — free hosting, auto-deploy

---

## Affiliate Disclosure

PDFToolGuide is an independent affiliate partner of Wondershare.
Not operated by Wondershare or PDFelement.

## License
MIT
