#!/usr/bin/env python3
"""Generator halaman dalam (selain homepage) → blok inti Gutenberg.

Memakai komponen .rn yang sama dengan homepage (token & gaya di Additional CSS) plus komponen
halaman di pages.css. Hasil: <slug>.blocks.html untuk dikirim ke WordPress lewat Royal MCP.

    python3 build_pages.py            # semua halaman
    python3 build_pages.py tentang-kami
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).parent
UP = "https://renergynusantara.com/wp-content/uploads/"
WA = "https://wa.me/6281412250644"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap"'
         ' media="print" onload="this.media=\'all\'">')


# ---------- helper blok (sama dengan homepage/build.py) ----------
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


def img(id_, path, alt, cls_=None, size="large"):
    """path = berkas ukuran `size` (mis. ...-1024x576.jpg) agar src tidak memakai file asli yang besar."""
    a = {"id": id_, "sizeSlug": size, "linkDestination": "none", "className": cls_}
    return (f"<!-- wp:image{attrs(a)} -->\n<figure class=\"{cls('wp-block-image size-' + size, cls_)}\">"
            f"<img src=\"{UP}{path}\" alt=\"{alt}\" class=\"wp-image-{id_}\"/></figure>\n<!-- /wp:image -->")


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


def html(raw):
    return f"<!-- wp:html -->\n{raw.strip()}\n<!-- /wp:html -->"


def section(children, cls_=None, anchor=None):
    return group([group(children, cls_="container")], tag="section", cls_=cls_, anchor=anchor)


def page(children):
    """Pembungkus halaman: grup .rn penuh + font (dimuat tanpa memblokir render)."""
    return group([html(FONTS)] + children, cls_="rn rn-page", align="full")


def card(title, text):
    return group([h(title, 3), p(text)], cls_="card")


def point(title, text):
    return f"<strong>{title}</strong>{text}"


# ---------- Tentang Kami (ID 44, /tentang-kami/) ----------
def tentang_kami():
    head = section([
        img(3529, "2023/04/WhatsApp-Image-2023-04-03-at-00.22.45.jpeg",
            "Tim teknisi Renus memasang panel surya di atap", "hero-bg", size="full"),
        group([
            p("Tentang kami", "eyebrow"),
            h("Renus Global Indonesia, penyedia PLTS untuk rumah, bisnis, dan industri.", 1, "page-title"),
            p("Kami bergerak di bidang energi, mekanikal, dan elektrikal, dengan fokus pada pembangkit listrik tenaga "
              "surya: on-grid, off-grid, dan hybrid. Renus terdaftar sebagai badan usaha ketenagalistrikan di DJK "
              "Kementerian ESDM dan memegang empat sertifikasi ISO.", "lede"),
            buttons(button("Konsultasi gratis", WA, "rn-btn-primary", external=True),
                    button("Lihat proyek kami", "/proyek/", "rn-btn-outline")),
        ]),
    ], cls_="page-hero")

    stats = group([group([
        group([p("500+", "num"), p("proyek terpasang", "lbl")]),
        group([p("10 MWp+", "num"), p("kapasitas terpasang", "lbl")]),
        group([p("6+ tahun", "num"), p("pengalaman di energi surya", "lbl")]),
        group([p("4", "num"), p("sertifikasi ISO", "lbl")]),
    ], cls_="big-stats")], cls_="container")
    band = group([stats], tag="section", cls_="band band-stats")

    visi = section([
        img(4423, "2024/01/20220530_132107-scaled-e1705389799940-1024x683.jpg",
            "Panel surya terpasang di atap bangunan klien Renus", "photo split-photo"),
        group([
            p("Visi dan misi", "eyebrow"),
            h("Kepuasan pelanggan jadi ukuran kerja kami.", 2, "h2"),
            ul([
                point("Visi", "Menjadi perusahaan terpadu yang memberi solusi di bidang teknologi dan energi terbarukan."),
                point("Misi", "Menyediakan produk dan layanan berkualitas yang memberi nilai tambah, bekerja profesional "
                              "di setiap proyek, dan menjaga kepuasan pelanggan dari survei sampai purna jual."),
            ], "points"),
        ]),
    ], cls_="split")

    kenapa = section([
        group([
            p("Mengapa Renus", "eyebrow"),
            h("Lebih dari 6 tahun mengerjakan PLTS.", 2, "h2"),
            group([
                card("Tim ahli bersertifikat", "Perhitungan sistem mempertimbangkan sisi teknis dan biaya, jadi "
                     "kapasitas yang dipasang sesuai kebutuhan listrik dan anggaran Anda."),
                card("Komponen merek premium", "Panel, inverter, dan baterai berkualitas dengan perkiraan umur pakai "
                     "hingga 15 tahun."),
                card("Konsultasi gratis", "Tanyakan pengadaan komponen tenaga surya atau jasa instalasinya saja, "
                     "tanpa biaya konsultasi."),
                card("Bersertifikat ISO", "Empat standar ISO untuk mutu, lingkungan, K3, dan anti-penyuapan "
                     "diterapkan di setiap proyek."),
            ], cls_="cards"),
        ]),
        img(3682, "2023/06/IMG_20230508_172438-576x1024.jpg",
            "Teknisi Renus memeriksa instalasi panel surya", "photo split-photo tall"),
    ], cls_="soft split")

    legal = section([
        group([group([p("Legalitas & sertifikasi", "eyebrow"),
                      h("Terdaftar, bersertifikat, dan bisa dicek.", 2, "h2")])], cls_="sec-head"),
        group([
            group([
                img(4222, "2024/01/Untitled-2-01-1-1024x714.png",
                    "Sertifikat ISO PT Renus Global Indonesia", "cert"),
                h("Sertifikasi ISO", 3),
                ul(["<strong>ISO 9001:2015</strong> Sistem manajemen mutu",
                    "<strong>ISO 14001:2015</strong> Sistem manajemen lingkungan",
                    "<strong>ISO 45001:2018</strong> Sistem manajemen K3",
                    "<strong>ISO 37001:2025</strong> Sistem manajemen anti-penyuapan"], "checks"),
            ], cls_="doc"),
            group([
                img(4220, "2024/01/SBU-RENUS-01-1-768x543.png",
                    "Sertifikat Badan Usaha ketenagalistrikan PT Renus Global Indonesia", "cert", size="medium_large"),
                h("Badan usaha ketenagalistrikan", 3),
                p("Renus memegang Sertifikat Badan Usaha untuk pembangunan dan pemasangan instalasi penyediaan "
                  "tenaga listrik, terdaftar di Kementerian ESDM."),
            ], cls_="doc"),
            group([
                img(4224, "2024/01/Untitled-3-01-10-1-1024x715.png",
                    "Sertifikat kompetensi tenaga ahli PLTS Renus", "cert"),
                h("Tenaga ahli bersertifikat", 3),
                ul(["Supervisor Senior Pembangunan dan Pemasangan Unit PLTS (Level 5)",
                    "Pelaksana Senior Pembangunan dan Pemasangan Peralatan PLTS (Level 3)",
                    "Keselamatan dan Kesehatan Kerja (K3) Umum"], "checks"),
            ], cls_="doc"),
        ], cls_="docs"),
    ])

    cta = section([
        group([
            group([p("Profil perusahaan", "eyebrow"),
                   h("Pelajari Renus lebih lengkap.", 2, "h2"),
                   p("Unduh profil perusahaan untuk melihat produk, solusi, dan proyek yang sudah kami kerjakan.", "lede")]),
            buttons(button("Unduh profil (PDF)", UP + "2024/06/Company-Profile-PT.-Renus-Global-Indonesia-_compressed.pdf",
                           "rn-btn-primary", external=True),
                    button("Konsultasi via WhatsApp", WA, "rn-btn-outline", external=True)),
        ], cls_="band-head"),
    ], cls_="band cta-band")

    return page([head, band, visi, kenapa, legal, cta])


PAGES = {"tentang-kami": tentang_kami}

if __name__ == "__main__":
    for slug in (sys.argv[1:] or PAGES):
        out = OUT.parent / slug / f"{slug}.blocks.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(PAGES[slug]() + "\n", encoding="utf-8")
        print(out.relative_to(OUT.parent), out.stat().st_size, "bytes")
