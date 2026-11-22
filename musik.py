class Audio:
    jumlah_audio = 0

    def __init__(self, judul, durasi):
        self._judul = judul
        self._durasi = durasi
        Audio.jumlah_audio += 1

    @property
    def judul(self):
        return self._judul

    @property
    def durasi(self):
        return self._durasi

    @durasi.setter
    def durasi(self, nilai):
        if nilai <= 0:
            raise ValueError("Durasi harus lebih dari 0 detik")
        self._durasi = nilai

    @staticmethod
    def format_durasi(detik):
        return f"{detik // 60}:{detik % 60:02d}"

    def putar(self):
        return f"Memutar {self._judul}"


class Lagu(Audio):
    def __init__(self, judul, durasi, artis):
        super().__init__(judul, durasi)
        self._artis = artis

    @property
    def artis(self):
        return self._artis

    @classmethod
    def dari_teks(cls, teks):
        judul, artis, waktu = teks.split("-")
        menit, detik = waktu.split(":")
        return cls(judul, int(menit) * 60 + int(detik), artis)

    def putar(self):
        return f"Memutar lagu {self.judul} oleh {self._artis}"

    def __str__(self):
        return f"{self.judul} oleh {self._artis} ({Audio.format_durasi(self.durasi)})"

    def __eq__(self, other):
        return isinstance(other, Lagu) and self.judul == other.judul and self._artis == other._artis


class EpisodePodcast(Audio):
    def __init__(self, judul, durasi, host, nomor):
        super().__init__(judul, durasi)
        self._host = host
        self._nomor = nomor

    def putar(self):
        return f"Memutar podcast {self.judul} eps. {self._nomor} bersama {self._host}"


class Playlist:
    def __init__(self, nama):
        self._nama = nama
        self._daftar_lagu = []

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):
        if not nilai.strip():
            raise ValueError("Nama playlist tidak boleh kosong")
        self._nama = nilai

    def tambah_lagu(self, lagu):
        if lagu in self._daftar_lagu:
            return False
        self._daftar_lagu.append(lagu)
        return True

    def __str__(self):
        total = sum(lagu.durasi for lagu in self._daftar_lagu)
        return f"Playlist {self._nama}: {len(self._daftar_lagu)} lagu, {Audio.format_durasi(total)}"


class Pengguna:
    def __init__(self, username):
        self._username = username
        self._playlists = [Playlist("Lagu Disukai")]

    def buat_playlist(self, nama):
        playlist = Playlist(nama)
        self._playlists.append(playlist)
        return playlist

    def putar(self, audio):
        return audio.putar()

    def skip(self):
        return f"{self._username} melewati lagu"


class PenggunaFree(Pengguna):
    BATAS_SKIP = 6

    def __init__(self, username):
        super().__init__(username)
        self._sisa_skip = PenggunaFree.BATAS_SKIP

    def putar(self, audio):
        return f"[Iklan] {super().putar(audio)}"

    def skip(self):
        if self._sisa_skip == 0:
            return "Batas skip habis, upgrade ke Premium"
        self._sisa_skip -= 1
        return f"{super().skip()} (sisa skip: {self._sisa_skip})"


class DownloadMixin:
    def __init__(self, *args):
        super().__init__(*args)
        self._unduhan = []

    def unduh(self, audio):
        self._unduhan.append(audio)
        return f"{audio.judul} berhasil diunduh"


class PenggunaPremium(DownloadMixin, Pengguna):
    def __init__(self, username):
        super().__init__(username)
        self._kualitas = "320 kbps"

    def putar(self, audio):
        return f"{super().putar(audio)} [{self._kualitas}]"


if __name__ == "__main__":
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
    except ValueError as e:
        print(f"Gagal ubah durasi: {e}")
    print(f"lagu1 == lagu3: {lagu1 == lagu3}")
    print(f"lagu1 == lagu2: {lagu1 == lagu2}")
    print(f"Jumlah audio: {Audio.jumlah_audio}")
    print(f"MRO Premium: {' -> '.join(cls.__name__ for cls in PenggunaPremium.mro())}")

    print(podcast)
    print(santai)
    print(lagu1)