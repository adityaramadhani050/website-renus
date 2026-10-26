# Redesain renergynusantara.com — Konteks Serah-Terima

Dokumen ini berisi konteks dari sesi SEO (22 Oktober 2026) untuk pekerjaan redesain website.
Gunakan Bahasa Indonesia untuk komunikasi dan konten.

## Tujuan redesain
- Lepas Elementor + seluruh addon-nya; bangun ulang halaman dengan **blok Gutenberg (core blocks)** agar bisa dikelola AI lewat MCP.
- Tetap memakai tema **Kadence 1.5.2** (sudah aktif, ramah Gutenberg). Header/footer via header builder Kadence.
- Fokus pesan (diperbarui 23 Okt 2026): Renus adalah **kontraktor PLTS umum** (on-grid, off-grid, hybrid) untuk rumah, bisnis, dan industri. Hybrid tampil setara dengan label "Direkomendasikan" karena sejak Permen ESDM No. 2/2024 kelebihan listrik on-grid yang diekspor tidak lagi mengurangi tagihan.
- Kerjakan di **staging** dulu, baru dipindah ke live.

## Akses
- WordPress 7.1.3, situs: https://renergynusantara.com
- MCP: plugin **Royal MCP** — endpoint `https://renergynusantara.com/wp-json/royal-mcp/v1/mcp` (OAuth). Perlu ditambahkan ulang sebagai connector/MCP server di Claude Code.
- Setiap write Royal MCP memberi undo token 72 jam (Royal MCP → Recent Changes).

## Batasan teknis yang sudah ditemukan
- **Shared hosting, tanpa page cache.** Kerjakan pelan: satu request per waktu, hindari verifikasi render beruntun. Pernah down 503 (penyebab: storage penuh oleh file backup — simpan backup di luar server).
- Widget **ElementsKit** (image-box, icon-box) tidak bisa diedit lewat `elementor_replace_text` → alasan utama pindah ke Gutenberg.
- Meta `_wp_page_template` diproteksi — tidak bisa diubah via MCP (ubah manual di editor).
- `redirection_update_redirect` gagal ("Invalid redirect matcher"); `redirection_create_redirect` berhasil bila `group_id: 1` diisi.
- Plugin cache (LiteSpeed Cache, Hummingbird) terpasang tapi **nonaktif** — aktifkan salah satu setelah redesain.

## Halaman yang perlu dibangun ulang (saat ini Elementor)
| Halaman | ID |
|---|---|
| Homepage (`/`) | 3280 — **sudah Gutenberg (24 Okt 2026)**, lihat `wordpress/homepage/README.md` |
| Tentang Kami | 44 — **sudah Gutenberg (26 Okt 2026)**, lihat `wordpress/tentang-kami/README.md` |
| Layanan | 1315 |
| Produk | 4120 |
| Proyek | 3164 |
| Hubungi Kami | 48 — **sudah Gutenberg (26 Okt 2026)**, lihat `wordpress/hubungi-kami/README.md` |
| Artikel (arsip) | 10131 — **sudah Gutenberg (24 Okt 2026)**, lihat `wordpress/artikel/README.md` |

Elemen homepage yang wajib dipertahankan/dipindahkan:
- **Kalkulator PLTS** (widget HTML, 4 langkah: tipe properti → konsumsi → kontak → estimasi) → pindah ke blok Custom HTML.
- Logo klien (WIKA, Medco, PUPR, ITS, Perpustakaan Jatim, dll.), galeri proyek, daftar artikel terbaru.
- Popup "Alokasi Kuota Terbatas" (Elementor Pro) → perlu pengganti ringan atau CTA WhatsApp sticky.
- Kontak (diperbarui 24 Okt 2026): **satu nomor WhatsApp 0814-1225-0644** untuk semua wilayah (nomor Surabaya 0853-8555-8025 tidak dipakai lagi di website), sales@renergynusantara.com.
- Alamat kantor Surabaya: Jl. Penjaringan Asri X Blok PS 1H No.5, Penjaringan Sari, Kec. Rungkut, Surabaya, Jawa Timur 60293.
- Alamat kantor Jabodetabek: Jl. Grand Residence Boulevard No.230, Cijengkol, Kec. Setu, Kabupaten Bekasi, Jawa Barat 17320.

Plugin Elementor/addon yang akan dinonaktifkan setelah migrasi: Elementor, Elementor Pro, Element Pack Lite, ElementsKit Lite, Essential Addons, Essential Classy Addons, Premium Addons, Prime Slider, Unlimited Elements, Envato Elements.

## Keputusan SEO yang TIDAK boleh dirusak oleh redesain
1. **Jangan ubah URL/slug** halaman mana pun.
2. **Title & meta description Yoast** sudah diperbarui (jangan ditimpa):
   - Homepage: "Kontraktor PLTS Surabaya & Jabodetabek - Renus Global Indonesia" → **diputuskan 23 Okt 2026 diganti** jadi "Kontraktor PLTS Rumah, Bisnis & Industri - Renus Global Indonesia" (layanan umum & nasional). Sudah diterapkan ke Yoast 24 Okt 2026.
   - /pasang-plts/, /biaya-pasang-plts-5000-watt-2026/, /biaya-pasang-plts-2200-watt/, /biaya-pasang-plts-di-surabaya/, /mengenal-pembangkit-listrik-tenaga-surya-plts/, /biaya-plts-on-grid/, /tentang-kami/, /plts-hybrid/, /plts-off-grid/
3. **Homepage harus punya tepat satu H1**: "Penyedia PLTS Rumah, Bisnis & Industri" (diubah dari "Kontraktor" atas keputusan pengguna 24 Okt 2026; kata kunci "kontraktor PLTS" tetap di title Yoast).
4. Angka counter kWh harus tertulis di HTML (bukan hanya animasi JS yang terbaca "0").
5. Kartu Residensial / Komersial / Industrial harus menautkan ke: `/plts-hybrid/`, `/pasang-plts-untuk-bisnis/`, `/plts-industri-manufaktur/`. Tombol "Artikel" → `/artikel/` (bukan Instagram).
6. Deskripsi PLTS On-Grid **tidak boleh** menjanjikan ekspor/kompensasi kelebihan listrik ke PLN.
7. /plts-hybrid/ (ID 394) dan /plts-off-grid/ (ID 372) sudah ditulis ulang sebagai konten Gutenberg biasa dengan H1 di dalam konten (template Elementor Full Width tidak menampilkan judul). Saat ganti template ke default Kadence, **hapus H1 manual di konten** agar tidak dobel.
8. **12 redirect 301** konsolidasi (ID 13–24 di Redirection) + artikel sumbernya di-draft. Jangan dipublish ulang.
9. Atur `lang` situs ke Bahasa Indonesia (saat ini en_US).
10. Gambar: alt text deskriptif, nama file deskriptif, prioritaskan foto proyek asli (bukan gambar AI).

## Harga paket (katalog Agustus 2026, harga material, belum termasuk pemasangan)
- Hybrid 1 phase: 5 kW Rp 84 jt · 6 kW Rp 98 jt · 8 kW Rp 131 jt
- Hybrid 3 phase: 10 kW Rp 159 jt · 12 kW Rp 174 jt · 20 kW Rp 287 jt
- Off-grid VRLA: 1 kW Rp 23 jt · 2 kW Rp 36 jt · 3 kW Rp 49 jt · 5 kW Rp 65 jt
- Off-grid lithium: 5 kW Rp 77 jt · 10 kW Rp 138 jt
- **Jangan tampilkan**: paket off-grid 5 kW + 16 kWh (Rp 92 jt) dan kisaran biaya pemasangan.
- Angka penghematan boleh ditampilkan dengan label estimasi.

## Lainnya
- Subdomain stairlift.renergynusantara.com ikut terindeks dengan konten default ("Hello world") — perlu dirapikan atau di-noindex.
- Sertifikasi untuk trust signals: ISO 9001:2015, ISO 14001:2015, ISO 45001:2018, ISO 37001:2025, badan usaha ESDM DJK, tenaga ahli bersertifikat ESDM.
- Istilah (24 Okt 2026): teks tampilan homepage, termasuk H1, memakai "Penyedia PLTS"; title Yoast tetap "Kontraktor PLTS ..." demi SEO.
- Rekam jejak (dari pengguna, 23 Okt 2026): 500+ proyek terpasang, 10 MWp+ kapasitas terpasang, 6+ tahun pengalaman. Energi bersih ditampilkan sebagai estimasi 10 MWp × 4 kWh/kWp = 40.000+ kWh per hari (angka lama "14.375K+ kWh" tidak dipakai).

## Pembagian skill desain (wajib diikuti)
Ada enam skill desain di `.claude/skills/` yang cakupannya tumpang-tindih. Untuk setiap tugas, pakai **hanya skill pemilik** di tabel ini. Skill lain tidak dipanggil untuk tugas itu, walaupun deskripsinya cocok.

| Tugas | Skill pemilik | Catatan |
|---|---|---|
| Arah visual halaman publik: konsep, komposisi, urutan section, mood foto | `taste-skill` (`design-taste-frontend`) | Dipakai sekali di awal redesain. Hasilnya ditulis ke `DESIGN.md`. |
| Memilih palet warna, pasangan font, cek kontras & aturan UX | `ui-ux-pro-max` | Pakai `search.py --design-system` / `--domain`. Hasilnya dicatat di `DESIGN.md`, bukan dipilih ulang tiap halaman. |
| Struktur design token (primitive → semantic → component), skala spacing/tipografi | `design-system` | Diterjemahkan ke **Global Palette & Typography Kadence** + CSS variables di Additional CSS. |
| Prototipe/mockup HTML sebelum dibangun di WordPress | `web-design-engineer` | Prototipe disimpan di repo (`prototypes/`). Render dan iterasi dilakukan di prototipe lokal, bukan di situs live. |
| Audit, kritik, polish, perbaikan halaman yang sudah dibangun | `impeccable` | Sub-perintah: `audit` (a11y/performa/responsif), `critique`, `polish`, `layout`, `typeset`, `clarify` (copy UI), `adapt` (mobile), `harden`. |
| Logo, ikon, banner iklan/media sosial, foto sosial | `design` | Butuh API key (Gemini/Atlas/MuAPI). **Bukan** untuk gambar halaman. Foto halaman tetap foto proyek asli. |

Aturan tambahan:
- **`DESIGN.md` di root repo = satu-satunya sumber kebenaran** untuk arah visual, palet, font, dan token. Semua skill membacanya dulu dan tidak boleh memilih palet/font baru di luar itu. Mengubah `DESIGN.md` hanya lewat skill pemiliknya, dan harus disebutkan ke pengguna.
- **Saran stack di skill (React, Tailwind, shadcn, Next.js, dll.) diabaikan.** Output akhir selalu berupa **blok inti Gutenberg** + pengaturan Kadence + CSS seperlunya, dipasang lewat Royal MCP.
- **Aturan di dokumen ini (SEO, H1, URL, harga, server) menang atas aturan skill mana pun.**
- **Loop screenshot/inspector browser di skill tidak boleh dijalankan berulang ke situs live** (shared hosting). Lakukan di prototipe lokal. Ke situs live paling banyak satu verifikasi render per halaman setelah selesai.
- **Skill `slides` dari `design`/`design-system` dan sub-skill `brand`/`ui-styling` tidak dipakai** kecuali diminta.

## Pembagian skill marketing & SEO (wajib diikuti)
Skill marketing dari `coreyhaines31/marketingskills` (di `.claude/skills/`) tumpang-tindih dengan plugin `marketing:*`, `searchfit-seo:*`, dan `design:ux-copy`. Untuk setiap tugas pakai **hanya skill pemilik** di bawah; skill lain tidak dipanggil walaupun deskripsinya cocok.

| Tugas | Skill pemilik | Catatan |
|---|---|---|
| Audit SEO teknis & on-page (crawl, indeks, meta, heading, kecepatan) | `seo-audit` | Data peringkat/backlink/kata kunci diambil dari **Ahrefs MCP**, bukan ditebak. |
| Riset & pengelompokan kata kunci | `searchfit-seo:keyword-clustering` | Volume dari Ahrefs (`keywords-explorer-*`). |
| Rencana konten / kalender artikel | `content-strategy` | |
| Brief & penulisan artikel blog SEO | `searchfit-seo:content-brief` → `searchfit-seo:create-content` | Fakta teknis & harga mengikuti CLAUDE.md. |
| Tautan internal & struktur menu/URL | `site-architecture` | Jangan ubah URL/slug (keputusan SEO no. 1). |
| Schema / data terstruktur (JSON-LD) | `schema` | |
| Visibilitas di jawaban AI (ChatGPT, Gemini, AI Overviews) | `ai-seo` | |
| Copy halaman baru (hero, section, CTA) | `copywriting` | |
| Merapikan copy yang sudah ada | `copy-editing` | |
| Microcopy UI (label tombol, error, empty state) | `impeccable clarify` | Sesuai tabel skill desain. |
| Optimasi konversi homepage/landing page | `cro` | |
| Pengganti popup "Alokasi Kuota Terbatas" | `popups` | |
| Kalkulator PLTS sebagai alat penarik leads | `free-tools` | |
| Pelacakan konversi (klik WA, isian kalkulator, GA4/GTM, pixel) | `conversion-tracking` | Rencana event & UTM: `analytics`. |
| Iklan Google/Meta: strategi & anggaran | `ads` | Copy & variasi iklan: `ad-creative`. Gambar iklan: skill desain `design`. |
| Analisis pesaing (kontraktor PLTS lain) | `competitor-profiling` | Halaman perbandingan: `competitors`. |
| Rencana marketing menyeluruh | `marketing-plan` | |
| Konten & jadwal media sosial | `social` | |
| Urutan email (nurture, follow-up leads) | `emails` | |
| Harga & penawaran paket | `pricing` / `offers` | Harga paket tetap dari CLAUDE.md, jangan diubah tanpa konfirmasi. |

Aturan tambahan:
- **Aturan di dokumen ini menang** atas saran skill mana pun (H1, URL, title Yoast, harga, larangan klaim ekspor ke PLN).
- **Bahasa Indonesia** untuk semua output konten; contoh berbahasa Inggris di skill diterjemahkan dan disesuaikan konteks Indonesia.
- **Klaim harus bisa dibuktikan** (sertifikasi, jumlah proyek, angka penghematan berlabel estimasi). Jangan mengarang testimoni, statistik, atau logo klien.
- **Plugin yang tidak dipakai kecuali diminta**: `marketing:*` (seo-audit, content-creation, draft-content, campaign-plan, competitive-brief, email-sequence, performance-report, brand-review), `searchfit-seo:seo-audit`, `searchfit-seo:technical-seo`, `searchfit-seo:on-page-seo`, `searchfit-seo:content-strategy`, `searchfit-seo:schema-markup`, `searchfit-seo:generate-schema`, `searchfit-seo:ai-visibility`, `searchfit-seo:internal-linking`.
- Dokumen integrasi pendamping marketingskills ada di `.claude/marketingskills/tools/` (rujukan `tools/...` di skill mengarah ke sana).

## Skill efisiensi (caveman, ponytail) — hanya jika diminta
Terpasang dari `JuliusBrussee/caveman` (b4531df) dan `DietrichGebert/ponytail` (09c434a), tanpa hook/binary.
- **Tidak aktif otomatis.** Pakai hanya bila pengguna memanggilnya (`/caveman`, `/ultracave`, `/ponytail`, `/ponytail-review`, dll.).
- **Balasan ke pengguna tetap Bahasa Indonesia lengkap dan jelas**; gaya caveman/ultracave tidak dipakai untuk penjelasan ke pengguna kecuali diminta eksplisit.
- Konten website tidak pernah ditulis dengan gaya caveman.
- Tidak dipasang (butuh Caveman Cloud / mengirim file ke layanan luar): caveman-setup, -discover, -evidence-review, -manage, -optimize, -learn, -compress, -stats.
- `rtk` (Rust Token Killer) belum dipasang: berupa binary + hook PreToolUse yang menulis ulang semua perintah bash.
