from audio import Audio
from exceptions import LaguDuplikatError, NamaPlaylistKosongError


class Playlist:
    def __init__(self, nama):
        self.nama = nama
        self._daftar_lagu = []

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):
        if not nilai.strip():
            raise NamaPlaylistKosongError(nilai)
        self._nama = nilai

    def tambah_lagu(self, lagu):
        if lagu in self._daftar_lagu:
            raise LaguDuplikatError(self._nama, lagu.judul)
        self._daftar_lagu.append(lagu)

    def __str__(self):
        total = sum(lagu.durasi for lagu in self._daftar_lagu)
        return f"Playlist {self._nama}: {len(self._daftar_lagu)} lagu, {Audio.format_durasi(total)}"