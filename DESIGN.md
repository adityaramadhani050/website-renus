# DESIGN.md — Renus (renergynusantara.com)

Satu-satunya sumber kebenaran untuk arah visual, palet, font, dan token. Lihat aturan di `CLAUDE.md` → "Pembagian skill desain".
Status: **disetujui pengguna 23 Okt 2026** (warna brand biru muda, aksen kuning untuk energi surya, struktur 9 section, H1, CTA WA Jabodetabek).

## Arah visual
- Acuan: landing page Mersol (hero foto rumah full-bleed, judul sans besar rata kiri, tombol kapsul, baris bukti di dasar hero).
- Cerita utama: **PLTS hybrid + baterai** — listrik tetap menyala siang, malam, dan saat PLN padam.
- Hero punya 3 kondisi foto (siang / malam / PLN padam). Animasi aliran energi digambar langsung di atas foto (SVG terkunci ke koordinat foto 1920×1072); tidak ada section diagram terpisah.
- Foto hero = render AI (disetujui pengguna). Galeri proyek wajib memakai foto proyek asli.

## Aset
| Aset | Sumber | Versi web |
|---|---|---|
| Logo putih + tagline | `assets/source/logo-renus-tagline-putih.png` | `prototypes/assets/logo-renus-putih.png` (tinggi 96px, tampil 40–48px) |
| Hero siang | `assets/source/hero-plts-hybrid-siang.jpg` | `hero-plts-hybrid-siang-{1024,1920}.webp` |
| Hero malam | `assets/source/hero-plts-hybrid-malam.jpg` | `hero-plts-hybrid-malam-{1024,1920}.webp` |
| Hero mendung | `assets/source/hero-plts-hybrid-mendung.jpg` | `hero-plts-hybrid-mendung-{1024,1920}.webp` |
| Hero PLN padam | `assets/source/hero-plts-hybrid-pln-padam.jpg` | `hero-plts-hybrid-pln-padam-{1024,1920}.webp` |

Komposisi foto: rumah di 45–90% lebar (tengah-kanan), sisi kiri pepohonan → area teks. Di HP: `object-position: 68% center`.

## Token

### Primitive
```css
--blue-500: #039cfc;   /* biru brand (tombol Kadence) */
--blue-700: #0277c0;   /* tautan di atas putih, 4.77:1 */
--blue-300: #5cc2ff;   /* teks/aksen di atas navy, 6.3:1 */
--navy-900: #00384f;   /* header/footer brand */
--navy-950: #04212e;   /* section paling gelap */
--blue-50:  #e1f0f5;   /* latar section terang (footer brand) */
--ink-900:  #06131c;   /* teks utama */
--ink-600:  #44545e;   /* teks sekunder di atas putih */
--white:    #ffffff;
--sun-400:  #ffc83d;   /* HANYA energi surya: aliran panel, ikon matahari */
--grid-400: #9aa7b0;   /* aliran PLN */
```

### Semantic
```css
--color-bg: var(--white);
--color-bg-soft: var(--blue-50);
--color-bg-deep: var(--navy-900);
--color-text: var(--ink-900);
--color-text-muted: var(--ink-600);
--color-text-on-deep: var(--white);
--color-link: var(--blue-700);
--color-action: var(--blue-500);
--color-on-action: var(--white);        /* permintaan pengguna 23 Okt: teks putih di tombol biru (kontras 2.9:1, di bawah AA) */
--energy-solar: var(--sun-400);
--energy-battery: var(--blue-500);
--energy-grid: var(--grid-400);
--energy-load: var(--white);
```

### Component
```css
--btn-primary-bg: var(--color-action);
--btn-primary-fg: var(--color-on-action);
--btn-ghost-border: rgb(255 255 255 / .45);
--pill-active-bg: var(--color-action);
--radius-pill: 999px;
--radius-card: 16px;
--radius-sm: 8px;
```

### Tipografi
- Keluarga tunggal: **Plus Jakarta Sans** (Google Fonts, 400/500/600/700) — dipilih via `ui-ux-pro-max` (pairing "Friendly SaaS"), buatan desainer Indonesia, dekat dengan grotesk referensi.
- Skala: H1 hero `clamp(2.25rem, 3.8vw, 3.5rem)` / 600 / line-height 1.06 / tracking -0.03em · H2 `clamp(2rem, 4vw, 3.25rem)` / 600 / -0.03em · H3 1.25–1.5rem / 600 · body 1.0625rem / 1.6 · kecil 0.875rem.
- Panjang baris teks isi ≤ 68ch. Tanpa label ALL CAPS.

### Spacing & layout
- Basis 4px: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
- Kontainer 1240px, gutter `clamp(16px, 4vw, 40px)`. Section vertikal `clamp(64px, 10vw, 128px)`.

### Gerak
- Crossfade hero 800ms `cubic-bezier(.2,.7,.2,1)`. Aliran energi: `stroke-dashoffset` linear loop 1.2s.
- `prefers-reduced-motion`: tanpa crossfade & aliran diam (panah statis).

## Aturan konten (dari CLAUDE.md)
- H1 hero: frasa "PLTS Hybrid" diberi warna biru brand (`--blue-500`).
- Tepat satu H1: "Kontraktor PLTS Hybrid di Seluruh Indonesia" (layanan nasional; kantor Surabaya & Jabodetabek disebut di baris bukti); subjudul "Listrik tetap menyala siang, malam, bahkan saat PLN padam."
- Tidak ada aliran/klaim ekspor listrik ke PLN.
- CTA utama: WhatsApp Jabodetabek 0814-1225-0644.
- Harga paket hybrid boleh tampil (harga material, belum termasuk pemasangan). Jangan tampilkan kisaran biaya pemasangan.
- Implementasi akhir: blok inti Gutenberg + Kadence Global Palette (palette1 = blue-500, palette2 = navy-900, palette3 = ink-900, palette7 = blue-50, palette9 = white).
