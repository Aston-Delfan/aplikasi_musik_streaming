# aplikasi_musik_streaming

## Identitas
- Nama kelompok: (isi)
- Anggota: (isi nama dan NIM seluruh anggota)
- Studi kasus UTS: Aplikasi Musik Streaming

## Deskripsi Sistem
Aplikasi musik streaming sederhana. `Audio` adalah class induk dengan turunan `Lagu` dan `EpisodePodcast`. `Pengguna` memiliki kumpulan `Playlist` dan terbagi menjadi `PenggunaFree` (diiklankan dan dibatasi skip) serta `PenggunaPremium` (dapat mengunduh lewat `DownloadMixin`). Pada tugas P9, setiap penolakan data atau pelanggaran aturan bisnis dilaporkan melalui custom exception, bukan `print` atau nilai kembalian.

## Tabel Aturan Bisnis
| Aturan | Class/Method | Exception |
|---|---|---|
| Durasi audio harus lebih dari 0 detik | `Audio.durasi` (setter) | `DurasiTidakValidError` |
| Teks lagu harus berformat judul-artis-menit:detik | `Lagu.dari_teks` | `FormatTeksLaguError` |
| Nama playlist tidak boleh kosong | `Playlist.nama` (setter) | `NamaPlaylistKosongError` |
| Lagu yang sama tidak boleh ditambahkan dua kali | `Playlist.tambah_lagu` | `LaguDuplikatError` |
| Pengguna Free dibatasi 6 kali skip | `PenggunaFree.skip` | `BatasSkipHabisError` |
| Username tidak boleh kosong | `Pengguna.username` (setter) | `UsernameKosongError` |
| Audio yang sama tidak boleh diunduh dua kali | `DownloadMixin.unduh` | `UnduhanDuplikatError` |

## Class Diagram Revisi
![Class Diagram](docs/class-diagram.png)

## Daftar Custom Exception
| Nama | Class induk | Atribut konteks | Kapan dimunculkan | Method | Penanganan |
|---|---|---|---|---|---|
| `MusikStreamingError` | `Exception` | - | Base exception aplikasi | - | Penangkap umum di `main` |
| `DurasiTidakValidError` | `MusikStreamingError` | `durasi` | Durasi kurang dari atau sama dengan 0 | `Audio.durasi` | Pesan gagal ubah durasi |
| `FormatTeksLaguError` | `MusikStreamingError` | `teks` | Teks lagu salah format | `Lagu.dari_teks` | Pesan gagal beserta `__cause__` |
| `NamaPlaylistKosongError` | `MusikStreamingError` | `nama` | Nama playlist kosong | `Playlist.nama` | Pesan gagal membuat playlist |
| `LaguDuplikatError` | `MusikStreamingError` | `playlist`, `judul` | Lagu sudah ada di playlist | `Playlist.tambah_lagu` | Pesan gagal tambah lagu |
| `BatasSkipHabisError` | `MusikStreamingError` | `username`, `batas` | Sisa skip habis | `PenggunaFree.skip` | Pesan gagal skip |
| `UsernameKosongError` | `MusikStreamingError` | `username` | Username kosong | `Pengguna.username` | Pesan gagal membuat pengguna |
| `UnduhanDuplikatError` | `MusikStreamingError` | `username`, `judul` | Audio sudah pernah diunduh | `DownloadMixin.unduh` | Pesan gagal unduh |

## Penerapan Exception Handling
- `try/except/else/finally`: dipakai pada penambahan lagu ke playlist di `main.py`, dengan urutan `except` dari spesifik (`LaguDuplikatError`) ke umum (`MusikStreamingError`).
- `raise ... from e`: dipakai pada `Lagu.dari_teks`, penyebab aslinya ditampilkan lewat `e.__cause__`.
- EAFP: `Lagu.dari_teks` langsung melakukan `split` dan `int`, lalu menangkap `ValueError`. Di `main.py`, operasi `tambah_lagu`, `skip`, dan `unduh` langsung dijalankan di dalam `try`, lalu kegagalannya ditangkap tanpa pemeriksaan di muka.
- LBYL: `Playlist.tambah_lagu`, `PenggunaFree.skip`, dan `DownloadMixin.unduh` memeriksa aturan bisnis lebih dulu karena murah diperiksa.
- Class domain tidak mencetak pesan error. Penampilan pesan dilakukan di `main.py`.

## Cara Menjalankan
```
python src/main.py
```

## Pembagian Peran
| Anggota | Peran |
|---|---|
| Anggota 1 | `exceptions.py` (base), `audio.py`, `lagu.py`, `episode_podcast.py`, class diagram |
| Anggota 2 | `playlist.py`, README |
| Anggota 3 | `pengguna.py`, `main.py`, output program |