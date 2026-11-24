from exceptions import DurasiTidakValidError


class Audio:
    jumlah_audio = 0

    def __init__(self, judul, durasi):
        self._judul = judul
        self.durasi = durasi
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
            raise DurasiTidakValidError(nilai)
        self._durasi = nilai

    @staticmethod
    def format_durasi(detik):
        return f"{detik // 60}:{detik % 60:02d}"

    def putar(self):
        return f"Memutar {self._judul}"