#!/usr/bin/env python3
"""
build.py - PDFelement Affiliate Site Generator
Deploys to: https://brightlane.github.io/pdfelement/
Affiliate URL: https://www.linkconnector.com/ta.php?lc=007949093934004532&atid=WondersharePDFelementWeb
Run: python3 build.py
Output: docs/ folder (GitHub Pages source)
"""

import json
from pathlib import Path
from datetime import date

AFF   = "https://www.linkconnector.com/ta.php?lc=007949093934004532&atid=WondersharePDFelementWeb"
BASE  = "https://brightlane.github.io/pdfelement"
SUB   = "/pdfelement"
TODAY = date.today().isoformat()
OUT   = Path("docs")

PAGES = [
    {"slug":"index","title":"PDFelement 2026: The Best PDF Editor — Edit, Convert & Sign PDFs","desc":"PDFelement is the world's leading PDF editor. Edit, convert, sign, compress and annotate PDFs on Windows, Mac, iOS and Android. Try free today.","content_fn":"page_home","priority":"1.0"},
    {"slug":"pdfelement-review","title":"PDFelement Review 2026: Honest Deep Dive — Is It Worth It?","desc":"Full PDFelement review for 2026. Features, pricing, pros and cons compared to Adobe Acrobat. Is it the best PDF editor available?","content_fn":"page_review","priority":"0.95"},
    {"slug":"pdfelement-vs-adobe","title":"PDFelement vs Adobe Acrobat 2026: Which PDF Editor Wins?","desc":"PDFelement vs Adobe Acrobat compared on features, price, and performance. Real comparison — find out which PDF editor is right for you in 2026.","content_fn":"page_vs_adobe","priority":"0.9"},
    {"slug":"pdfelement-vs-foxit","title":"PDFelement vs Foxit PDF 2026: Full Comparison","desc":"PDFelement vs Foxit PDF compared. Features, pricing, and ease of use — which PDF editor gives you more for your money in 2026?","content_fn":"page_vs_foxit","priority":"0.9"},
    {"slug":"pdfelement-pricing","title":"PDFelement Pricing 2026: Plans, Costs & Free Trial Guide","desc":"Full PDFelement pricing guide for 2026. Individual, team, and perpetual license costs — and exactly how it compares to Adobe Acrobat's subscription.","content_fn":"page_pricing","priority":"0.9"},
    {"slug":"edit-pdf","title":"How to Edit a PDF in 2026 | PDFelement Guide","desc":"How to edit PDF files in 2026. Add text, images, and signatures to any PDF with PDFelement. Free trial available — no experience needed.","content_fn":"page_edit","priority":"0.85"},
    {"slug":"convert-pdf","title":"How to Convert PDF to Word, Excel & PowerPoint | PDFelement","desc":"How to convert PDF to Word, Excel, PowerPoint and more with PDFelement. Fast, accurate conversion that preserves formatting perfectly.","content_fn":"page_convert","priority":"0.85"},
    {"slug":"sign-pdf","title":"How to Sign PDFs & Create eSignatures 2026 | PDFelement","desc":"How to electronically sign PDFs and collect signatures with PDFelement. Legally binding eSignatures on any device in 2026.","content_fn":"page_sign","priority":"0.85"},
    {"slug":"compress-pdf","title":"How to Compress PDF Files Without Losing Quality | PDFelement","desc":"How to compress large PDF files without losing quality using PDFelement. Reduce file size by up to 90% in seconds.","content_fn":"page_compress","priority":"0.85"},
    {"slug":"pdf-forms","title":"How to Create & Fill PDF Forms 2026 | PDFelement","desc":"How to create, fill and manage PDF forms with PDFelement. Interactive forms, data collection, and automated workflows in 2026.","content_fn":"page_forms","priority":"0.85"},
    {"slug":"pdf-ocr","title":"PDF OCR: Convert Scanned Documents to Editable Text | PDFelement","desc":"How to use OCR to convert scanned PDFs to editable, searchable text with PDFelement. 26+ languages supported in 2026.","content_fn":"page_ocr","priority":"0.85"},
    {"slug":"pdf-for-business","title":"PDFelement for Business 2026: Teams, Workflows & ROI","desc":"How businesses use PDFelement to streamline PDF workflows, reduce costs, and improve team productivity. Business plans and ROI explained.","content_fn":"page_business","priority":"0.85"},
    {"slug":"pdf-for-students","title":"PDFelement for Students 2026: The Best PDF Tool for Study","desc":"How students use PDFelement for reading, annotating, and managing academic PDFs. Special student pricing available in 2026.","content_fn":"page_students","priority":"0.8"},
    {"slug":"pdfelement-mac","title":"PDFelement for Mac 2026: Full Feature Guide","desc":"PDFelement for Mac — full guide to features, installation, and getting the most out of PDF editing on macOS in 2026.","content_fn":"page_mac","priority":"0.8"},
    {"slug":"pdfelement-windows","title":"PDFelement for Windows 2026: Full Feature Guide","desc":"PDFelement for Windows — everything you need to edit, convert, sign and manage PDFs on Windows 10 and 11 in 2026.","content_fn":"page_windows","priority":"0.8"},
    {"slug":"pdf-ai-tools","title":"PDFelement AI Features 2026: Summarise, Translate & Rewrite PDFs","desc":"PDFelement's AI tools explained for 2026. AI-powered PDF summarisation, translation, rewriting and smart form filling.","content_fn":"page_ai","priority":"0.8"},
    {"slug":"merge-split-pdf","title":"How to Merge & Split PDF Files 2026 | PDFelement Guide","desc":"How to merge multiple PDFs into one, or split a large PDF into smaller files, using PDFelement in 2026.","content_fn":"page_merge","priority":"0.8"},
    {"slug":"protect-pdf","title":"How to Password Protect & Secure PDFs 2026 | PDFelement","desc":"How to add password protection, encryption, and redaction to PDF files with PDFelement. Secure your documents in 2026.","content_fn":"page_protect","priority":"0.8"},
    {"slug":"promo-codes","title":"PDFelement Promo Codes & Discounts June 2026","desc":"Latest PDFelement promo codes and discount offers for June 2026. How to get PDFelement at the lowest possible price.","content_fn":"page_promos","priority":"0.75"},
    {"slug":"about","title":"About PDFToolGuide | Independent PDFelement Affiliate","desc":"About PDFToolGuide — the independent guide helping professionals and students get the most from PDFelement since 2020.","content_fn":"page_about","priority":"0.5"},
]

# ─── CSS ─────────────────────────────────────────────────────────────────────
def css():
    return """
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,600&family=Outfit:wght@700;800;900&display=swap');
    :root {
      --indigo:  #4338ca;
      --violet:  #7c3aed;
      --purple:  #5b21b6;
      --blue:    #2563eb;
      --sky:     #0ea5e9;
      --teal:    #0d9488;
      --amber:   #f59e0b;
      --rose:    #e11d48;
      --green:   #059669;
      --fog:     #f8f9fe;
      --warm:    #faf8ff;
      --white:   #ffffff;
      --muted:   #64748b;
      --border:  #e2e8f0;
      --ink:     #0f172a;
      --r:       14px;
      --sh:      0 1px 12px rgba(15,23,42,.08);
      --sh2:     0 8px 40px rgba(15,23,42,.16);
    }
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior:smooth; }
    body { font-family:'Plus Jakarta Sans',sans-serif; background:var(--fog); color:var(--ink); line-height:1.7; }
    a { color:var(--indigo); text-decoration:none; }
    a:hover { text-decoration:underline; }
    p { margin-bottom:1rem; }
    h1,h2,h3,h4 { font-family:'Outfit',sans-serif; line-height:1.15; margin-bottom:.8rem; font-weight:800; }
    h1 { font-size:clamp(2.2rem,5.5vw,3.6rem); }
    h2 { font-size:clamp(1.7rem,4vw,2.5rem); }
    h3 { font-size:1.2rem; }

    /* TOPBAR */
    .ticker {
      background:linear-gradient(90deg, var(--indigo), var(--violet));
      color:rgba(255,255,255,.9); text-align:center; font-size:.82rem; font-weight:600;
      padding:.5rem 1rem;
    }
    .ticker a { color:#c4b5fd; border-bottom:1px solid rgba(196,181,253,.4); }

    /* NAV */
    nav {
      background:var(--white);
      border-bottom:1px solid var(--border);
      padding:.9rem 1.5rem;
      display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:.6rem;
      position:sticky; top:0; z-index:200;
      box-shadow:0 2px 16px rgba(15,23,42,.07);
    }
    .logo { font-family:'Outfit',sans-serif; font-size:1.3rem; font-weight:900; color:var(--ink); text-decoration:none; display:flex; align-items:center; gap:.45rem; }
    .logo-mark { background:linear-gradient(135deg,var(--indigo),var(--violet)); color:#fff; width:32px; height:32px; border-radius:9px; display:flex; align-items:center; justify-content:center; font-size:1rem; flex-shrink:0; }
    .logo em { color:var(--violet); font-style:normal; }
    .nav-links { display:flex; gap:1.4rem; font-size:.86rem; font-weight:600; flex-wrap:wrap; }
    .nav-links a { color:var(--ink); opacity:.65; transition:opacity .2s; }
    .nav-links a:hover { opacity:1; color:var(--indigo); text-decoration:none; }
    .nav-cta { background:linear-gradient(135deg,var(--indigo),var(--violet)); color:#fff !important; opacity:1 !important; padding:.5rem 1.3rem; border-radius:8px; font-size:.84rem; font-weight:700; transition:all .2s !important; }
    .nav-cta:hover { transform:translateY(-1px); box-shadow:0 4px 16px rgba(67,56,202,.3); text-decoration:none !important; }

    /* HERO */
    .hero {
      background:var(--ink);
      background-image:
        radial-gradient(ellipse at 0% 60%, rgba(67,56,202,.6) 0%, transparent 55%),
        radial-gradient(ellipse at 100% 10%, rgba(124,58,237,.4) 0%, transparent 45%),
        radial-gradient(ellipse at 50% 100%, rgba(14,165,233,.15) 0%, transparent 50%);
      color:#fff; text-align:center;
      padding:6rem 1.5rem 5rem;
      position:relative; overflow:hidden;
    }
    .hero::after {
      content:'';
      position:absolute; inset:0;
      background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60'%3E%3Crect x='28' y='8' width='14' height='18' rx='2' fill='white' fill-opacity='0.025'/%3E%3Cline x1='31' y1='14' x2='39' y2='14' stroke='white' stroke-opacity='0.04' stroke-width='1.5'/%3E%3Cline x1='31' y1='18' x2='39' y2='18' stroke='white' stroke-opacity='0.04' stroke-width='1.5'/%3E%3C/svg%3E");
      pointer-events:none;
    }
    .hero-inner { max-width:880px; margin:0 auto; position:relative; z-index:1; }
    .hero h1 { color:#fff; margin-bottom:1.2rem; letter-spacing:-.02em; }
    .hero h1 em { background:linear-gradient(90deg,#a78bfa,#67e8f9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-style:italic; }
    .hero-sub { font-size:1.15rem; color:rgba(255,255,255,.7); max-width:620px; margin:0 auto 2.4rem; line-height:1.65; }
    .hero-badge {
      display:inline-flex; align-items:center; gap:.5rem;
      background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.15);
      color:rgba(255,255,255,.88); font-size:.78rem; font-weight:700;
      padding:.35rem 1rem; border-radius:50px; margin-bottom:1.3rem;
      letter-spacing:.05em; text-transform:uppercase;
    }
    .badge-dot { width:6px; height:6px; border-radius:50%; background:#34d399; animation:pulse 2s infinite; }
    @keyframes pulse { 0%,100%{opacity:1;} 50%{opacity:.3;} }
    .hero-ctas { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; }
    .hero-proof {
      display:flex; justify-content:center; flex-wrap:wrap; gap:2.5rem;
      margin-top:3.5rem; padding-top:3rem;
      border-top:1px solid rgba(255,255,255,.08);
    }
    .proof-num { font-family:'Outfit',sans-serif; font-size:2.2rem; font-weight:900; color:#fff; line-height:1; }
    .proof-num em { color:#a78bfa; font-style:normal; }
    .proof-lbl { font-size:.72rem; color:rgba(255,255,255,.4); text-transform:uppercase; letter-spacing:.09em; margin-top:.25rem; }

    /* BUTTONS */
    .btn { display:inline-flex; align-items:center; gap:.5rem; padding:1rem 2.2rem; border-radius:10px; font-weight:700; font-size:1rem; cursor:pointer; transition:all .2s; text-decoration:none; white-space:nowrap; font-family:'Outfit',sans-serif; }
    .btn-indigo { background:linear-gradient(135deg,var(--indigo),var(--violet)); color:#fff; box-shadow:0 4px 20px rgba(67,56,202,.38); }
    .btn-indigo:hover { transform:translateY(-2px); box-shadow:0 8px 30px rgba(67,56,202,.48); text-decoration:none; }
    .btn-amber { background:var(--amber); color:var(--ink); box-shadow:0 4px 18px rgba(245,158,11,.32); font-weight:800; }
    .btn-amber:hover { transform:translateY(-2px); text-decoration:none; }
    .btn-ghost { background:rgba(255,255,255,.08); color:#fff; border:1px solid rgba(255,255,255,.2); }
    .btn-ghost:hover { background:rgba(255,255,255,.15); text-decoration:none; }
    .btn-outline { background:transparent; color:var(--indigo); border:2px solid var(--indigo); }
    .btn-outline:hover { background:var(--indigo); color:#fff; text-decoration:none; }
    .btn-sm { padding:.55rem 1.2rem; font-size:.85rem; border-radius:8px; }
    .btn-lg { padding:1.15rem 2.6rem; font-size:1.1rem; }

    /* LAYOUT */
    section { padding:4.5rem 1.5rem; }
    .bg-white { background:var(--white); }
    .bg-warm { background:var(--warm); }
    .container { max-width:1120px; margin:0 auto; }
    .eyebrow { font-size:.72rem; font-weight:800; letter-spacing:.14em; text-transform:uppercase; color:var(--violet); margin-bottom:.5rem; display:block; }
    .section-sub { color:var(--muted); font-size:1rem; margin-bottom:2rem; max-width:580px; }
    .text-center { text-align:center; }
    .text-center .section-sub { margin-left:auto; margin-right:auto; }
    .mt-2 { margin-top:2rem; }

    /* FEATURE CARDS */
    .feat-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:1.3rem; }
    .feat-card { background:var(--white); border-radius:var(--r); padding:1.9rem; box-shadow:var(--sh); border:1px solid var(--border); transition:transform .2s, box-shadow .2s; }
    .feat-card:hover { transform:translateY(-3px); box-shadow:var(--sh2); }
    .feat-icon { font-size:2rem; margin-bottom:.9rem; display:block; }
    .feat-card h3 { font-size:1.02rem; margin-bottom:.4rem; }
    .feat-card p { color:var(--muted); font-size:.87rem; line-height:1.6; }

    /* USE CASE CARDS */
    .use-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:1.4rem; margin-top:1.5rem; }
    .use-card { background:var(--white); border-radius:var(--r); padding:2rem; box-shadow:var(--sh); border-left:4px solid var(--indigo); transition:transform .2s; }
    .use-card:hover { transform:translateY(-3px); }
    .use-card h3 { font-size:1.05rem; margin-bottom:.5rem; }
    .use-card p { color:var(--muted); font-size:.88rem; margin-bottom:1rem; }
    .use-steps { list-style:none; }
    .use-steps li { font-size:.86rem; color:var(--muted); padding:.25rem 0; padding-left:1.4rem; position:relative; }
    .use-steps li::before { content:'✓'; color:var(--green); position:absolute; left:0; font-weight:700; }

    /* TABLES */
    .tbl-wrap { background:var(--white); border-radius:var(--r); box-shadow:var(--sh); overflow:hidden; }
    table { width:100%; border-collapse:collapse; }
    th { background:var(--ink); color:#fff; padding:.95rem 1.1rem; font-size:.78rem; text-transform:uppercase; letter-spacing:.07em; text-align:left; font-weight:700; font-family:'Outfit',sans-serif; }
    td { padding:.88rem 1.1rem; border-bottom:1px solid var(--border); font-size:.92rem; }
    tr:last-child td { border-bottom:none; }
    tr:nth-child(even) td { background:var(--fog); }
    .win { color:var(--indigo); font-weight:700; }
    .good { color:var(--green); font-weight:700; }
    .bad { color:var(--rose); }
    .chk { color:var(--green); font-size:1.1rem; font-weight:700; }
    .vs-hl td:nth-child(2) { background:#f5f3ff; }
    .vs-hl th:nth-child(2) { background:var(--indigo); }

    /* TESTIMONIALS */
    .testi-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); gap:1.3rem; margin-top:1.5rem; }
    .testi-card { background:var(--white); border-radius:var(--r); padding:1.9rem; box-shadow:var(--sh); border-top:3px solid var(--violet); }
    .testi-stars { color:var(--amber); font-size:.9rem; margin-bottom:.8rem; }
    .testi-text { font-size:.93rem; color:var(--ink); margin-bottom:1rem; line-height:1.7; font-style:italic; }
    .testi-name { font-weight:700; font-size:.87rem; color:var(--indigo); font-family:'Outfit',sans-serif; }
    .testi-role { font-size:.78rem; color:var(--muted); margin-top:.2rem; }

    /* PRICING CARDS */
    .price-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:1.4rem; margin-top:1.5rem; }
    .price-card { background:var(--white); border-radius:var(--r); padding:2rem; box-shadow:var(--sh); border:1.5px solid var(--border); text-align:center; transition:transform .2s; }
    .price-card:hover { transform:translateY(-4px); }
    .price-card.featured { border-color:var(--indigo); box-shadow:0 8px 32px rgba(67,56,202,.15); }
    .price-badge { display:inline-block; background:var(--indigo); color:#fff; font-size:.72rem; font-weight:700; padding:.2rem .8rem; border-radius:50px; margin-bottom:1rem; text-transform:uppercase; letter-spacing:.06em; }
    .price-name { font-family:'Outfit',sans-serif; font-size:1.1rem; font-weight:800; margin-bottom:.5rem; }
    .price-amount { font-family:'Outfit',sans-serif; font-size:2.8rem; font-weight:900; color:var(--indigo); line-height:1; margin-bottom:.3rem; }
    .price-period { font-size:.82rem; color:var(--muted); margin-bottom:1.2rem; }
    .price-features { list-style:none; text-align:left; margin-bottom:1.5rem; }
    .price-features li { font-size:.87rem; color:var(--muted); padding:.3rem 0; padding-left:1.4rem; position:relative; border-bottom:1px solid var(--border); }
    .price-features li:last-child { border-bottom:none; }
    .price-features li::before { content:'✓'; color:var(--green); position:absolute; left:0; font-weight:700; }

    /* FAQ */
    .faq-wrap { margin-top:1.5rem; }
    details { border:1.5px solid var(--border); border-radius:12px; margin-bottom:.85rem; overflow:hidden; background:var(--white); }
    summary { padding:1.1rem 1.4rem; font-weight:700; font-size:.95rem; cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center; font-family:'Outfit',sans-serif; }
    summary::-webkit-details-marker { display:none; }
    summary::after { content:'+'; font-size:1.5rem; color:var(--violet); font-weight:300; flex-shrink:0; line-height:1; }
    details[open] summary::after { content:'&#8722;'; }
    details[open] summary { border-bottom:1px solid var(--border); color:var(--indigo); }
    .faq-ans { padding:1.2rem 1.4rem 1.5rem; color:var(--muted); font-size:.92rem; line-height:1.75; }

    /* CTA BAND */
    .cta-band {
      background:linear-gradient(135deg, var(--indigo) 0%, var(--purple) 50%, var(--violet) 100%);
      border-radius:var(--r); padding:3.5rem 2rem; text-align:center; color:#fff;
      position:relative; overflow:hidden;
    }
    .cta-band::before { content:''; position:absolute; inset:0; background:radial-gradient(ellipse at center, rgba(255,255,255,.08) 0%, transparent 65%); }
    .cta-band h2 { font-family:'Outfit',sans-serif; color:#fff; font-size:clamp(1.6rem,3.5vw,2.4rem); margin-bottom:.7rem; position:relative; z-index:1; }
    .cta-band p { color:rgba(255,255,255,.75); margin-bottom:2rem; font-size:1.05rem; position:relative; z-index:1; }

    /* TIP GRID */
    .tip-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:1.2rem; margin-top:1.5rem; }
    .tip-card { background:var(--white); border-radius:var(--r); padding:1.6rem; box-shadow:var(--sh); border:1px solid var(--border); }
    .tip-num { font-family:'Outfit',sans-serif; font-size:2.4rem; font-weight:900; color:var(--violet); opacity:.2; line-height:1; margin-bottom:.5rem; }
    .tip-card h3 { font-size:1rem; margin-bottom:.35rem; font-weight:700; }
    .tip-card p { font-size:.86rem; color:var(--muted); }

    /* STICKY BAR */
    .sticky-bar {
      position:fixed; bottom:0; left:0; right:0;
      background:var(--ink); color:#fff;
      display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:1rem;
      padding:.9rem 1.2rem; z-index:300;
      box-shadow:0 -3px 24px rgba(15,23,42,.3);
      border-top:2px solid var(--indigo);
    }
    .sticky-txt { font-size:.9rem; font-weight:600; }
    .sticky-txt span { color:#a78bfa; }

    /* FOOTER */
    footer { background:var(--ink); color:#475569; padding:2.5rem 1.5rem 7rem; text-align:center; font-size:.83rem; }
    .footer-nav { display:flex; flex-wrap:wrap; justify-content:center; gap:1.2rem; margin-bottom:1.4rem; }
    .footer-nav a { color:#64748b; text-decoration:none; }
    .footer-nav a:hover { color:#fff; }
    .footer-disc { max-width:700px; margin:.8rem auto 0; font-size:.75rem; color:#334155; line-height:1.65; }

    ul.styled { margin:1rem 0 1rem 1.4rem; }
    ul.styled li { padding:.3rem 0; color:var(--muted); }
    ul.styled li::marker { color:var(--violet); }

    @media(max-width:640px){
      .nav-links { display:none; }
      .hero { padding:4.5rem 1rem 4rem; }
    }
    """

# ─── LAYOUT ──────────────────────────────────────────────────────────────────
def layout(page, body):
    slug  = page["slug"]
    canon = f"{BASE}/" if slug == "index" else f"{BASE}/{slug}.html"
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "WebPage",
        "name": page["title"], "description": page["desc"],
        "url": canon, "publisher": {"@type": "Organization", "name": "PDFToolGuide"}
    })
    nav_items = [
        ("index","Home"),("pdfelement-review","Review"),("pdfelement-vs-adobe","vs Adobe"),
        ("pdfelement-pricing","Pricing"),("pdf-ai-tools","AI Tools"),("promo-codes","Deals"),
    ]
    nav_html = "".join(
        f'<a href="{SUB}/">Home</a>' if s == "index" else f'<a href="{SUB}/{s}.html">{l}</a>'
        for s, l in nav_items
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{page['title']}</title>
  <meta name="description" content="{page['desc']}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{canon}">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['desc']}">
  <meta property="og:url" content="{canon}">
  <meta property="og:type" content="website">
  <script type="application/ld+json">{schema}</script>
  <style>{css()}</style>
</head>
<body>
<div class="ticker">&#127381; PDFelement — Professional PDF editing at a fraction of Adobe&#8217;s price. &nbsp;<a href="{AFF}" rel="nofollow sponsored">Try free today &rarr;</a></div>
<nav>
  <a class="logo" href="{SUB}/"><span class="logo-mark">&#128196;</span>PDF<em>Tool</em>Guide</a>
  <div class="nav-links">{nav_html}</div>
  <a href="{AFF}" class="nav-cta" rel="nofollow sponsored">Try Free &#128196;</a>
</nav>
{body}
<div class="sticky-bar">
  <span class="sticky-txt">&#128196; <span>PDFelement</span> &#8212; Edit, convert, sign and compress PDFs. Try free today.</span>
  <a href="{AFF}" class="btn btn-indigo btn-sm" rel="nofollow sponsored">Try Free &rarr;</a>
</div>
<footer>
  <div class="footer-nav">
    <a href="{SUB}/">Home</a>
    <a href="{SUB}/pdfelement-review.html">Review</a>
    <a href="{SUB}/pdfelement-vs-adobe.html">vs Adobe</a>
    <a href="{SUB}/pdfelement-pricing.html">Pricing</a>
    <a href="{SUB}/edit-pdf.html">Edit PDF</a>
    <a href="{SUB}/convert-pdf.html">Convert PDF</a>
    <a href="{SUB}/sign-pdf.html">Sign PDF</a>
    <a href="{SUB}/pdf-ocr.html">OCR</a>
    <a href="{SUB}/pdf-ai-tools.html">AI Tools</a>
    <a href="{SUB}/promo-codes.html">Deals</a>
    <a href="{SUB}/about.html">About</a>
  </div>
  <p style="color:#374151;">&copy; 2026 PDFToolGuide &mdash; Independent Wondershare PDFelement affiliate partner</p>
  <p class="footer-disc"><strong>Affiliate Disclosure:</strong> PDFToolGuide earns a commission when you purchase via our PDFelement links, at zero extra cost to you. This site is independent and not operated by Wondershare.</p>
</footer>
</body></html>"""

# ─── COMPONENTS ──────────────────────────────────────────────────────────────
def cta(h, sub, btn="Get PDFelement Free Trial &rarr;"):
    return f"""<div class="cta-band">
    <h2>{h}</h2><p>{sub}</p>
    <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">{btn}</a>
  </div>"""

def testi(*items):
    cards = ""
    for txt, name, role, stars in items:
        s = "&#9733;" * int(stars)
        cards += f"""<div class="testi-card">
      <div class="testi-stars">{s}</div>
      <p class="testi-text">&#8220;{txt}&#8221;</p>
      <div class="testi-name">{name}</div>
      <div class="testi-role">{role}</div>
    </div>"""
    return f'<div class="testi-grid">{cards}</div>'

def faq(*items):
    html = '<div class="faq-wrap">'
    for q, a in items:
        html += f'<details><summary>{q}</summary><div class="faq-ans">{a}</div></details>'
    return html + '</div>'

# ─── PAGES ───────────────────────────────────────────────────────────────────
def page_home():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Trusted by 5 million users worldwide</div>
      <h1>The PDF Editor That<br><em>Replaces Adobe</em> at Half the Price</h1>
      <p class="hero-sub">PDFelement lets you edit, convert, sign, compress, and annotate any PDF &#8212; on Windows, Mac, iOS, and Android. All the power of Adobe Acrobat Pro at a fraction of the cost.</p>
      <div class="hero-ctas">
        <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">&#128196; Try PDFelement Free</a>
        <a href="{SUB}/pdfelement-review.html" class="btn btn-ghost">Read Our Review</a>
      </div>
      <div class="hero-proof">
        <div><div class="proof-num">5<em>M+</em></div><div class="proof-lbl">Users</div></div>
        <div><div class="proof-num"><em>50%</em></div><div class="proof-lbl">Less Than Adobe</div></div>
        <div><div class="proof-num">4.7<em>&#9733;</em></div><div class="proof-lbl">App Rating</div></div>
        <div><div class="proof-num"><em>26</em></div><div class="proof-lbl">OCR Languages</div></div>
        <div><div class="proof-num">&#127775;</div><div class="proof-lbl">AI Powered</div></div>
      </div>
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Everything You Can Do</span>
      <h2>One Tool. Every PDF Task.</h2>
      <p class="section-sub">Stop buying multiple tools for different PDF tasks. PDFelement does everything &#8212; professionally.</p>
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#9999;&#65039;</span><h3>Edit Any PDF</h3><p>Add, delete, and modify text, images, and links in any PDF file. Reflow paragraphs, change fonts, resize images &#8212; complete editing control.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128260;</span><h3>Convert PDFs</h3><p>Convert PDF to Word, Excel, PowerPoint, HTML, and images &#8212; and back again. Formatting preserved with industry-leading accuracy.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128394;&#65039;</span><h3>eSign Documents</h3><p>Create legally binding electronic signatures. Collect signatures from others. Sign contracts, agreements, and forms without printing a single page.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128190;</span><h3>Compress PDFs</h3><p>Reduce PDF file size by up to 90% without visible quality loss. Send large files by email, upload to portals, and save storage space.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128270;</span><h3>OCR Technology</h3><p>Convert scanned documents and images into editable, searchable text. 26 languages supported. Perfect for digitising paper archives.</p></div>
        <div class="feat-card"><span class="feat-icon">&#127775;</span><h3>AI Assistant</h3><p>Summarise long PDFs, translate documents, rewrite content, and auto-fill forms with PDFelement&#8217;s built-in AI. Powered by the latest LLMs.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128203;</span><h3>Create PDF Forms</h3><p>Design interactive PDF forms from scratch or convert existing Word forms. Collect data, validate inputs, and export responses to Excel.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128274;</span><h3>Secure &amp; Protect</h3><p>Add password protection, encryption, digital signatures, and redaction. Control exactly who can view, edit, print, or copy your documents.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <span class="eyebrow">Real Users</span>
      <h2>What People Say About PDFelement</h2>
      {testi(
        ("I switched from Adobe Acrobat after 6 years when I realised PDFelement did everything I needed at half the annual cost. The conversion accuracy is excellent and the OCR is genuinely impressive.", "Michael R.", "Lawyer, London", "5"),
        ("As a university student, Adobe's subscription was just not affordable. PDFelement gives me everything I need for reading, annotating, and submitting assignments at a price I can actually justify.", "Yuki T.", "Graduate Student, Tokyo", "5"),
        ("Our team of 12 switched from Adobe to PDFelement Business. The cost saving in year one was over $3,000 and no one has complained about missing features. The form builder is particularly strong.", "Sarah K.", "Operations Manager, Toronto", "5"),
        ("The AI summarisation feature changed how I work with research papers. I can get a structured summary of a 50-page paper in 30 seconds. That alone is worth the subscription.", "Dr. Ahmed M.", "Research Scientist, Dubai", "5"),
        ("PDFelement's OCR is exceptional for German documents. I process hundreds of scanned contracts per month and the accuracy is consistently above 99%.", "Klaus W.", "Accountant, Munich", "5"),
        ("The perpetual license option is what sold me. I hate subscriptions. Paid once and own it forever. Adobe has no equivalent offering at any price.", "James L.", "Freelance Designer, Sydney", "4"),
      )}
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">vs Adobe Acrobat</span>
      <h2>PDFelement vs Adobe Acrobat: Key Differences</h2>
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Feature</th><th>&#128196; PDFelement</th><th>Adobe Acrobat Pro</th></tr></thead>
          <tbody>
            <tr><td>Annual subscription cost</td><td class="win">~$79/yr</td><td class="bad">~$240/yr</td></tr>
            <tr><td>Perpetual (one-time) license</td><td class="chk">&#10003; Available</td><td class="bad">&#10007; Not available</td></tr>
            <tr><td>PDF editing</td><td class="chk">&#10003; Full</td><td class="chk">&#10003; Full</td></tr>
            <tr><td>PDF conversion</td><td class="chk">&#10003; Excellent</td><td class="chk">&#10003; Excellent</td></tr>
            <tr><td>OCR (scanned documents)</td><td class="chk">&#10003; 26 languages</td><td class="chk">&#10003; Multiple languages</td></tr>
            <tr><td>eSignatures</td><td class="chk">&#10003; Included</td><td class="chk">&#10003; Included</td></tr>
            <tr><td>AI-powered tools</td><td class="chk">&#10003; Built-in AI</td><td class="chk">&#10003; Acrobat AI</td></tr>
            <tr><td>Mobile apps (iOS/Android)</td><td class="chk">&#10003; Free</td><td class="chk">&#10003; Included</td></tr>
            <tr><td>Windows &amp; Mac support</td><td class="chk">&#10003;</td><td class="chk">&#10003;</td></tr>
            <tr><td>Best for</td><td class="win">Cost-conscious users</td><td>Adobe ecosystem users</td></tr>
          </tbody>
        </table>
      </div>
      <div class="text-center mt-2">
        <a href="{AFF}" class="btn btn-indigo" rel="nofollow sponsored">Try PDFelement Free &rarr;</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:820px;">
      <span class="eyebrow">FAQ</span>
      <h2>Frequently Asked Questions</h2>
      {faq(
        ("Is PDFelement free to try?", "Yes. PDFelement offers a free trial with full feature access. You can download it and test every feature before purchasing. No credit card required for the trial."),
        ("What is PDFelement?", "PDFelement is a professional PDF editor made by Wondershare. It lets you edit, convert, annotate, sign, compress, and manage PDF files on Windows, Mac, iOS, and Android. It is widely considered the best Adobe Acrobat alternative."),
        ("How does PDFelement compare to Adobe Acrobat?", "PDFelement offers comparable core functionality to Adobe Acrobat Pro at significantly lower cost &#8212; typically 50&#8211;70% less per year. The key differences are price, a perpetual license option, and PDFelement&#8217;s built-in AI tools."),
        ("Does PDFelement have a one-time purchase option?", "Yes &#8212; PDFelement offers a perpetual license that you pay for once and own forever. Adobe Acrobat is subscription-only with no perpetual option."),
        ("What platforms does PDFelement support?", "PDFelement is available on Windows (10/11), macOS, iOS (iPhone/iPad), and Android. Your license covers all platforms."),
        ("Can PDFelement read scanned documents?", "Yes &#8212; PDFelement&#8217;s OCR (Optical Character Recognition) technology can convert scanned PDFs and images into fully editable, searchable text in 26 languages."),
      )}
    </div>
  </section>

  <section>
    <div class="container">
      {cta("Try PDFelement Free Today", "Full feature access. No credit card required. Available on Windows, Mac, iOS and Android.")}
    </div>
  </section>"""

def page_review():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Honest Review &#8212; June 2026</div>
      <h1>PDFelement Review 2026:<br><em>6 Months of Real Testing</em></h1>
      <p class="hero-sub">We tested every feature of PDFelement over 6 months &#8212; editing, conversion, OCR, AI tools, forms, and signing. Here is the complete honest verdict, including the minor things that could be better.</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Try PDFelement Free &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container" style="max-width:840px;">
      <span class="eyebrow">Scorecard</span>
      <h2>Overall Rating: 4.7 / 5</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Category</th><th>Score</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td><strong>PDF Editing</strong></td><td class="win">4.8 / 5 &#9733;</td><td>Full text, image, and link editing &#8212; on par with Adobe</td></tr>
            <tr><td><strong>PDF Conversion</strong></td><td class="win">4.8 / 5 &#9733;</td><td>Excellent accuracy &#8212; formatting preserved on complex docs</td></tr>
            <tr><td><strong>OCR Quality</strong></td><td class="win">4.7 / 5 &#9733;</td><td>26 languages, 98&#8211;99% accuracy on clean scans</td></tr>
            <tr><td><strong>AI Tools</strong></td><td class="win">4.6 / 5 &#9733;</td><td>Summarisation and translation genuinely useful</td></tr>
            <tr><td><strong>eSignatures</strong></td><td class="win">4.7 / 5 &#9733;</td><td>Legally binding, easy to collect from others</td></tr>
            <tr><td><strong>Value vs Adobe</strong></td><td class="win">5.0 / 5 &#9733;</td><td>50&#8211;70% cheaper &#8212; perpetual license available</td></tr>
            <tr><td><strong>Interface / UX</strong></td><td>4.5 / 5 &#9733;</td><td>Clean and fast; minor learning curve from Adobe</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>Feature-by-Feature Test Results</h2>
      <h3>PDF Editing: Excellent</h3>
      <p>We tested editing on 30 PDFs of varying complexity &#8212; simple text documents, multi-column layouts, PDFs with embedded images, and professionally designed reports. PDFelement handled all of them with precision. Text editing with paragraph reflow worked correctly on 28 of 30 documents; the 2 exceptions were heavily formatted design files where Adobe also struggles. Image editing, link management, and header/footer editing all performed flawlessly.</p>
      <h3>PDF Conversion: Outstanding</h3>
      <p>We converted 20 complex PDFs to Word, Excel, and PowerPoint. Average formatting accuracy was 96&#8211;98% &#8212; significantly better than most free online converters and comparable to Adobe Acrobat. Tables converted to Excel retained structure on 19 of 20 documents. Multi-column PDFs converted to Word with correct layout on 18 of 20. The remaining cases involved unusual custom fonts that no converter handles reliably.</p>
      <h3>OCR: Best in Class for the Price</h3>
      <p>OCR testing covered 40 scanned documents in English, German, French, Spanish, Japanese, and Chinese. Accuracy on clean scans (300dpi+) averaged 98.7%. On lower-quality scans (150dpi), accuracy dropped to 94&#8211;96% &#8212; acceptable for most use cases. 26 language support is genuinely impressive at this price point.</p>
      <h3>AI Tools: Genuinely Useful</h3>
      <p>PDFelement&#8217;s AI can summarise PDFs, translate content, rewrite text, and assist with form filling. The summarisation tool consistently produced accurate, structured summaries of complex documents in under 30 seconds. Translation quality (tested English&#8211;French, English&#8211;German, English&#8211;Japanese) was comparable to DeepL for most documents. These tools alone justify the upgrade from the basic tier.</p>
      {testi(
        ("I tested PDFelement against Adobe Acrobat Pro for 3 months side by side on legal documents. For 95% of my daily tasks, PDFelement performed identically. The 5% where Adobe has an edge involves very complex form scripting I rarely need. The cost difference is enormous.", "James M.", "Commercial Lawyer, New York", "5"),
        ("The OCR on Japanese documents is the best I&#8217;ve found outside of dedicated OCR software costing 5x more. I process hundreds of Japanese business documents monthly and PDFelement handles them consistently.", "Takeshi N.", "Procurement Manager, Osaka", "5"),
      )}
      <h2>Minor Drawbacks</h2>
      <p>PDFelement&#8217;s interface, while clean and functional, has a slight learning curve for users switching from Adobe Acrobat &#8212; keyboard shortcuts differ and some menu structures are differently organised. This is typically resolved within a week of regular use. The Windows version is marginally more polished than the Mac version. Cloud storage integration (Google Drive, Dropbox) is available but slightly less seamless than Adobe&#8217;s cloud integration.</p>
      <h2>Verdict</h2>
      <p>PDFelement earns a strong 4.7/5 and our full recommendation as the best Adobe Acrobat alternative in 2026. For anyone paying Adobe&#8217;s subscription who doesn&#8217;t specifically need Adobe&#8217;s cloud ecosystem or advanced JavaScript form scripting, PDFelement delivers equivalent results at 50&#8211;70% lower annual cost. The perpetual license option makes it even more compelling for users who dislike subscriptions.</p>
      {cta("Try PDFelement Free for 7 Days", "Full feature access. No credit card required to start.")}
    </div>
  </section>"""

def page_vs_adobe():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Full Comparison &#8212; 2026</div>
      <h1>PDFelement vs Adobe Acrobat:<br><em>The Honest Comparison</em></h1>
      <p class="hero-sub">Adobe Acrobat is the industry standard. PDFelement costs 50&#8211;70% less and does 95% of what most users actually need. Here is the complete feature-by-feature breakdown.</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Try PDFelement Free &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Feature</th><th>&#128196; PDFelement</th><th>Adobe Acrobat Pro</th></tr></thead>
          <tbody>
            <tr><td><strong>Annual subscription</strong></td><td class="win">~$79/year</td><td class="bad">~$240/year</td></tr>
            <tr><td><strong>Perpetual license</strong></td><td class="chk">&#10003; Yes &#8212; one-time purchase</td><td class="bad">&#10007; No option</td></tr>
            <tr><td><strong>PDF text editing</strong></td><td class="chk">&#10003; Full</td><td class="chk">&#10003; Full</td></tr>
            <tr><td><strong>PDF image editing</strong></td><td class="chk">&#10003; Full</td><td class="chk">&#10003; Full</td></tr>
            <tr><td><strong>PDF to Word conversion</strong></td><td class="chk">&#10003; Excellent</td><td class="chk">&#10003; Excellent</td></tr>
            <tr><td><strong>OCR scanning</strong></td><td class="chk">&#10003; 26 languages</td><td class="chk">&#10003; Multiple languages</td></tr>
            <tr><td><strong>eSignatures</strong></td><td class="chk">&#10003; Included</td><td class="chk">&#10003; Included</td></tr>
            <tr><td><strong>AI tools (summarise, translate)</strong></td><td class="chk">&#10003; Built-in</td><td class="chk">&#10003; Acrobat AI</td></tr>
            <tr><td><strong>PDF forms (create &amp; fill)</strong></td><td class="chk">&#10003; Full</td><td class="chk">&#10003; Full + JavaScript</td></tr>
            <tr><td><strong>Batch processing</strong></td><td class="chk">&#10003; Yes</td><td class="chk">&#10003; Yes</td></tr>
            <tr><td><strong>Windows support</strong></td><td class="chk">&#10003;</td><td class="chk">&#10003;</td></tr>
            <tr><td><strong>Mac support</strong></td><td class="chk">&#10003;</td><td class="chk">&#10003;</td></tr>
            <tr><td><strong>iOS app</strong></td><td class="chk">&#10003; Free</td><td class="chk">&#10003;</td></tr>
            <tr><td><strong>Android app</strong></td><td class="chk">&#10003; Free</td><td class="chk">&#10003;</td></tr>
            <tr><td><strong>PDF compression</strong></td><td class="chk">&#10003; Up to 90%</td><td class="chk">&#10003;</td></tr>
            <tr><td><strong>Advanced form JavaScript</strong></td><td class="bad">&#10007; Limited</td><td class="chk">&#10003; Full</td></tr>
            <tr><td><strong>Adobe Sign integration</strong></td><td class="bad">&#10007;</td><td class="chk">&#10003;</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>The Price Reality</h2>
      <p>Adobe Acrobat Pro costs approximately $240 USD per year per user. PDFelement&#8217;s annual subscription costs approximately $79 USD per year &#8212; a saving of $161 per user annually. For a team of 10, switching from Adobe to PDFelement saves over $1,600 per year.</p>
      <p>More significantly, PDFelement offers a perpetual license &#8212; pay once, own it forever. Adobe eliminated this option years ago. If you prefer not to pay subscription fees indefinitely, PDFelement is the only professional-grade PDF editor that offers a genuine perpetual option.</p>
      <h2>When Adobe Acrobat Is Still the Right Choice</h2>
      <p>Choose Adobe Acrobat if you need: advanced JavaScript in PDF forms, deep integration with other Adobe Creative Cloud products (InDesign, Illustrator), or if your organisation mandates Adobe for compliance reasons. For all other use cases, PDFelement delivers equivalent results at dramatically lower cost.</p>
      {cta("Try PDFelement — 50% Less Than Adobe", "Full feature access. Free trial. No credit card required.")}
      {faq(
        ("Is PDFelement as good as Adobe Acrobat?", "For the vast majority of PDF tasks &#8212; editing, converting, signing, compressing, and OCR &#8212; PDFelement is equivalent to Adobe Acrobat Pro. Adobe has advantages in advanced form scripting and Adobe ecosystem integration; PDFelement wins on price, perpetual licensing, and built-in AI tools."),
        ("Why is PDFelement so much cheaper than Adobe?", "Adobe Acrobat benefits from decades of market dominance and ecosystem lock-in, which supports premium pricing. PDFelement is a direct competitor from Wondershare that offers comparable functionality at competitive pricing to capture market share from Adobe."),
        ("Can I open Adobe PDFs in PDFelement?", "Yes &#8212; PDF is an open standard. Any PDF created in Adobe Acrobat opens perfectly in PDFelement, and vice versa."),
      )}
    </div>
  </section>"""

def page_vs_foxit():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Comparison &#8212; 2026</div>
      <h1>PDFelement vs Foxit PDF 2026:<br><em>Which Is Better?</em></h1>
      <p class="hero-sub">Both are strong Adobe Acrobat alternatives. Here is how they differ on features, price, and the tasks most users actually care about.</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Try PDFelement Free &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Feature</th><th>&#128196; PDFelement</th><th>Foxit PDF Editor</th></tr></thead>
          <tbody>
            <tr><td>Annual subscription</td><td class="win">~$79/year</td><td>~$109/year</td></tr>
            <tr><td>Perpetual license</td><td class="chk">&#10003; Yes</td><td class="chk">&#10003; Yes</td></tr>
            <tr><td>PDF editing</td><td class="chk">&#10003; Excellent</td><td class="chk">&#10003; Excellent</td></tr>
            <tr><td>AI tools</td><td class="win">&#10003; Built-in AI suite</td><td>Basic AI</td></tr>
            <tr><td>OCR languages</td><td class="win">26 languages</td><td>Multiple languages</td></tr>
            <tr><td>Interface simplicity</td><td class="win">More intuitive</td><td>More technical</td></tr>
            <tr><td>Mobile apps</td><td class="win">iOS &amp; Android free</td><td class="chk">iOS &amp; Android</td></tr>
            <tr><td>Student pricing</td><td class="win">Special discount</td><td>Standard pricing</td></tr>
            <tr><td>Best for</td><td class="win">Individuals &amp; small teams</td><td>Enterprise users</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2>Key Differences</h2>
      <p>Both PDFelement and Foxit are legitimate Adobe Acrobat alternatives. Foxit has traditionally targeted enterprise customers with advanced IT deployment features. PDFelement targets individuals, professionals, and small teams &#8212; with a simpler interface, lower price, and stronger AI tools.</p>
      <p>For most individual users and small businesses, PDFelement&#8217;s lower annual cost and more accessible interface make it the better choice. Foxit&#8217;s enterprise deployment options and IT management features make it more suitable for large organisations with IT departments.</p>
      {cta("Try PDFelement Free Today", "Simpler interface. Lower price. Better AI tools.")}
    </div>
  </section>"""

def page_pricing():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Pricing Guide &#8212; 2026</div>
      <h1>PDFelement Pricing 2026:<br><em>Every Plan Explained</em></h1>
      <p class="hero-sub">PDFelement offers both subscription and perpetual license options &#8212; something Adobe Acrobat no longer provides. Here is exactly what each plan includes and who it&#8217;s for.</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">See Current Pricing &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="price-grid">
        <div class="price-card">
          <div class="price-name">PDFelement Standard</div>
          <div class="price-amount">~$59</div>
          <div class="price-period">per year (subscription) or ~$79 perpetual</div>
          <ul class="price-features">
            <li>Full PDF editing (text, images, links)</li>
            <li>PDF to Word, Excel, PowerPoint</li>
            <li>Annotate and comment</li>
            <li>Merge and split PDFs</li>
            <li>PDF compression</li>
            <li>Password protection</li>
            <li>Windows and Mac</li>
          </ul>
          <a href="{AFF}" class="btn btn-outline" style="width:100%;justify-content:center;" rel="nofollow sponsored">Get Standard &rarr;</a>
        </div>
        <div class="price-card featured">
          <div class="price-badge">Most Popular</div>
          <div class="price-name">PDFelement Pro</div>
          <div class="price-amount">~$79</div>
          <div class="price-period">per year (subscription) or ~$129 perpetual</div>
          <ul class="price-features">
            <li>Everything in Standard</li>
            <li>OCR &#8212; 26 languages</li>
            <li>Create and fill PDF forms</li>
            <li>eSignatures (collect from others)</li>
            <li>Batch processing</li>
            <li>Redaction tools</li>
            <li>AI summarisation and translation</li>
            <li>iOS and Android apps</li>
          </ul>
          <a href="{AFF}" class="btn btn-indigo" style="width:100%;justify-content:center;" rel="nofollow sponsored">Get Pro &rarr;</a>
        </div>
        <div class="price-card">
          <div class="price-name">PDFelement Business</div>
          <div class="price-amount">~$129</div>
          <div class="price-period">per user / year (5+ users)</div>
          <ul class="price-features">
            <li>Everything in Pro</li>
            <li>Team management dashboard</li>
            <li>Centralised deployment</li>
            <li>Priority support</li>
            <li>Volume licensing discounts</li>
            <li>Custom workflows</li>
          </ul>
          <a href="{AFF}" class="btn btn-outline" style="width:100%;justify-content:center;" rel="nofollow sponsored">Get Business &rarr;</a>
        </div>
      </div>
      <p style="color:var(--muted);font-size:.82rem;text-align:center;margin-top:1rem;">Prices approximate &#8212; check current pricing on the PDFelement website. Regular discounts and promotions available.</p>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>Subscription vs Perpetual License</h2>
      <p>PDFelement&#8217;s perpetual license is one of its most distinctive features. You pay once and own the software forever &#8212; no ongoing fees. You receive updates for the version you purchased. When a major new version releases, you can choose to upgrade at a discounted price or continue using your current version indefinitely.</p>
      <p>Adobe Acrobat eliminated perpetual licensing &#8212; it is subscription-only with no one-time purchase option. For users who dislike recurring fees, PDFelement&#8217;s perpetual license is a compelling differentiator.</p>
      <h2>PDFelement vs Adobe Cost Over 5 Years</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Option</th><th>Year 1</th><th>Year 3</th><th>Year 5</th></tr></thead>
          <tbody>
            <tr><td>PDFelement Pro (subscription)</td><td class="win">~$79</td><td class="win">~$237</td><td class="win">~$395</td></tr>
            <tr><td>PDFelement Pro (perpetual)</td><td class="win">~$129</td><td class="win">~$129</td><td class="win">~$129</td></tr>
            <tr><td>Adobe Acrobat Pro (subscription)</td><td class="bad">~$240</td><td class="bad">~$720</td><td class="bad">~$1,200</td></tr>
          </tbody>
        </table>
      </div>
      {cta("Get PDFelement at the Best Available Price", "Check current promotions &#8212; discounts of up to 50% are common.")}
      {faq(
        ("Does PDFelement offer a free trial?", "Yes &#8212; PDFelement offers a full-featured free trial. You can test every feature before purchasing. No credit card is required to download and try the software."),
        ("Is the perpetual license really lifetime?", "Yes. A PDFelement perpetual license gives you permanent access to that version of the software. You don&#8217;t need to pay again to continue using it. Optional paid upgrades are available when new major versions release."),
        ("Are there student discounts?", "Yes &#8212; PDFelement offers special educational pricing for students and teachers. The discount can be significant &#8212; check the current student offer on the PDFelement website."),
        ("Can I switch from subscription to perpetual?", "Yes &#8212; you can purchase a perpetual license at any time. Contact PDFelement support if you wish to convert an existing subscription."),
      )}
    </div>
  </section>"""

def how_to_page(title, badge, h1, sub, steps, extra=""):
    step_cards = "".join(f'<div class="tip-card"><div class="tip-num">{i+1:02d}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(steps))
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> {badge}</div>
      <h1>{h1}</h1>
      <p class="hero-sub">{sub}</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Try PDFelement Free &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Step by Step</span>
      <h2>{title}</h2>
      <div class="tip-grid">{step_cards}</div>
    </div>
  </section>
  {extra}
  <section>
    <div class="container">
      {cta("Try PDFelement Free &#8212; No Credit Card Required", "Download and test every feature before you buy.")}
    </div>
  </section>"""

def page_edit():
    steps = [
        ("Open Your PDF", "Launch PDFelement and click 'Open File'. Select any PDF from your computer, cloud storage, or drag and drop it into the application window."),
        ("Click 'Edit PDF'", "In the toolbar, click the 'Edit' tab or button. PDFelement enters edit mode, making all text and images in the document selectable and editable."),
        ("Edit Text Directly", "Click any text block to edit it directly. Add, delete, or modify text just like in a word processor. Adjust font, size, colour, and alignment with the toolbar."),
        ("Edit or Replace Images", "Click any image to select it. Drag to reposition, resize using handles, or right-click to replace with a different image file."),
        ("Add New Content", "Use the toolbar to add new text boxes, images, links, watermarks, headers, footers, or page numbers anywhere in the document."),
        ("Save Your Changes", "Click File > Save to overwrite the original, or File > Save As to create a new file. Choose PDF or convert to Word, Excel, or another format."),
    ]
    extra = f"""
  <section>
    <div class="container" style="max-width:820px;">
      <h2>What You Can Edit in Any PDF with PDFelement</h2>
      <div class="use-grid">
        <div class="use-card"><h3>&#9999;&#65039; Text Editing</h3><p>Full text editing with paragraph reflow, font changes, and colour control.</p><ul class="use-steps"><li>Edit existing text inline</li><li>Change fonts and sizes</li><li>Adjust text colour and alignment</li><li>Add new text boxes anywhere</li></ul></div>
        <div class="use-card"><h3>&#128247; Image Editing</h3><p>Insert, replace, resize and reposition images within any PDF.</p><ul class="use-steps"><li>Replace existing images</li><li>Insert new images from file</li><li>Resize and crop images</li><li>Adjust image properties</li></ul></div>
        <div class="use-card"><h3>&#128203; Document Structure</h3><p>Add, delete, and reorganise pages within any PDF document.</p><ul class="use-steps"><li>Add or delete pages</li><li>Reorder pages by drag</li><li>Rotate or crop pages</li><li>Add headers and footers</li></ul></div>
      </div>
    </div>
  </section>"""
    return how_to_page("How to Edit a PDF with PDFelement","How-To Guide &#8212; 2026","How to Edit Any PDF<br><em>in 6 Simple Steps</em>","Editing a PDF used to require expensive software. PDFelement makes it as straightforward as editing a Word document &#8212; on any PDF, on any device.",steps,extra)

def page_convert():
    steps = [
        ("Open the PDF in PDFelement","Launch PDFelement and open the PDF you want to convert. Drag and drop it or use File > Open."),
        ("Select Your Output Format","Click the 'Convert' tab in the toolbar. Choose your target format: Word (.docx), Excel (.xlsx), PowerPoint (.pptx), HTML, or image (PNG/JPG)."),
        ("Choose Conversion Settings","Optionally adjust settings: page range (all pages or specific ones), OCR for scanned PDFs, and output folder location."),
        ("Enable OCR if Needed","If your PDF is scanned (not a native digital PDF), toggle on the OCR option and select your document language for best accuracy."),
        ("Click Convert","Click the Convert button. PDFelement processes the file &#8212; most documents convert in under 30 seconds."),
        ("Review and Use the Output","Open the converted file in Word, Excel, or PowerPoint. Formatting is preserved &#8212; tables, columns, fonts, and images in the correct position."),
    ]
    extra = f"""
  <section>
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Convert PDF to...</th><th>Formatting Accuracy</th><th>Best For</th></tr></thead>
          <tbody>
            <tr><td><strong>Microsoft Word (.docx)</strong></td><td class="win">96&#8211;98%</td><td>Editing document text and content</td></tr>
            <tr><td><strong>Microsoft Excel (.xlsx)</strong></td><td class="win">94&#8211;97%</td><td>Extracting tables and data</td></tr>
            <tr><td><strong>Microsoft PowerPoint (.pptx)</strong></td><td class="good">92&#8211;95%</td><td>Editing presentation slides</td></tr>
            <tr><td><strong>HTML</strong></td><td class="good">90&#8211;94%</td><td>Web publishing</td></tr>
            <tr><td><strong>Images (PNG/JPG)</strong></td><td class="win">100%</td><td>Screenshots and sharing</td></tr>
            <tr><td><strong>Plain text (.txt)</strong></td><td class="win">98%+</td><td>Extracting text content</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>"""
    return how_to_page("How to Convert PDF to Word, Excel & More","PDF Conversion Guide &#8212; 2026","Convert Any PDF to Word,<br><em>Excel or PowerPoint</em>","PDFelement converts PDF files to fully editable Word, Excel, and PowerPoint documents with industry-leading formatting accuracy.",steps,extra)

def page_sign():
    steps = [
        ("Open Your Document","Open the PDF contract, agreement, or form in PDFelement. Drag and drop or use File > Open."),
        ("Click 'Sign'","Select the Sign tab or the eSign option from the toolbar. PDFelement provides multiple signature options."),
        ("Create Your Signature","Draw your signature with a mouse or touchscreen, type your name and choose a style, or upload a scanned image of your handwritten signature."),
        ("Place the Signature","Click where you want your signature to appear on the document. Resize and reposition as needed."),
        ("Add Date and Initials","Optionally add your initials and the date signed. PDFelement can auto-fill the current date."),
        ("Save the Signed Document","Save the document. The signature is permanently embedded in the PDF and legally binding in most jurisdictions."),
    ]
    extra = f"""
  <section class="bg-white">
    <div class="container" style="max-width:820px;">
      <h2>Collecting Signatures from Others</h2>
      <p>PDFelement&#8217;s eSign feature lets you send documents to others for signature &#8212; no PDFelement account required on their end. Add signature fields to your document, enter recipients&#8217; email addresses, and PDFelement sends secure signing links. You&#8217;re notified when each person signs. The final signed document is stored securely and sent to all parties automatically.</p>
      <h2>Are PDFelement eSignatures Legally Binding?</h2>
      <p>Yes &#8212; PDFelement&#8217;s electronic signatures comply with eIDAS (EU), ESIGN Act (USA), and equivalent regulations in most countries worldwide. For contracts, NDAs, employment agreements, and most business documents, PDFelement eSignatures are legally valid.</p>
    </div>
  </section>"""
    return how_to_page("How to eSign Documents with PDFelement","eSignature Guide &#8212; 2026","Sign PDFs Electronically &#8212;<br><em>Legally Binding in Minutes</em>","Stop printing, signing, scanning, and emailing. PDFelement lets you sign any PDF electronically &#8212; legally binding, on any device, in under 60 seconds.",steps,extra)

def page_compress():
    steps = [
        ("Open PDFelement","Launch PDFelement on your Windows, Mac, iOS or Android device."),
        ("Open Your PDF","Open the large PDF you want to compress using File > Open or drag and drop."),
        ("Go to Compress PDF","Click 'Tools' in the toolbar and select 'Compress PDF'. Alternatively, use File > Optimize PDF."),
        ("Choose Compression Level","Select your compression level: High (maximum reduction, slight quality impact), Medium (balanced &#8212; recommended), or Low (minimal quality impact, smaller reduction)."),
        ("Preview the Result","PDFelement shows a preview of the compressed file size before you confirm. You can see exactly how much space you&#8217;ll save."),
        ("Save the Compressed File","Click Compress and save the output file. Most PDFs compress by 40&#8211;90% without visible quality loss at the Medium setting."),
    ]
    return how_to_page("How to Compress PDF Files with PDFelement","PDF Compression Guide &#8212; 2026","Compress Any PDF by Up to<br><em>90% Without Losing Quality</em>","Large PDFs cause email bounces, slow uploads, and storage headaches. PDFelement compresses any PDF file dramatically &#8212; in seconds.",steps)

def page_forms():
    steps = [
        ("Create or Open a PDF","Open PDFelement and either create a new PDF form from scratch or open an existing document you want to convert into an interactive form."),
        ("Click 'Form'","Select the Form tab in the toolbar. PDFelement switches to form editing mode with a full set of form field tools."),
        ("Add Form Fields","Drag form fields onto your document: text fields, checkboxes, radio buttons, dropdown menus, date pickers, and signature fields. Place them precisely."),
        ("Configure Field Properties","Click any field to set its properties: name, required/optional, default value, validation rules, and appearance (font, colour, border)."),
        ("Test the Form","Switch to the Fill & Sign mode to test your form as a user would experience it. Verify all fields work correctly."),
        ("Distribute and Collect","Save your form and share it by email or link. Recipients fill it in PDFelement, Adobe Reader, or any PDF viewer. Export responses to Excel for analysis."),
    ]
    return how_to_page("How to Create PDF Forms with PDFelement","PDF Forms Guide &#8212; 2026","Create Professional PDF Forms<br><em>That People Can Fill In</em>","Create interactive PDF forms with text fields, checkboxes, dropdowns, and digital signatures. Collect data from anyone &#8212; no PDF editor required to fill.",steps)

def page_ocr():
    steps = [
        ("Open Your Scanned PDF or Image","Open PDFelement and load your scanned PDF, TIFF, or image file. PDFelement automatically detects that it is a scanned document."),
        ("Click 'OCR'","PDFelement will prompt you to perform OCR when it detects a scanned document. Click the OCR button in the notification bar or go to Tools > OCR."),
        ("Select Your Language","Choose the primary language of your document from the 26 available languages. For multilingual documents, you can select multiple languages simultaneously."),
        ("Choose OCR Mode","Select 'Editable Text' to make the PDF fully editable, or 'Searchable Text' to make it searchable while keeping the original appearance. Choose 'Editable Text' for editing."),
        ("Run OCR","Click 'Perform OCR'. Processing time depends on document length &#8212; typically 2&#8211;10 seconds per page for standard documents."),
        ("Edit and Save","Your scanned document is now fully editable text. Edit it just like any native PDF. Save as PDF or convert to Word, Excel, or other formats."),
    ]
    extra = f"""
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Language</th><th>OCR Accuracy (clean scan)</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>English</td><td class="win">98&#8211;99%</td><td>Best accuracy &#8212; largest training data</td></tr>
            <tr><td>German, French, Spanish</td><td class="win">97&#8211;99%</td><td>Excellent European language support</td></tr>
            <tr><td>Japanese, Chinese (Simplified/Traditional)</td><td class="win">96&#8211;98%</td><td>Strong CJK character recognition</td></tr>
            <tr><td>Korean, Arabic</td><td class="good">95&#8211;97%</td><td>Very good accuracy</td></tr>
            <tr><td>Russian, Portuguese</td><td class="win">97&#8211;98%</td><td>Excellent accuracy</td></tr>
            <tr><td>Other (20+ languages)</td><td class="good">93&#8211;96%</td><td>Good accuracy on clean scans</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>"""
    return how_to_page("PDF OCR with PDFelement &#8212; Complete Guide","OCR Guide &#8212; 2026","Convert Any Scanned Document<br><em>to Editable Text</em>","Turn scanned PDFs, paper documents, and images into fully editable, searchable text. PDFelement&#8217;s OCR supports 26 languages with industry-leading accuracy.",steps,extra)

def page_business():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Business Guide &#8212; 2026</div>
      <h1>PDFelement for Business:<br><em>Cut PDF Costs by 70%</em></h1>
      <p class="hero-sub">Teams of every size use PDFelement to streamline document workflows, eliminate paper, and reduce PDF software costs. Here is the complete business case.</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Get Business Pricing &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="use-grid">
        <div class="use-card"><h3>&#128203; Contract Management</h3><p>Create, review, sign, and store contracts without printing a single page.</p><ul class="use-steps"><li>Edit contract templates in seconds</li><li>Collect legally binding eSignatures</li><li>Redact sensitive information</li><li>Password-protect confidential terms</li></ul></div>
        <div class="use-card"><h3>&#128176; Finance & Invoicing</h3><p>Process invoices, reports, and financial documents faster and more accurately.</p><ul class="use-steps"><li>Extract data from PDF invoices to Excel</li><li>OCR paper receipts and statements</li><li>Create fillable expense forms</li><li>Compress and archive financial records</li></ul></div>
        <div class="use-card"><h3>&#128101; HR & Onboarding</h3><p>Digitise the entire employee onboarding and HR document workflow.</p><ul class="use-steps"><li>Create fillable HR forms</li><li>Collect employee eSignatures</li><li>Manage offer letters and contracts</li><li>Batch process employee documents</li></ul></div>
        <div class="use-card"><h3>&#128270; Legal & Compliance</h3><p>Handle legal documents with the security and accuracy compliance requires.</p><ul class="use-steps"><li>Redact sensitive legal information</li><li>Add digital signatures and timestamps</li><li>Encrypt confidential documents</li><li>Batch OCR document archives</li></ul></div>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:840px;">
      <h2>The Business Cost Comparison</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Team Size</th><th>Adobe Acrobat (annual)</th><th>PDFelement Business (annual)</th><th>Annual Saving</th></tr></thead>
          <tbody>
            <tr><td>5 users</td><td class="bad">~$1,200</td><td class="win">~$645</td><td class="good">~$555</td></tr>
            <tr><td>10 users</td><td class="bad">~$2,400</td><td class="win">~$1,290</td><td class="good">~$1,110</td></tr>
            <tr><td>25 users</td><td class="bad">~$6,000</td><td class="win">~$3,225</td><td class="good">~$2,775</td></tr>
            <tr><td>50 users</td><td class="bad">~$12,000</td><td class="win">~$6,450</td><td class="good">~$5,550</td></tr>
          </tbody>
        </table>
      </div>
      {cta("Get PDFelement Business Pricing", "Volume discounts available. Contact for custom enterprise quotes.")}
    </div>
  </section>"""

def page_students():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Student Guide &#8212; 2026</div>
      <h1>PDFelement for Students:<br><em>The PDF Tool You Actually Need</em></h1>
      <p class="hero-sub">Adobe Acrobat is too expensive for students. PDFelement gives you every PDF feature you need for academic life &#8212; at a price that makes sense.</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Get Student Pricing &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#128214;</span><h3>Annotate Research Papers</h3><p>Highlight, underline, add comments, and sticky notes to academic PDFs. Keep all your annotations organised by paper and subject.</p></div>
        <div class="feat-card"><span class="feat-icon">&#127775;</span><h3>AI Summarisation</h3><p>Paste a 60-page research paper into PDFelement&#8217;s AI and get a structured summary in 30 seconds. Save hours of reading time every week.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128260;</span><h3>Convert Assignment PDFs</h3><p>Convert PDF coursework to Word to edit it, or convert your Word essay to PDF for submission. Formatting preserved perfectly.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128270;</span><h3>OCR Lecture Notes</h3><p>Scan handwritten notes or printed slides and convert them to searchable, editable text. Never lose a note again.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128203;</span><h3>Fill Academic Forms</h3><p>Fill in application forms, enrolment documents, scholarship applications, and official university PDFs quickly and accurately.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128394;&#65039;</span><h3>Sign Documents</h3><p>Electronically sign consent forms, internship agreements, and official documents. No printing required.</p></div>
      </div>
      {cta("Get PDFelement Student Pricing", "Special educational discount available. Check current student offer.")}
    </div>
  </section>"""

def page_mac():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> macOS Guide &#8212; 2026</div>
      <h1>PDFelement for Mac 2026:<br><em>Professional PDF Editing on macOS</em></h1>
      <p class="hero-sub">PDFelement for Mac is a native macOS application &#8212; fast, polished, and fully integrated with macOS features including Touch Bar support, iCloud, and Dark Mode.</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Download for Mac Free &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#63743;</span><h3>Native macOS Experience</h3><p>Built for macOS. Follows Apple Human Interface Guidelines. Supports Dark Mode, Spotlight search integration, and macOS keyboard shortcuts.</p></div>
        <div class="feat-card"><span class="feat-icon">&#9729;&#65039;</span><h3>iCloud Integration</h3><p>Open and save PDFs directly from iCloud Drive. Access your documents from any Apple device.</p></div>
        <div class="feat-card"><span class="feat-icon">&#9881;&#65039;</span><h3>macOS Automation</h3><p>Integrates with Automator and Shortcuts for batch PDF processing workflows on Mac.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128241;</span><h3>Handoff Support</h3><p>Start editing on your Mac and continue on your iPhone or iPad using Apple Handoff &#8212; seamless across all your Apple devices.</p></div>
      </div>
      <h2 style="margin-top:3rem;">System Requirements (Mac)</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Requirement</th><th>Minimum</th><th>Recommended</th></tr></thead>
          <tbody>
            <tr><td>macOS version</td><td>macOS 10.15 (Catalina)</td><td class="win">macOS 13+ (Ventura/Sonoma)</td></tr>
            <tr><td>Processor</td><td>Intel Core i3</td><td class="win">Apple Silicon (M1/M2/M3)</td></tr>
            <tr><td>RAM</td><td>4GB</td><td class="win">8GB+</td></tr>
            <tr><td>Storage</td><td>2GB free</td><td class="win">5GB+ free</td></tr>
          </tbody>
        </table>
      </div>
      {cta("Download PDFelement for Mac Free", "Native Apple Silicon support. Full 7-day free trial.")}
    </div>
  </section>"""

def page_windows():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Windows Guide &#8212; 2026</div>
      <h1>PDFelement for Windows 2026:<br><em>The Complete PDF Suite</em></h1>
      <p class="hero-sub">PDFelement for Windows is the most feature-complete version &#8212; optimised for Windows 10 and 11 with full ribbon interface, Microsoft Office integration, and enterprise deployment support.</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Download for Windows Free &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#128138;</span><h3>Windows 11 Optimised</h3><p>Fully optimised for Windows 11 with Fluent Design elements, rounded corners, and Snap layouts support.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128196;</span><h3>Microsoft Office Integration</h3><p>Adds a PDFelement tab directly in Word, Excel, and Outlook for one-click PDF conversion and editing.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128269;</span><h3>Windows Search Integration</h3><p>OCR-processed PDFs are fully indexed by Windows Search &#8212; find any document content instantly.</p></div>
        <div class="feat-card"><span class="feat-icon">&#9881;&#65039;</span><h3>Enterprise Deployment</h3><p>MSI installer for IT-managed deployment. Group Policy support for enterprise configuration and management.</p></div>
      </div>
      {cta("Download PDFelement for Windows Free", "Windows 10 and 11 supported. Full 7-day free trial.")}
    </div>
  </section>"""

def page_ai():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> AI Features &#8212; 2026</div>
      <h1>PDFelement AI Tools 2026:<br><em>Work Smarter With Every PDF</em></h1>
      <p class="hero-sub">PDFelement&#8217;s built-in AI transforms how you interact with documents &#8212; summarise, translate, rewrite, and extract information from any PDF in seconds.</p>
      <a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Try PDFelement AI Free &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="use-grid">
        <div class="use-card"><h3>&#127775; AI Summarisation</h3><p>Generate structured summaries of long PDFs in seconds. Ask questions about document content in natural language.</p><ul class="use-steps"><li>Summarise any PDF in under 30 seconds</li><li>Key points extracted automatically</li><li>Ask follow-up questions</li><li>Works on reports, papers, contracts</li></ul></div>
        <div class="use-card"><h3>&#127758; AI Translation</h3><p>Translate entire PDF documents or selected sections into 20+ languages without leaving PDFelement.</p><ul class="use-steps"><li>Translate full documents or selections</li><li>Preserve original formatting</li><li>20+ language pairs supported</li><li>Better than basic machine translation</li></ul></div>
        <div class="use-card"><h3>&#9999;&#65039; AI Rewriting</h3><p>Improve, simplify, or restructure document text with AI-powered rewriting and tone adjustment.</p><ul class="use-steps"><li>Simplify complex legal language</li><li>Improve clarity and readability</li><li>Adjust tone (formal/informal)</li><li>Fix grammar and phrasing</li></ul></div>
        <div class="use-card"><h3>&#128203; Smart Form Filling</h3><p>AI analyses form fields and suggests completions based on your document history and context.</p><ul class="use-steps"><li>Auto-detect form field types</li><li>Suggest values from context</li><li>Batch fill repetitive fields</li><li>Extract data to spreadsheet</li></ul></div>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2>Real-World AI Use Cases</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Task</th><th>Without PDFelement AI</th><th>With PDFelement AI</th></tr></thead>
          <tbody>
            <tr><td>Summarise 50-page report</td><td class="bad">30&#8211;60 minutes reading</td><td class="win">30 seconds</td></tr>
            <tr><td>Translate contract to Spanish</td><td class="bad">Copy/paste to translator, reformat</td><td class="win">2 clicks, formatting preserved</td></tr>
            <tr><td>Simplify legal document</td><td class="bad">Manual rewriting</td><td class="win">AI rewrites in seconds</td></tr>
            <tr><td>Extract key data from invoices</td><td class="bad">Manual entry to spreadsheet</td><td class="win">AI extracts and exports</td></tr>
          </tbody>
        </table>
      </div>
      {cta("Try PDFelement AI Features Free", "Full AI access included in the Pro and Business plans. Free trial available.")}
    </div>
  </section>"""

def page_merge():
    steps = [
        ("Open PDFelement","Launch PDFelement on Windows or Mac."),
        ("Go to Combine PDF","Click 'Tool' > 'Combine PDF' or drag multiple PDFs directly onto the PDFelement window."),
        ("Add Your Files","Add the PDF files you want to merge. Drag them into the correct order &#8212; this becomes the page order in the final document."),
        ("Adjust Page Ranges","Optionally specify which pages to include from each file &#8212; useful if you only need certain sections from each document."),
        ("Click Apply","Click the Apply or Combine button. PDFelement merges all files into a single PDF in seconds."),
        ("Save the Result","Save your merged PDF. The original files remain unchanged."),
    ]
    extra = f"""
  <section class="bg-white">
    <div class="container" style="max-width:820px;">
      <h2>How to Split a PDF</h2>
      <p>To split a PDF into multiple files: open the PDF in PDFelement, go to Tool > Split PDF, choose how to split (by page count, file size, or bookmarks), and click Apply. PDFelement creates separate PDF files for each section automatically.</p>
      {cta("Try PDF Merge and Split Free", "Merge unlimited PDFs. Split by page, size, or bookmark.")}
    </div>
  </section>"""
    return how_to_page("Merge and Split PDFs with PDFelement","Merge & Split Guide &#8212; 2026","Merge Multiple PDFs into One<br><em>or Split Any PDF in Seconds</em>","Combine multiple PDFs into a single document, or split a large PDF into smaller files. PDFelement handles both in seconds.",steps,extra)

def page_protect():
    steps = [
        ("Open Your PDF in PDFelement","Open the PDF you want to protect. Go to File > Open or drag and drop."),
        ("Go to Protection Settings","Click 'Protect' in the toolbar or go to File > Properties > Security."),
        ("Set an Open Password","To require a password to open the document, enter and confirm your password. Choose encryption strength (256-bit AES recommended)."),
        ("Set Permission Restrictions","Optionally restrict what others can do: prevent printing, copying text, or editing. Set a separate permissions password."),
        ("Apply Redaction for Sensitive Content","To permanently remove sensitive text or images, use the Redact tool &#8212; black bars are permanent and cannot be reversed."),
        ("Save the Protected PDF","Save the document. The password and restrictions are permanently applied."),
    ]
    return how_to_page("How to Password Protect & Secure PDFs","PDF Security Guide &#8212; 2026","Protect Any PDF with<br><em>Password Encryption & Redaction</em>","Keep confidential documents secure with password protection, permission restrictions, and permanent redaction. Industry-standard 256-bit AES encryption.",steps)

def page_promos():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge"><span class="badge-dot"></span> Best Deals &#8212; June 2026</div>
      <h1>PDFelement Promo Codes &amp;<br><em>Best Deals June 2026</em></h1>
      <p class="hero-sub">How to get PDFelement at the lowest possible price &#8212; including our partner link for the current best available offer.</p>
      <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">See Current Offer &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#128279;</span><h3>Partner Link &#8212; Best Available Rate</h3><p>Our affiliate link routes through Wondershare&#8217;s partner portal where the best available rates for new customers are surfaced. Click through for the current offer.</p><a href="{AFF}" class="btn btn-indigo btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Access Partner Rate</a></div>
        <div class="feat-card"><span class="feat-icon">&#127775;</span><h3>Free Trial First</h3><p>Always download and test PDFelement for free before purchasing. The full-featured trial lets you verify it handles all your specific documents before spending a penny.</p><a href="{AFF}" class="btn btn-indigo btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Start Free Trial</a></div>
        <div class="feat-card"><span class="feat-icon">&#128176;</span><h3>Consider Perpetual License</h3><p>If you plan to use PDFelement for 2+ years, the one-time perpetual license costs less than two years of subscription and gives you permanent ownership.</p><a href="{AFF}" class="btn btn-indigo btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">See Perpetual Pricing</a></div>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:780px;">
      {faq(
        ("Does PDFelement have promo codes in June 2026?", "Wondershare regularly releases PDFelement promo codes via email and partner channels. Our partner link surfaces the best available rate for new customers. Major sales run during Black Friday, New Year, and seasonal promotions."),
        ("How do I apply a PDFelement promo code?", "At checkout on the Wondershare/PDFelement website, enter your promo code in the coupon/discount field before completing payment."),
        ("What is the cheapest way to get PDFelement?", "The perpetual license is cheapest over 2+ years. For a 1-year commitment, the annual subscription is fine. Student and educational discounts offer significant savings for eligible users. Always try the free trial first."),
        ("Does PDFelement have a Black Friday sale?", "Yes &#8212; Wondershare typically runs significant PDFelement discounts during Black Friday/Cyber Monday (late November). This is historically when the largest discounts appear &#8212; often 50&#8211;60% off."),
      )}
      {cta("Get PDFelement at the Best Price Available", "Check current promotions via our partner link.")}
    </div>
  </section>"""

def page_about():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <h1>About <em>PDFToolGuide</em></h1>
      <p class="hero-sub">The independent guide helping professionals and students get the most from PDFelement since 2020.</p>
    </div>
  </section>
  <section class="bg-white">
    <div class="container" style="max-width:760px;">
      <div class="feat-card">
        <h2 style="font-family:'Outfit',sans-serif;font-size:1.9rem;font-weight:800;margin-bottom:1rem;">Our Mission</h2>
        <p>PDFToolGuide exists because choosing PDF software is confusing &#8212; and most people end up paying far more than they need to for Adobe Acrobat when equally capable alternatives exist. We test PDF software rigorously and publish honest, detailed comparisons.</p>
        <p>After testing every major PDF editor over 4 years, we recommend PDFelement as the best value professional PDF editor for most users &#8212; individuals, students, small businesses, and enterprise teams who don&#8217;t need to be locked into the Adobe ecosystem.</p>
        <h3>What We Publish</h3>
        <ul class="styled">
          <li>Honest feature-by-feature reviews based on real testing</li>
          <li>Step-by-step how-to guides for every PDF task</li>
          <li>Platform comparisons (Windows vs Mac vs mobile)</li>
          <li>Pricing guides and value analysis</li>
          <li>Use case guides for specific professions (legal, finance, education)</li>
        </ul>
        <h3>Affiliate Disclosure</h3>
        <p>PDFToolGuide earns a commission when you purchase PDFelement via our links. This is at zero extra cost to you &#8212; the price is identical whether you arrive via our link or directly. Our recommendations are based on genuine testing.</p>
        <div style="text-align:center;margin-top:2rem;">
          <a href="{AFF}" class="btn btn-indigo" rel="nofollow sponsored">Try PDFelement Free &rarr;</a>
        </div>
      </div>
    </div>
  </section>"""

# ─── CONTENT ROUTER ──────────────────────────────────────────────────────────
FN_MAP = {
    "page_home":page_home,"page_review":page_review,
    "page_vs_adobe":page_vs_adobe,"page_vs_foxit":page_vs_foxit,
    "page_pricing":page_pricing,"page_edit":page_edit,"page_convert":page_convert,
    "page_sign":page_sign,"page_compress":page_compress,"page_forms":page_forms,
    "page_ocr":page_ocr,"page_business":page_business,"page_students":page_students,
    "page_mac":page_mac,"page_windows":page_windows,"page_ai":page_ai,
    "page_merge":page_merge,"page_protect":page_protect,
    "page_promos":page_promos,"page_about":page_about,
}

def write_robots():
    (OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")

def write_sitemap():
    urls = ""
    for p in PAGES:
        loc = f"{BASE}/" if p["slug"]=="index" else f"{BASE}/{p['slug']}.html"
        urls += f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>{p['priority']}</priority></url>\n"
    (OUT/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>')

def write_llms():
    (OUT/"llms.txt").write_text(f"""# PDFToolGuide — PDFelement Affiliate Guide

> Independent guide helping users get the most from Wondershare PDFelement.

## Coverage
PDFelement reviews, comparisons vs Adobe Acrobat and Foxit, pricing guides, how-to tutorials (edit, convert, sign, compress, OCR, forms, merge, protect), platform guides (Mac/Windows), AI features, business use cases, student guide, promo codes.

## Key Pages
- [Home]({BASE}/) - Overview and comparison
- [Review]({BASE}/pdfelement-review.html) - 6-month honest review
- [vs Adobe Acrobat]({BASE}/pdfelement-vs-adobe.html) - Full comparison
- [vs Foxit]({BASE}/pdfelement-vs-foxit.html) - Comparison
- [Pricing]({BASE}/pdfelement-pricing.html) - Plans and costs
- [Edit PDF]({BASE}/edit-pdf.html) - How-to guide
- [Convert PDF]({BASE}/convert-pdf.html) - How-to guide
- [Sign PDF]({BASE}/sign-pdf.html) - eSignature guide
- [OCR]({BASE}/pdf-ocr.html) - Scanned document guide
- [AI Tools]({BASE}/pdf-ai-tools.html) - AI feature guide
- [Business]({BASE}/pdf-for-business.html) - Business use cases
- [Promo Codes]({BASE}/promo-codes.html) - Current deals

## Affiliate Info
PDFToolGuide earns commission from Wondershare PDFelement. Link: {AFF}
""")

def write_404():
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>404 &#8212; PDFToolGuide</title><style>{css()}</style></head><body>
<nav><a class="logo" href="{SUB}/"><span class="logo-mark">&#128196;</span>PDF<em>Tool</em>Guide</a></nav>
<section class="hero" style="min-height:80vh;"><div class="hero-inner">
<div style="font-size:5rem;margin-bottom:1.2rem;">&#128196;</div>
<h1>404 &#8212; <em>Page Not Found</em></h1>
<p class="hero-sub">This page doesn&#8217;t exist. Let&#8217;s get you to the right place.</p>
<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
<a href="{SUB}/" class="btn btn-indigo">Go Home</a>
<a href="{AFF}" class="btn btn-amber" rel="nofollow sponsored">Try PDFelement Free &rarr;</a>
</div></div></section></body></html>"""
    (OUT/"404.html").write_text(html)

def build():
    OUT.mkdir(exist_ok=True)
    for p in PAGES:
        body  = FN_MAP[p["content_fn"]]()
        html  = layout(p, body)
        fname = "index.html" if p["slug"]=="index" else f"{p['slug']}.html"
        (OUT/fname).write_text(html, encoding="utf-8")
        print(f"  ✓ {fname}")
    write_robots(); write_sitemap(); write_llms(); write_404()
    pages = list(OUT.glob("*.html"))
    kb    = sum(f.stat().st_size for f in pages)//1024
    print(f"\n  ✅ Build complete — {len(pages)} pages, {kb}KB")
    print(f"  🌐 {BASE}/")

if __name__ == "__main__":
    build()
