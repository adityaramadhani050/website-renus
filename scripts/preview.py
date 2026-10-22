#!/usr/bin/env python3
"""Buat pratinjau statis homepage (perkiraan tampilan, bukan render WordPress asli).

Meniru CSS layout yang biasanya dihasilkan WordPress (columns, buttons, gallery,
cover, constrained layout) dan mengganti Query Loop dengan 3 artikel contoh.

Pemakaian: python3 scripts/build.py && python3 scripts/preview.py
Hasil:     build/preview.html
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"

WP_EMULATION = """
*,*::before,*::after{box-sizing:border-box}
body{margin:0;font-family:"Source Sans Pro","Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:17px;line-height:1.6;color:#2D3B45;background:#fff}
img{max-width:100%;height:auto;display:block}
a{color:#039CFC}
h1,h2,h3{font-weight:800;line-height:1.25}
.pv-header{position:sticky;top:0;z-index:50;background:#fff;box-shadow:0 1px 8px rgba(0,0,0,.08);display:flex;align-items:center;justify-content:space-between;padding:14px 32px}
.pv-logo{font-weight:800;font-size:20px;color:#00384F;letter-spacing:.5px}
.pv-nav{display:flex;gap:22px;font-size:15px;font-weight:600}
.pv-nav a{color:#00384F;text-decoration:none}
.pv-footer{background:#011B26;color:rgba(255,255,255,.7);text-align:center;padding:28px 16px;font-size:14px}
.pv-wa{position:fixed;right:30px;bottom:30px;background:#2db742;color:#fff;border-radius:999px;padding:12px 18px;font-weight:700;font-size:14px;box-shadow:0 6px 18px rgba(0,0,0,.2);z-index:60}
.pv-note{background:#FFF7E0;color:#7A5B00;font-size:13px;text-align:center;padding:6px}
/* layout constrained */
.wp-block-group,.wp-block-cover__inner-container{padding-left:24px;padding-right:24px}
.wp-block-group>*,.wp-block-cover__inner-container>*{max-width:1200px;margin-left:auto;margin-right:auto}
.wp-block-group>.wp-block-columns{max-width:1200px}
/* columns */
.wp-block-columns{display:flex;gap:32px;align-items:stretch;margin-bottom:24px}
.wp-block-columns.are-vertically-aligned-center{align-items:center}
.wp-block-column{flex:1 1 0;min-width:0}
.wp-block-column[style*="flex-basis"]{flex-grow:0}
/* buttons */
.wp-block-buttons{display:flex;flex-wrap:wrap;gap:12px}
.wp-block-buttons[data-center]{justify-content:center}
.wp-block-button__link{display:inline-block;text-decoration:none;text-align:center}
/* cover */
.wp-block-cover{position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden;padding:48px 0}
.wp-block-cover__background{position:absolute;inset:0;z-index:1}
.has-background-dim-70{opacity:.7}
.wp-block-cover__image-background{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;max-width:none}
.wp-block-cover__inner-container{position:relative;z-index:2;width:100%}
/* image */
.wp-block-image{margin:0 0 16px}
.wp-block-image.is-resized img{width:56px}
/* gallery */
.wp-block-gallery{display:grid;gap:16px;margin:0 0 24px;padding:0}
.wp-block-gallery.columns-3{grid-template-columns:repeat(3,1fr)}
.wp-block-gallery.columns-7{grid-template-columns:repeat(7,1fr);align-items:center}
.wp-block-gallery .wp-block-image{margin:0}
.wp-block-gallery.is-cropped .wp-block-image img{width:100%;aspect-ratio:4/3;object-fit:cover}
.has-text-align-center{text-align:center}
/* query mock */
.pv-posts{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:24px}
.pv-posts img{width:100%;aspect-ratio:16/9;object-fit:cover}
@media (max-width:781px){
  .pv-nav{display:none}
  .wp-block-columns{flex-direction:column}
  .wp-block-column[style*="flex-basis"]{flex-basis:auto!important}
  .wp-block-gallery.columns-3,.pv-posts{grid-template-columns:1fr}
  .wp-block-gallery.columns-7{grid-template-columns:repeat(3,1fr)}
}
"""

MOCK_POSTS = [
    ("Panduan Panel Listrik Tenaga Surya 2026: Biaya &amp; ROI", "21 September 2026",
     "https://renergynusantara.com/wp-content/uploads/2026/09/solar-panel-sky-background-scaled.jpg"),
    ("Investasi PLTS di 2026: Apakah Masih Menguntungkan?", "25 Juni 2026",
     "https://renergynusantara.com/wp-content/uploads/2025/02/DJI_0058.avif"),
    ("Kontraktor PLTS Surabaya Terpercaya untuk Rumah, Bisnis, dan Industri", "17 Juni 2026",
     "https://renergynusantara.com/wp-content/uploads/2025/11/Gemini_Generated_Image_eguj5peguj5peguj.avif"),
]


def mock_query() -> str:
    cards = "".join(
        f'<div class="rn-post-grid"><figure class="wp-block-post-featured-image"><img src="{img}" alt=""></figure>'
        f'<h3 class="wp-block-post-title"><a href="#">{title}</a></h3>'
        f'<div class="wp-block-post-date">{date}</div></div>'
        for title, date, img in MOCK_POSTS
    )
    return f'<div class="pv-posts">{cards}</div>'


def main() -> None:
    content = (BUILD / "homepage.html").read_text(encoding="utf-8")
    content = re.sub(r"<!-- wp:query .*?<!-- /wp:query -->", lambda _m: mock_query(), content, flags=re.S)
    content = content.replace(
        '<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n<div class="wp-block-buttons">',
        '<div class="wp-block-buttons" data-center>',
    )
    css = (ROOT / "blocks" / "homepage.css").read_text(encoding="utf-8")
    page = f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pratinjau Homepage Renus</title>
<style>{WP_EMULATION}</style>
<style>{css}</style>
</head>
<body>
<div class="pv-note">Pratinjau statis — perkiraan tampilan. Header/footer asli dari Kadence; artikel di bawah hanya contoh.</div>
<header class="pv-header"><span class="pv-logo">RENUS</span>
<nav class="pv-nav"><a href="#">Beranda</a><a href="#">Tentang Kami</a><a href="#">Layanan</a><a href="#">Produk</a><a href="#">Proyek</a><a href="#">Artikel</a><a href="#">Hubungi Kami</a></nav></header>
<main>
{content}
</main>
<footer class="pv-footer">© Renus Global Indonesia — footer Kadence</footer>
<span class="pv-wa">💬 Butuh bantuan? Chat kami</span>
</body>
</html>
"""
    (BUILD / "preview.html").write_text(page, encoding="utf-8")
    print("build/preview.html")


if __name__ == "__main__":
    main()
