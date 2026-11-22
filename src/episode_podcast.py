from audio import Audio


class EpisodePodcast(Audio):
    def __init__(self, judul, durasi, host, nomor):
        super().__init__(judul, durasi)
        self._host = host
        self._nomor = nomor

    def putar(self):
        return f"Memutar podcast {self.judul} eps. {self._nomor} bersama {self._host}"
