# Rencana Pemasangan Homepage Gutenberg

## File

| File | Isi |
|---|---|
| `blocks/homepage.html` | Markup blok core Gutenberg homepage (sumber) |
| `blocks/kalkulator-plts.html` | Kalkulator PLTS (blok Custom HTML), di-include ke homepage |
| `blocks/homepage.css` | Gaya `.rn-*` untuk Customizer → Additional CSS |
| `scripts/build.py` | Menggabungkan file di atas → `build/homepage.html` dan memastikan tepat satu `<h1>` |

## Keputusan yang sudah diambil (22 Okt 2026)

1. Counter ditulis statis: **14.375.000+ kWh** per tahun.
2. Kalkulator: "Estimasi Investasi" & "Payback" dihapus, diganti **paket katalog** yang sesuai (harga material Agustus 2026, dengan catatan "belum termasuk pemasangan"). Paket 5 kW + 16 kWh (Rp 92 jt) tidak dimasukkan. On-grid dan kapasitas di luar katalog → "sesuai hasil survei".
3. Popup "Alokasi Kuota Terbatas" **dihapus**. Tombol WhatsApp melayang sudah disediakan plugin WP Chat App di semua halaman (desktop & mobile), ditambah seksi kontak dua kantor di akhir homepage.

## Perubahan konten penting

- H1: "Kontraktor PLTS Surabaya & Jabodetabek" (satu-satunya H1).
- Seksi baru "Listrik Surya Paling Hemat Bila Dipakai Sendiri" menjelaskan Permen ESDM No. 2/2024 → alasan hybrid + baterai.
- Kartu solusi diurutkan Hybrid (ditonjolkan) → Off-Grid → On-Grid. Deskripsi On-Grid tidak lagi menyebut penyaluran kelebihan listrik ke jaringan.
- Kalkulator: penghematan on-grid dibatasi porsi pemakaian siang (residensial 40%, komersial/industri 70%); hybrid/off-grid dibatasi sebesar konsumsi. Nama pengguna di-escape. Heading internal kalkulator diubah ke `<p>` agar struktur heading halaman tetap rapi. Font mengikuti tema (Google Font Plus Jakarta Sans tidak lagi dimuat).
- Semua gambar konten diberi alt text; ikon SVG dekoratif `alt=""`.

## Langkah pemasangan (satu request per waktu)

1. **Draft pratinjau** — buat halaman baru berstatus *draft* (bukan menimpa ID 3280) berisi `build/homepage.html`, lalu buat preview link.
   - Cek: `<script>` kalkulator masih ada setelah disimpan (butuh kapabilitas `unfiltered_html`). Jika terhapus, kalkulator perlu dipasang via WPCode/Code Snippets sebagai shortcode.
2. **CSS** — baca dulu Additional CSS yang ada (`wp_get_custom_css`), lalu *tambahkan* isi `blocks/homepage.css` di bawahnya (jangan menimpa).
3. **Review** oleh pemilik situs di preview link (desktop & mobile).
4. **Go-live ke ID 3280** (setelah disetujui):
   - Simpan revisi/undo token; pastikan backup tersedia di luar server.
   - Ganti `post_content` ID 3280 dengan `build/homepage.html`.
   - Matikan Elementor untuk halaman ini: hapus/kosongkan meta `_elementor_edit_mode` (jika diizinkan MCP; jika tidak, klik "Back to WordPress Editor" di editor).
   - **Manual di editor:** template halaman → Default (Kadence). Pengaturan Kadence: Page Title = *Hide* (agar judul post tidak menjadi H1 kedua), Layout = Fullwidth, Content Style = Unboxed, Vertical Padding = Hide.
   - Jangan ubah slug, title Yoast, atau meta description Yoast.
5. **Verifikasi** (satu request): halaman merender tepat 1 H1, angka 14.375.000+ ada di HTML, link kartu & artikel benar, title Yoast tetap "Kontraktor PLTS Surabaya & Jabodetabek - Renus Global Indonesia".

## Masih terbuka

- **Nama klien per logo** — 11 file `Untitled-3-01-*.png`, `JATIM-1`, dan `Logo-Biru-Muda` masih ber-alt "Logo klien Renus". Yang sudah dikenali: PUPR (3856), ITS (3814).
- **`/pasang-plts-untuk-bisnis/`** belum terkonfirmasi lewat pencarian MCP; cek saat preview.
- **Pemetaan kWp → paket**: kapasitas paket katalog (kW inverter) dipetakan langsung dari kWp hasil hitung. Mohon dikonfirmasi tim teknis.
- **Alt text foto** ditulis berdasarkan nama file & konteks (mis. "JIIPe" → kawasan industri JIIPE Gresik); mohon dicek kecocokannya.
