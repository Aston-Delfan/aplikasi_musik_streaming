from audio import Audio
from exceptions import FormatTeksLaguError


class Lagu(Audio):
    def __init__(self, judul, durasi, artis):
        super().__init__(judul, durasi)
        self._artis = artis

    @property
    def artis(self):
        return self._artis

    @classmethod
    def dari_teks(cls, teks):
        try:
            judul, artis, waktu = teks.split("-")
            menit, detik = waktu.split(":")
            return cls(judul, int(menit) * 60 + int(detik), artis)
        except ValueError as e:
            raise FormatTeksLaguError(teks) from e

    def putar(self):
        return f"Memutar lagu {self.judul} oleh {self._artis}"

    def __str__(self):
        return f"{self.judul} oleh {self._artis} ({Audio.format_durasi(self.durasi)})"

    def __eq__(self, other):
        return isinstance(other, Lagu) and self.judul == other.judul and self._artis == other._artis