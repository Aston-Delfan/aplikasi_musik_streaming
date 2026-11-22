from audio import Audio
from episode_podcast import EpisodePodcast
from exceptions import DurasiTidakValidError
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
    print(f"Tambah lagu duplikat: {santai.tambah_lagu(lagu3)}")
    print(santai)

    print("\n=== PENGGUNA FREE ===")
    print(free.putar(lagu1))
    print(free.skip())

    print("\n=== PENGGUNA PREMIUM ===")
    print(premium.putar(podcast))
    print(premium.unduh(lagu2))

    print("\n=== VALIDASI DAN PERBANDINGAN ===")
    try:
        lagu2.durasi = -10
    except DurasiTidakValidError as e:
        print(f"Gagal ubah durasi: {e}")
    print(f"lagu1 == lagu3: {lagu1 == lagu3}")
    print(f"lagu1 == lagu2: {lagu1 == lagu2}")
    print(f"Jumlah audio: {Audio.jumlah_audio}")
    print(f"MRO Premium: {' -> '.join(cls.__name__ for cls in PenggunaPremium.mro())}")

    print(podcast)
    print(santai)
    print(lagu1)


if __name__ == "__main__":
    main()
