from audio import Audio
from episode_podcast import EpisodePodcast
from exceptions import (
    BatasSkipHabisError,
    DurasiTidakValidError,
    FormatTeksLaguError,
    LaguDuplikatError,
    MusikStreamingError,
    NamaPlaylistKosongError,
    UnduhanDuplikatError,
    UsernameKosongError,
)
from lagu import Lagu
from pengguna import PenggunaFree, PenggunaPremium


def main():
    lagu1 = Lagu("Senja di Kuta", 215, "Arya")
    lagu2 = Lagu.dari_teks("Langit Biru-Dewi-3:48")
    lagu3 = Lagu("Senja di Kuta", 215, "Arya")
    lagu4 = Lagu("Iqro", 215, "Raim Laode")
    podcast = EpisodePodcast("Ngobrol Teknologi", 1800, "Budi", 12)
    podcast1 = EpisodePodcast("Ngobrol Prabowo", 2000, "Prabowo", 17)

    free = PenggunaFree("ibal")
    premium = PenggunaPremium("sari")

    santai = premium.buat_playlist("Lagu Santai")
    santai.tambah_lagu(lagu1)
    santai.tambah_lagu(lagu2)

    print("=== PLAYLIST ===")
    for lagu in [lagu4, lagu3]:
        try:
            santai.tambah_lagu(lagu)
        except LaguDuplikatError as e:
            print(f"Gagal tambah lagu: {e}")
        except MusikStreamingError as e:
            print(f"Gagal: {e}")
        else:
            print(f"Berhasil menambahkan {lagu.judul}")
        finally:
            print(f"[LOG] percobaan tambah lagu {lagu.judul}")
    print(santai)

    print("\n=== PENGGUNA FREE ===")
    print(free.putar(lagu1))
    for _ in range(PenggunaFree.BATAS_SKIP + 1):
        try:
            print(free.skip())
        except BatasSkipHabisError as e:
            print(f"Gagal skip: {e}")

    print("\n=== PENGGUNA PREMIUM ===")
    print(premium.putar(podcast))
    print(premium.unduh(lagu2))
    try:
        premium.unduh(lagu2)
    except UnduhanDuplikatError as e:
        print(f"Gagal unduh: {e}")

    print("\n=== VALIDASI DAN PERBANDINGAN ===")
    try:
        lagu2.durasi = -10
    except DurasiTidakValidError as e:
        print(f"Gagal ubah durasi: {e}")

    try:
        Lagu.dari_teks("Langit Biru-Dewi")
    except FormatTeksLaguError as e:
        print(f"Gagal membuat lagu: {e}")
        print(f"Penyebab: {e.__cause__}")

    try:
        premium.buat_playlist("   ")
    except NamaPlaylistKosongError as e:
        print(f"Gagal membuat playlist: {e}")

    try:
        PenggunaFree("   ")
    except UsernameKosongError as e:
        print(f"Gagal membuat pengguna: {e}")

    print(f"lagu1 == lagu3: {lagu1 == lagu3}")
    print(f"lagu1 == lagu2: {lagu1 == lagu2}")
    print(f"Jumlah audio: {Audio.jumlah_audio}")
    print(f"MRO Premium: {' -> '.join(cls.__name__ for cls in PenggunaPremium.mro())}")

    print(podcast)
    print(santai)
    print(lagu1)


if __name__ == "__main__":
    main()