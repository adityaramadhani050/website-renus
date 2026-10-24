#!/usr/bin/env python3
"""Bangun markup blok Gutenberg + CSS homepage dari prototipe.

Sumber: prototypes/landing-plts-hybrid.html (hasil iterasi yang sudah disetujui).
Keluaran:
  wordpress/homepage/homepage.blocks.html  -> isi halaman (wp_create_page / wp_update_page)
  wordpress/homepage/rn.css                -> blok CSS ".rn" untuk Additional CSS Kadence

Aturan:
- Teks statis memakai blok inti (group, heading, paragraph, image, list, table,
  details, buttons, latest-posts) supaya bisa diedit lewat editor/MCP.
- Bagian interaktif (hero, kartu isometrik, tab paket, kalkulator, kartu kontak,
  tombol WA mengambang, skrip) memakai blok Custom HTML.
- Semua CSS di-scope ke "body .rn" agar tidak mengganggu halaman lain.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "prototypes" / "landing-plts-hybrid.html"
OUT = Path(__file__).resolve().parent
UP = "https://renergynusantara.com/wp-content/uploads/"
WA = "https://wa.me/6281412250644"

proto = SRC.read_text(encoding="utf-8")
lines = proto.splitlines()


def between(start_pat, end_pat, include_end=True):
    """Ambil potongan prototipe dari baris yang cocok start_pat sampai end_pat."""
    s = next(i for i, l in enumerate(lines) if re.search(start_pat, l))
    e = next(i for i in range(s, len(lines)) if re.search(end_pat, lines[i]))
    return "\n".join(lines[s : e + (1 if include_end else 0)])


# ---------- pembungkus blok ----------
def attrs(d):
    d = {k: v for k, v in d.items() if v not in (None, "", False)}
    return (" " + json.dumps(d, ensure_ascii=False, separators=(",", ":"))) if d else ""


def cls(*names):
    return " ".join(n for n in names if n)


def group(children, tag="div", cls_=None, anchor=None, align=None):
    a = {"tagName": tag if tag != "div" else None, "anchor": anchor, "align": align,
         "className": cls_, "layout": {"type": "default"}}
    klass = cls("wp-block-group", f"align{align}" if align else None, cls_)
    idattr = f' id="{anchor}"' if anchor else ""
    inner = "\n".join(children)
    return f"<!-- wp:group{attrs(a)} -->\n<{tag}{idattr} class=\"{klass}\">\n{inner}\n</{tag}>\n<!-- /wp:group -->"


def p(html, cls_=None):
    c = f' class="{cls_}"' if cls_ else ""
    return f"<!-- wp:paragraph{attrs({'className': cls_})} -->\n<p{c}>{html}</p>\n<!-- /wp:paragraph -->"


def h(html, level=2, cls_=None):
    a = {"level": level if level != 2 else None, "className": cls_}
    return (f"<!-- wp:heading{attrs(a)} -->\n<h{level} class=\"{cls('wp-block-heading', cls_)}\">"
            f"{html}</h{level}>\n<!-- /wp:heading -->")


def img(id_, path, alt, cls_=None, caption=None):
    a = {"id": id_, "sizeSlug": "full", "linkDestination": "none", "className": cls_}
    cap = f'<figcaption class="wp-element-caption">{caption}</figcaption>' if caption else ""
    return (f"<!-- wp:image{attrs(a)} -->\n<figure class=\"{cls('wp-block-image size-full', cls_)}\">"
            f"<img src=\"{UP}{path}\" alt=\"{alt}\" class=\"wp-image-{id_}\"/>{cap}</figure>\n<!-- /wp:image -->")


def ul(items, cls_=None, ordered=False):
    tag = "ol" if ordered else "ul"
    a = {"ordered": ordered, "className": cls_}
    li = "\n".join(f"<!-- wp:list-item -->\n<li>{t}</li>\n<!-- /wp:list-item -->" for t in items)
    return f"<!-- wp:list{attrs(a)} -->\n<{tag} class=\"{cls('wp-block-list', cls_)}\">\n{li}\n</{tag}>\n<!-- /wp:list -->"


def button(text, href, variant, external=False):
    a = {"className": variant, "linkTarget": "_blank" if external else None,
         "rel": "noreferrer noopener" if external else None}
    tgt = ' target="_blank" rel="noreferrer noopener"' if external else ""
    return (f"<!-- wp:button{attrs(a)} -->\n<div class=\"{cls('wp-block-button', variant)}\">"
            f"<a class=\"wp-block-button__link wp-element-button\" href=\"{href}\"{tgt}>{text}</a></div>\n<!-- /wp:button -->")


def buttons(*btns):
    return "<!-- wp:buttons -->\n<div class=\"wp-block-buttons\">\n" + "\n".join(btns) + "\n</div>\n<!-- /wp:buttons -->"


def details(q, a):
    return (f"<!-- wp:details -->\n<details class=\"wp-block-details\"><summary>{q}</summary>"
            f"{p(a)}</details>\n<!-- /wp:details -->")


def html(raw):
    return f"<!-- wp:html -->\n{raw.strip()}\n<!-- /wp:html -->"


def more(text, href):
    return p(f'<a href="{href}">{text}</a>', "more")


def sec_head(eyebrow, title, link=None):
    kids = [group([p(eyebrow, "eyebrow"), h(title, 2, "h2")])]
    if link:
        kids.append(more(*link))
    return group(kids, cls_="sec-head")


def section(anchor, children, cls_=None):
    return group(children, tag="section", cls_=cls_, anchor=anchor)


# ---------- aset WordPress ----------
HERO = {  # id media: 1920 / 1024 (unggahan 24 Okt 2026)
    "siang": "2026/10/hero-plts-hybrid-siang",
    "mendung": "2026/10/hero-plts-hybrid-mendung",
    "malam": "2026/10/hero-plts-hybrid-malam",
    "pln-padam": "2026/10/hero-plts-hybrid-pln-padam",
}


def wp_assets(raw):
    for k, base in HERO.items():
        raw = raw.replace(f"assets/hero-plts-hybrid-{k}-1920.webp", f"{UP}{base}.webp")
        raw = raw.replace(f"assets/hero-plts-hybrid-{k}-1024.webp", f"{UP}{base}-hp.webp")
    for k, slug in (("ongrid", "on-grid"), ("offgrid", "off-grid"), ("hybrid", "hybrid")):
        url = f"{UP}2026/10/isometrik-plts-{slug}.webp"
        raw = raw.replace(
            f' srcset="assets/isometrik-plts-{k}-480.webp 480w, assets/isometrik-plts-{k}-800.webp 800w" sizes="(max-width:960px) 90vw, 30vw"', "")
        raw = raw.replace(f"assets/isometrik-plts-{k}-800.webp", url)
    assert "assets/" not in raw, "masih ada path aset lokal"
    return raw


# ---------- 1. Hero ----------
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap">')
hero = html(FONTS + "\n" + wp_assets(between(r'<section class="hero"', r"^</section>")))

# ---------- 2. Proyek ----------
gallery = group([
    img(4810, "2024/10/DJI_0017-scaled.jpg", "Foto udara PLTS atap pabrik hasil pemasangan Renus", "photo proj-main",
        "<strong>PLTS atap industri</strong>Foto udara proyek Renus"),
    img(3487, "2023/03/JIIPe-e1680162481413.jpg", "PLTS atap di kawasan industri JIIPe", "photo",
        "<strong>Kawasan industri JIIPe</strong>Industrial"),
    img(3289, "2023/03/DJI_0441-2-scaled.jpg", "Foto udara deretan panel surya di atap gedung komersial", "photo",
        "<strong>Gedung komersial</strong>Komersial"),
    img(4743, "2024/09/WhatsApp-Image-2024-09-02-at-09.35.08-2-scaled.jpeg", "PLTS atap rumah tinggal hasil pemasangan Renus", "photo",
        "<strong>Rumah tinggal</strong>Residensial"),
], cls_="proj-grid")
CLIENTS = [
    (4063, "2024/01/Untitled-3-01-3.png", "WIKA"),
    (4060, "2024/01/Untitled-3-01.png", "Medco Energi"),
    (3856, "2023/10/Logo_PU_RGB-scaled.jpg", "Kementerian PUPR"),
    (3814, "2023/09/lambang-its-png-v2.png", "Institut Teknologi Sepuluh Nopember (ITS)"),
    (3796, "2023/09/JATIM-1-e1695633415190.png", "Perpustakaan Jawa Timur"),
    (4064, "2024/01/Untitled-3-01-4.png", "Minarta"),
    (4066, "2024/01/Untitled-3-01-6.png", "Politeknik Negeri Madiun"),
    (4067, "2024/01/Untitled-3-01-7.png", "Poltera"),
    (4065, "2024/01/Untitled-3-01-5.png", "YSUN"),
    (3784, "2023/09/Logo-Biru-Muda.png", "UHT"),
    (4061, "2024/01/Untitled-3-01-1.png", "PJU"),
    (4062, "2024/01/Untitled-3-01-2.png", "PJUC"),
    (4072, "2024/01/Untitled-3-01-8.png", "Logo klien Renus"),
    (4073, "2024/01/Untitled-3-01-9.png", "Logo klien Renus"),
]
proyek = section("proyek", [
    group([group([p("Proyek", "eyebrow"), h("Terpasang di atap rumah, gedung, dan pabrik.", 2, "h2")]),
           more("Lihat semua proyek →", "/proyek/")], cls_="container sec-head"),
    gallery,
    group([p("Klien kami", "clients-head"),
           group([img(i, f, a, "client") for i, f, a in CLIENTS], cls_="clients")], cls_="container"),
], "proj")

# ---------- 3. Untuk siapa ----------
def sol_card(id_, path, alt, tag, title, href, desc):
    return group([
        img(id_, path, alt, "photo"),
        group([p(tag, "sol-tag"), h(f'<a href="{href}">{title}</a>', 3), p(desc), p("Selengkapnya", "go")], cls_="sol-body"),
    ], cls_="sol-card")

solusi = section("solusi", [group([
    sec_head("Untuk siapa", "Rumah, bisnis, dan pabrik.", ("Semua layanan →", "/layanan/")),
    group([
        sol_card(3180, "2022/09/DJI_0034-scaled.jpg", "Foto udara PLTS atap rumah tinggal hasil pemasangan Renus",
                 "Residensial", "PLTS untuk rumah", "/plts-hybrid/",
                 "On-grid, off-grid, atau hybrid untuk rumah tinggal dengan sambungan 1 phase maupun 3 phase."),
        sol_card(3289, "2023/03/DJI_0441-2-scaled.jpg", "Foto udara PLTS atap gedung komersial hasil pemasangan Renus",
                 "Komersial", "PLTS untuk bisnis", "/pasang-plts-untuk-bisnis/",
                 "Kantor, ruko, hotel, sekolah, dan instansi yang ingin menekan biaya listrik operasional."),
        sol_card(4810, "2024/10/DJI_0017-scaled.jpg", "Foto udara PLTS atap pabrik hasil pemasangan Renus",
                 "Industrial", "PLTS industri &amp; manufaktur", "/plts-industri-manufaktur/",
                 "Sistem skala besar di atap pabrik, gudang, dan kawasan industri."),
    ], cls_="sol"),
], cls_="container")], "soft")

# ---------- 4. Sistem PLTS ----------
ROWS = [
    ("Sambungan PLN", "Perlu", "Tidak perlu", "Perlu"),
    ("Baterai", "Tidak ada", "Ada", "Ada"),
    ("Malam hari", "Listrik PLN", "Baterai", "Baterai, lalu PLN"),
    ("Saat PLN padam", "Ikut berhenti", "Tidak terpengaruh", "Tetap menyala"),
    ("Biaya awal", "Paling rendah", "Lebih tinggi (baterai)", "Lebih tinggi (baterai + inverter hybrid)"),
]
thead = "<thead><tr><th></th><th>On-grid</th><th>Off-grid</th><th>Hybrid</th></tr></thead>"
tbody = "<tbody>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in ROWS) + "</tbody>"
table = (f"<!-- wp:table {{\"hasFixedLayout\":false,\"className\":\"compare-wrap\"}} -->\n"
         f"<figure class=\"wp-block-table compare-wrap\"><table>{thead}{tbody}</table></figure>\n<!-- /wp:table -->")
sistem = section("sistem", [group([
    sec_head("Sistem PLTS", "Pilih sistem sesuai kebutuhan listrik Anda.", ("Panduan memilih sistem →", "/sistem-plts-terbaik-2026/")),
    html(wp_assets(between(r'<div class="systems">', r"^    </div>$"))),
    group([
        h("Perbandingan ketiga sistem", 3, "compare-title"),
        table,
        p("Sejak Permen ESDM No. 2/2024, kelebihan listrik yang mengalir ke PLN tidak lagi mengurangi tagihan. "
          "Karena itu kapasitas on-grid kami sesuaikan dengan pemakaian siang hari, dan hybrid kami rekomendasikan "
          "agar kelebihan energi tersimpan di baterai.", "fineprint"),
    ], cls_="compare-block"),
], cls_="container")])

# ---------- 5. Kenapa Renus ----------
def stat(num, unit, label):
    return group([p(f"{num}<sub>{unit}</sub>", "num"), p(label, "lbl")])

kenapa = section("kenapa-renus", [group([
    group([
        group([p("Kenapa Renus", "eyebrow"), h("Kontraktor PLTS bersertifikat dengan rekam jejak yang bisa dicek.", 2, "h2")]),
        group([buttons(button("Jadwalkan survei gratis", f"{WA}?text=Halo%20Renus%2C%20saya%20ingin%20survei%20atap%20gratis.", "rn-btn-primary", True)),
               more("Lihat paket &amp; harga", "#paket")], cls_="band-cta"),
    ], cls_="band-head"),
    group([
        stat("500", "+", "proyek terpasang"),
        stat("10", " MWp+", "kapasitas terpasang"),
        stat("40.000", " kWh+", "estimasi energi bersih per hari"),
        stat("6", "+ tahun", "pengalaman di energi surya"),
    ], cls_="big-stats"),
    group([
        group([p("Sertifikasi ISO", "cred-label"),
               ul(["<strong>9001:2015</strong>Mutu", "<strong>14001:2015</strong>Lingkungan",
                   "<strong>45001:2018</strong>K3", "<strong>37001:2025</strong>Anti-penyuapan"], "iso")], cls_="cred-group"),
        ul(["<strong>Badan usaha ketenagalistrikan</strong>Terdaftar di DJK Kementerian ESDM, dengan tenaga ahli bersertifikat ESDM.",
            "<strong>Pemerintah, BUMN, swasta, hingga rumah tinggal</strong>Klien kami antara lain Kementerian PUPR, WIKA, Medco Energi, dan Pertamina.",
            "<strong>Melayani seluruh Indonesia</strong>Kantor di Surabaya dan Jabodetabek, survei atap gratis sebelum penawaran."], "cred-list"),
    ], cls_="creds"),
], cls_="container")], "band")

# ---------- 6. Paket ----------
paket_html = between(r'<div class="tabs" role="tablist"', r'<div class="tab-panel" role="tabpanel" id="pan-ongrid"')
paket_html += "\n" + between(r'<div class="price-group ongrid">', r'^    </div>$')
paket = section("paket", [group([
    group([group([p("Paket &amp; harga", "eyebrow"), h("Harga paket yang jelas sejak awal.", 2, "h2")])], cls_="sec-head"),
    html(paket_html),
    p("Harga material sesuai katalog Agustus 2026, belum termasuk pemasangan. Biaya akhir ditentukan setelah survei lokasi gratis. "
      "*Estimasi penghematan maksimum; angka aktual bergantung pada pola pemakaian, orientasi atap, dan cuaca.", "fineprint"),
], cls_="container")])

# ---------- 7. Kalkulator ----------
cs = next(i for i, l in enumerate(lines) if l == '<div class="rn-calc">')
ce = lines.index("</script>", cs) + 1  # </div> penutup kalkulator tepat setelah skripnya
assert lines[ce] == "</div>"
calc = "\n".join(lines[cs : ce + 1])
kalkulator = section("kalkulator", [group([
    group([group([p("Kalkulator PLTS", "eyebrow"), h("Berapa kapasitas yang Anda butuhkan?", 2, "h2")])], cls_="sec-head"),
    p("Empat langkah singkat untuk estimasi kapasitas dan penghematan. Hasilnya bisa langsung dikirim ke tim kami lewat WhatsApp.", "lede"),
    html('<div class="calc-wrap">\n' + calc + "\n</div>"),
], cls_="container")], "soft")

# ---------- 8. Proses ----------
proses = section("proses", [group([
    img(4809, "2024/10/IMG-20240902-WA0040-1-scaled.jpg", "Tim Renus memasang PLTS di atap industri", "photo proc-photo",
        "Tim Renus di lokasi pemasangan"),
    group([
        p("Proses kerja", "eyebrow"),
        h("Dari survei sampai purna jual, satu tim.", 2, "h2"),
        ul(["<strong>Survei gratis</strong>Tim kami mengecek atap, instalasi listrik, dan pola pemakaian Anda.",
            "<strong>Desain sistem</strong>Kapasitas panel, inverter, dan baterai dihitung sesuai kebutuhan.",
            "<strong>Instalasi</strong>Dipasang oleh teknisi Renus, lalu sistem diuji sebelum diserahkan.",
            "<strong>Purna jual</strong>Pemantauan dan perawatan setelah sistem berjalan."], "steps", ordered=True),
    ]),
], cls_="container proc")])

# ---------- 9. FAQ ----------
FAQ = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>", proto)
assert len(FAQ) == 6
faq = section("faq", [group([
    group([
        p("Pertanyaan umum", "eyebrow"),
        h("Yang sering ditanyakan.", 2, "h2"),
        p("Belum terjawab? Tanyakan langsung ke tim kami.", "lede"),
        buttons(button("Tanya via WhatsApp", WA, "rn-btn-outline", True)),
    ]),
    group([details(q, a) for q, a in FAQ], cls_="faq"),
], cls_="container faq-grid")], "soft")

# ---------- 10. Kontak ----------
kontak = section("kontak", [group([
    group([
        p("Hubungi kami", "eyebrow"),
        h("Konsultasi dan survei atap gratis.", 2, "h2"),
        p("Ceritakan kebutuhan listrik Anda. Tim kami menghubungi Anda dalam 1×24 jam.", "lede"),
        p('Email: <a href="mailto:sales@renergynusantara.com">sales@renergynusantara.com</a>', "contact-mail"),
    ]),
    html(between(r'<div class="contact-side">', r"^    </div>$")),
], cls_="container contact")], "deep")

# ---------- 11. Artikel (dinamis: 3 artikel terbaru) ----------
latest = ('<!-- wp:latest-posts {"postsToShow":3,"displayPostContent":true,"excerptLength":24,'
          '"displayPostDate":true,"displayFeaturedImage":true,"featuredImageSizeSlug":"medium_large",'
          '"addLinkToFeaturedImage":true,"className":"posts"} /-->')
artikel = section("artikel", [group([
    sec_head("Artikel", "Panduan memilih dan memasang PLTS.", ("Semua artikel →", "/artikel/")),
    latest,
], cls_="container")])

# ---------- WA mengambang + skrip ----------
wa_float = next(l for l in lines if 'class="btn btn-primary wa-float hidden"' in l)
s = max(i for i, l in enumerate(lines) if l == "<script>")  # skrip halaman (bukan skrip kalkulator)
script = "\n".join(lines[s : lines.index("</script>", s) + 1])
# menu HP milik header prototipe; di WordPress diganti header Kadence
script = re.sub(r"\n  const menuBtn = .*?\n.*?\n", "\n", script)
assert "menuBtn" not in script
tail = html(wa_float + "\n" + script)

blocks = group([hero, proyek, solusi, sistem, kenapa, paket, kalkulator, proses, faq, kontak, artikel, tail],
               cls_="rn rn-home", align="full")
(OUT / "homepage.blocks.html").write_text(blocks + "\n", encoding="utf-8")

# ---------- CSS ----------
css_src = between(r"^<style>$", r"^</style>$")
css_src = css_src.split("\n", 1)[1].rsplit("\n", 1)[0]
css_src = re.sub(r"/\*.*?\*/", "", css_src, flags=re.S)

DROP = (".skip", ".site-header", ".logo", ".nav", ".header-cta", ".menu-btn", ".why", ".stats", ".stat ",
        ".gallery", ".sd-", ".sys-diagram", ".price-rows", ".legend", ".ph-logo", ".site-footer", ".mode-label",
        ".post", ".compare caption", "html")
RENAME = [  # prototipe -> markup blok inti
    (".compare ", ".compare-wrap table "), (".compare{", ".compare-wrap table{"), (".compare,", ".compare-wrap table,"),
    (".big-stats dd span", ".big-stats .num sub"), (".big-stats dd", ".big-stats .num"), (".big-stats dt", ".big-stats .lbl"),
    (".iso b", ".iso strong"), (".cred-list b", ".cred-list strong"),
    (".steps h3", ".steps strong"), (".proj-grid figcaption b", ".proj-grid figcaption strong"),
    (".proj-main figcaption b", ".proj-main figcaption strong"),
    ("@keyframes pulse", "@keyframes rn-pulse"), ("animation:pulse", "animation:rn-pulse"),
    ("@keyframes ring", "@keyframes rn-ring"), ("animation:ring", "animation:rn-ring"),
    ("@keyframes isoflow", "@keyframes rn-isoflow"), ("animation:isoflow", "animation:rn-isoflow"),
]
for a, b in RENAME:
    css_src = css_src.replace(a, b)

SCOPE = "body .rn"


def scope_sel(sel):
    sel = sel.strip()
    if sel == ":root" or sel == "body":
        return SCOPE
    if sel.startswith("*"):
        return f"{SCOPE} {sel}"
    return f"{SCOPE} {sel}"


def parse(css):
    """Pecah CSS datar menjadi (prelude, body) dengan @media bersarang."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0:
            break
        prelude = css[i:j].strip()
        depth, k = 1, j + 1
        while depth:
            depth += {"{": 1, "}": -1}.get(css[k], 0)
            k += 1
        out.append((prelude, css[j + 1 : k - 1]))
        i = k
    return out


def emit(rules):
    res = []
    for prelude, body in rules:
        if prelude.startswith("@media"):
            inner = emit(parse(body))
            if inner:
                res.append(f"{prelude}{{\n{inner}\n}}")
        elif prelude.startswith("@"):
            res.append(f"{prelude}{{{body.strip()}}}")
        else:
            sels = [s.strip() for s in prelude.split(",")]
            sels = [s for s in sels if not s.startswith(DROP)]
            if not sels:
                continue
            res.append(",".join(scope_sel(s) for s in sels) + "{" + body.strip() + "}")
    return "\n".join(res)


css = emit(parse(css_src))


def scope_calc(block):
    """Gaya kalkulator ikut di-scope ke "body .rn" agar menang atas reset & gaya Kadence."""
    m = re.search(r"<style>\n(.*?)</style>", block, re.S)
    return block.replace(m.group(1), emit(parse(re.sub(r"/\*.*?\*/", "", m.group(1), flags=re.S))) + "\n")


blocks = blocks.replace(calc, scope_calc(calc))
(OUT / "homepage.blocks.html").write_text(blocks + "\n", encoding="utf-8")
wp_css = (OUT / "wp-overrides.css").read_text(encoding="utf-8")
full_css = "html{scroll-behavior:smooth}\n" + (OUT / "wp-reset.css").read_text(encoding="utf-8") + css + "\n" + wp_css
(OUT / "rn.css").write_text(
    "/* ===== Renus redesign: token + komponen (.rn). Sumber: repo website-renus wordpress/homepage/ ===== */\n"
    + full_css, encoding="utf-8")


def minify(c):
    c = re.sub(r"/\*.*?\*/", "", c, flags=re.S)
    c = re.sub(r"\s*\n\s*", "", c)
    c = re.sub(r";\s+", ";", c)
    c = re.sub(r"\s*([{}])\s*", r"\1", c)
    return c.replace(";}", "}")


# CSS tinggal di Additional CSS Kadence (wordpress/additional-css.css). --inline-css menaruhnya
# di blok HTML pertama sebagai cadangan bila Additional CSS tidak bisa ditulis.
LEGACY_CSS = (OUT / "legacy-additional.css").read_text(encoding="utf-8")
(OUT.parent / "additional-css.css").write_text(
    "/* ===== CSS lama (sebelum redesain) ===== */\n" + LEGACY_CSS
    + "\n/* ===== Renus redesign: token + komponen (.rn). Sumber: repo website-renus wordpress/homepage/ ===== */\n"
    + minify(full_css) + "\n", encoding="utf-8")
if "--inline-css" in sys.argv:
    blocks = blocks.replace("<!-- wp:html -->\n" + FONTS, "<!-- wp:html -->\n" + FONTS + '\n<style id="rn-css">' + minify(full_css) + "</style>", 1)


def slim_html_block(m):
    """Hemat ukuran isi Custom HTML: buang indentasi & komentar HTML (bukan komentar blok)."""
    body = re.sub(r"<!--(?! /?wp:).*?-->", "", m.group(1), flags=re.S)
    body = "\n".join(l.strip() for l in body.splitlines() if l.strip())
    return "<!-- wp:html -->\n" + body + "\n<!-- /wp:html -->"


blocks = re.sub(r"<!-- wp:html -->\n(.*?)\n<!-- /wp:html -->", slim_html_block, blocks, flags=re.S)
(OUT / "homepage.blocks.html").write_text(blocks + "\n", encoding="utf-8")
print("blocks:", len(blocks), "bytes · css:", len(css) + len(wp_css), "bytes")


# --chunks DIR: pecah per section untuk dikirim bertahap (wp_update_page untuk 00, lalu
# wp_insert_blocks at=inside_end path=0 untuk 01..). Satu panggilan MCP penuh terlalu besar.
if "--chunks" in sys.argv:
    d = Path(sys.argv[sys.argv.index("--chunks") + 1]); d.mkdir(parents=True, exist_ok=True)
    ls = blocks.rstrip("\n").split("\n")
    parts, depth, cur = [], 0, []
    for l in ls[2:-2]:
        cur.append(l)
        for m in re.finditer(r"<!-- (/?)wp:[a-z/-]+(?: \{.*?\})?( /)? -->", l):
            if not m.group(2):
                depth += -1 if m.group(1) else 1
        if depth == 0 and re.search(r"<!-- /wp:[a-z-]+ -->$", l):
            parts.append("\n".join(cur)); cur = []
    assert not cur and depth == 0
    (d / "00.html").write_text("\n".join(ls[:2]) + "\n" + parts[0] + "\n" + "\n".join(ls[-2:]), encoding="utf-8")
    for i, part in enumerate(parts[1:], 1):
        (d / f"{i:02d}.html").write_text(part, encoding="utf-8")
    print("chunks:", len(parts))
