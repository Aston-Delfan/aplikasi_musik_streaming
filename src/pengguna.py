from playlist import Playlist


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
