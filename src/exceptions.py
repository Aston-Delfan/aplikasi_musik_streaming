class MusikStreamingError(Exception):
    pass


class DurasiTidakValidError(MusikStreamingError):
    def __init__(self, durasi):
        self.durasi = durasi
        super().__init__(f"Durasi harus lebih dari 0 detik, diberikan {durasi}")


class FormatTeksLaguError(MusikStreamingError):
    def __init__(self, teks):
        self.teks = teks
        super().__init__(f"Format teks lagu '{teks}' tidak valid, gunakan judul-artis-menit:detik")