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


# ---------- Hubungi Kami (ID 48, /hubungi-kami/) ----------
# Form tanpa plugin: isian disusun jadi pesan lalu membuka WhatsApp (data tidak disimpan di server).
WA_FORM = """
<form class="wa-form" id="wa-form" novalidate>
<p class="wa-form-title">Kirim pertanyaan lewat WhatsApp</p>
<div class="wa-row">
<label>Nama lengkap *<input name="nama" autocomplete="name" required></label>
<label>Kota / lokasi pemasangan *<input name="kota" autocomplete="address-level2" required></label>
</div>
<div class="wa-row">
<label>Tipe properti<select name="tipe"><option value="">Pilih</option><option>Rumah tinggal</option><option>Bisnis / komersial</option><option>Industri / pabrik</option></select></label>
<label>Sistem yang diminati<select name="sistem"><option value="">Pilih</option><option>Hybrid</option><option>On-grid</option><option>Off-grid</option><option>Belum tahu, minta saran</option></select></label>
</div>
<label>Pesan<textarea name="pesan" rows="4" placeholder="Contoh: tagihan listrik sekitar Rp 2 juta/bulan, daya 5.500 VA."></textarea></label>
<p class="wa-err" id="wa-err" role="alert" hidden>Isi nama dan kota terlebih dahulu.</p>
<button type="submit">Kirim via WhatsApp</button>
<p class="wa-note">Tombol ini membuka WhatsApp dengan pesan yang sudah terisi. Data tidak disimpan di situs.</p>
</form>
<script>
document.getElementById('wa-form').addEventListener('submit',function(e){
e.preventDefault();var f=e.target,v=function(n){return f.elements[n].value.trim()};
if(!v('nama')||!v('kota')){document.getElementById('wa-err').hidden=false;(v('nama')?f.elements.kota:f.elements.nama).focus();return}
var t='Halo Renus, saya '+v('nama')+' dari '+v('kota')+'.';
if(v('tipe'))t+='\\nTipe properti: '+v('tipe');if(v('sistem'))t+='\\nSistem: '+v('sistem');if(v('pesan'))t+='\\n\\n'+v('pesan');
window.open('https://wa.me/6281412250644?text='+encodeURIComponent(t),'_blank','noopener');
});
</script>
"""


def office(title, addr, maps_q, region):
    q = maps_q.replace(" ", "+")
    return group([
        html(f'<iframe class="map" title="Peta kantor Renus {title}" src="https://maps.google.com/maps?q={q}&output=embed" '
             f'loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'),
        group([
            h(f"Kantor {title}", 3),
            p(addr, "addr"),
            p(region, "region"),
            p(f'<a href="https://www.google.com/maps/search/?api=1&query={q}" target="_blank" rel="noreferrer noopener">'
              f"Buka di Google Maps →</a>", "more"),
        ], cls_="office-body"),
    ], cls_="office-card")


def hubungi_kami():
    head = section([
        img(4747, "2024/09/WhatsApp-Image-2024-09-02-at-09.35.08-3-scaled.jpeg",
            "Panel surya terpasang di atap rumah pelanggan Renus di Surabaya", "hero-bg", size="full"),
        group([
            p("Hubungi kami", "eyebrow"),
            h("Konsultasi PLTS gratis, langsung dengan tim kami.", 1, "page-title"),
            p("Ceritakan kebutuhan listrik rumah atau bisnis Anda. Tim Renus membalas dalam 1×24 jam "
              "dan bisa menjadwalkan survei atap tanpa biaya.", "lede"),
            buttons(button("Chat WhatsApp", WA, "rn-btn-primary", external=True),
                    button("Kirim email", "mailto:sales@renergynusantara.com", "rn-btn-outline")),
        ]),
    ], cls_="page-hero")

    kontak = section([
        group([
            p("Kontak langsung", "eyebrow"),
            h("Satu nomor untuk seluruh Indonesia.", 2, "h2"),
            p("Surabaya, Jabodetabek, maupun kota lain dilayani dari nomor yang sama, jadi pertanyaan Anda "
              "langsung sampai ke tim yang menangani wilayah Anda.", "lede"),
            ul([
                f'<strong>WhatsApp</strong><a href="{WA}" target="_blank" rel="noreferrer noopener">0814-1225-0644</a>',
                '<strong>Email</strong><a href="mailto:sales@renergynusantara.com">sales@renergynusantara.com</a>',
                "<strong>Survei atap</strong>Gratis, dijadwalkan setelah konsultasi.",
            ], "channels"),
        ]),
        html(WA_FORM),
    ], cls_="soft split contact-split")

    kantor = section([
        group([group([p("Kantor", "eyebrow"), h("Kunjungi kantor kami.", 2, "h2")])], cls_="sec-head"),
        group([
            office("Surabaya", "Jl. Penjaringan Asri X Blok PS 1H No.5, Penjaringan Sari, Kec. Rungkut, "
                   "Surabaya, Jawa Timur 60293", "PT Renus Global Indonesia Penjaringan Asri Rungkut Surabaya",
                   "Melayani Jawa Timur, Bali, Nusa Tenggara, dan sekitarnya."),
            office("Jabodetabek", "Jl. Grand Residence Boulevard No.230, Cijengkol, Kec. Setu, Kabupaten Bekasi, "
                   "Jawa Barat 17320", "Grand Residence Boulevard No.230 Cijengkol Setu Bekasi",
                   "Melayani Jabodetabek, Jawa Barat, dan sekitarnya."),
        ], cls_="offices-grid"),
    ])

    sosial = section([
        group([
            group([p("Media sosial", "eyebrow"),
                   h("Lihat proyek terbaru kami.", 2, "h2"),
                   p("Dokumentasi pemasangan, tips hemat listrik, dan kabar terbaru dari tim Renus.", "lede")]),
            buttons(button("Instagram", "https://www.instagram.com/renergynusantara", "rn-btn-outline", external=True),
                    button("Facebook", "https://www.facebook.com/renergynusantara", "rn-btn-outline", external=True),
                    button("LinkedIn", "https://www.linkedin.com/company/renus-global-indonesia", "rn-btn-outline", external=True),
                    button("YouTube", "https://www.youtube.com/@renergynusantara", "rn-btn-outline", external=True)),
        ], cls_="band-head"),
    ], cls_="band cta-band")

    return page([head, kontak, kantor, sosial])


# ---------- Layanan (ID 1315, /layanan/) ----------
def wa_text(topic):
    return WA + "?text=" + ("Halo Renus, saya ingin konsultasi tentang " + topic).replace(" ", "%20")


def sol_card(id_, path, alt, tag, title, href, text):
    """Kartu foto "untuk siapa" (gaya .sol-card homepage)."""
    return group([
        img(id_, path, alt, "photo"),
        group([p(tag, "sol-tag"), h(f'<a href="{href}">{title}</a>', 3), p(text), p("Selengkapnya →", "go")], cls_="sol-body"),
    ], cls_="sol-card")


def svc(id_, path, alt, title, text, href, link, badge=None):
    kids = [img(id_, path, alt, "photo svc-img")]
    if badge:
        kids.append(p(badge, "svc-badge"))
    kids += [h(title, 3), p(text), p(f'<a href="{href}">{link}</a>', "more")]
    return group(kids, cls_="svc")


def layanan():
    head = section([
        img(3289, "2023/03/DJI_0441-2-1024x576.jpg", "Foto udara PLTS atap gedung komersial hasil pemasangan Renus",
            "hero-bg"),
        group([
            p("Layanan kami", "eyebrow"),
            h("Layanan PLTS untuk rumah, bisnis, dan industri.", 1, "page-title"),
            p("Dari survei atap, desain sistem, pemasangan, sampai perawatan. Renus mengerjakan PLTS on-grid, "
              "off-grid, dan hybrid dengan tim bersertifikat ESDM.", "lede"),
            buttons(button("Konsultasi gratis", wa_text("layanan PLTS"), "rn-btn-primary", external=True),
                    button("Lihat paket & harga", "/#paket", "rn-btn-outline")),
        ]),
    ], cls_="page-hero")

    siapa = section([
        group([group([p("Untuk siapa", "eyebrow"), h("Pilih sesuai jenis bangunan Anda.", 2, "h2")])], cls_="sec-head"),
        group([
            sol_card(3180, "2022/09/DJI_0034-1024x576.jpg", "Foto udara PLTS atap rumah tinggal hasil pemasangan Renus",
                     "Residensial", "PLTS untuk Rumah", "/plts-hybrid/",
                     "Tekan tagihan listrik rumah dan tetap menyala saat PLN padam dengan sistem hybrid."),
            sol_card(3289, "2023/03/DJI_0441-2-1024x576.jpg", "Foto udara PLTS atap gedung komersial hasil pemasangan Renus",
                     "Komersial", "PLTS untuk Bisnis", "/pasang-plts-untuk-bisnis/",
                     "Kantor, ruko, hotel, sekolah, dan instansi yang ingin menekan biaya listrik operasional."),
            sol_card(4810, "2024/10/DJI_0017-1024x576.jpg", "Foto udara PLTS atap pabrik skala industri",
                     "Industrial", "PLTS untuk Industri", "/plts-industri-manufaktur/",
                     "Sistem skala besar untuk atap pabrik dan gudang dengan perhitungan beban siang hari."),
        ], cls_="sol"),
    ], cls_="soft")

    sistem = section([
        group([group([p("Sistem PLTS", "eyebrow"), h("Tiga sistem, satu tim yang sama.", 2, "h2")])], cls_="sec-head"),
        group([
            svc(15449, "2026/10/isometrik-plts-hybrid.webp", "Ilustrasi sistem PLTS hybrid dengan panel, inverter, baterai, dan PLN",
                "PLTS Hybrid", "Terhubung PLN dan dilengkapi baterai. Listrik siang disimpan untuk malam hari, "
                "dan rumah tetap menyala saat PLN padam.", "/plts-hybrid/", "Pelajari PLTS hybrid →", "Direkomendasikan"),
            svc(15447, "2026/10/isometrik-plts-on-grid.webp", "Ilustrasi sistem PLTS on-grid yang terhubung ke jaringan PLN",
                "PLTS On-Grid", "Terhubung langsung ke PLN tanpa baterai. Paling hemat biaya awal, cocok bila "
                "pemakaian listrik terbesar terjadi di siang hari.", "/biaya-plts-on-grid/", "Biaya PLTS on-grid →"),
            svc(15448, "2026/10/isometrik-plts-off-grid.webp", "Ilustrasi sistem PLTS off-grid mandiri dengan baterai",
                "PLTS Off-Grid", "Berdiri sendiri tanpa PLN. Baterai menyimpan energi untuk malam hari, cocok "
                "untuk lokasi yang belum terjangkau listrik.", "/plts-off-grid/", "Pelajari PLTS off-grid →"),
        ], cls_="svc-grid"),
    ])

    lain = section([
        group([group([p("Solusi lain", "eyebrow"), h("Produk energi surya untuk kebutuhan khusus.", 2, "h2")])], cls_="sec-head"),
        group([
            card("Smart Powerwall", "Baterai rumah yang mengatur penyimpanan energi otomatis dan memberi cadangan saat "
                 "diperlukan. Desainnya ringkas untuk dipasang di dalam rumah."),
            card("Solar Charging Station", "Stasiun pengisian daya gadget bertenaga surya untuk ruang publik, kampus, "
                 "dan taman kota."),
            card("EV Charging Station", "Pengisian kendaraan listrik yang dipasok energi surya, untuk kantor, "
                 "fasilitas umum, maupun rumah."),
        ], cls_="cards c3"),
        p(f'<a href="{wa_text("produk energi surya khusus")}" target="_blank" rel="noreferrer noopener">'
          "Tanyakan produk ini via WhatsApp →</a>", "more"),
    ], cls_="soft")

    manfaat = section([
        img(3324, "2023/03/DJI_0444-3-768x768.jpg", "Foto udara rumah dengan panel surya terpasang di atap",
            "photo split-photo", size="medium_large"),
        group([
            p("Manfaat", "eyebrow"),
            h("Yang Anda dapat dari PLTS di rumah.", 2, "h2"),
            ul(["Tagihan listrik bulanan lebih rendah",
                "Listrik tetap menyala saat PLN padam (sistem hybrid dan off-grid)",
                "Energi bersih yang mengurangi emisi karbon",
                "Nilai properti bertambah",
                "Komponen bergaransi dengan umur pakai panjang"], "checks"),
        ]),
    ], cls_="split")

    cta = section([
        group([
            group([p("Mulai dari konsultasi", "eyebrow"),
                   h("Ceritakan kebutuhan listrik Anda.", 2, "h2"),
                   p("Tim Renus menghitung kapasitas, biaya, dan estimasi penghematan, lalu menjadwalkan survei atap gratis.", "lede")]),
            buttons(button("Chat WhatsApp", wa_text("layanan PLTS"), "rn-btn-primary", external=True),
                    button("Hubungi kami", "/hubungi-kami/", "rn-btn-outline")),
        ], cls_="band-head"),
    ], cls_="band cta-band")

    return page([head, siapa, sistem, lain, manfaat, cta])


PAGES = {"tentang-kami": tentang_kami, "hubungi-kami": hubungi_kami, "layanan": layanan}

if __name__ == "__main__":
    for slug in (sys.argv[1:] or PAGES):
        out = OUT.parent / slug / f"{slug}.blocks.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(PAGES[slug]() + "\n", encoding="utf-8")
        print(out.relative_to(OUT.parent), out.stat().st_size, "bytes")
