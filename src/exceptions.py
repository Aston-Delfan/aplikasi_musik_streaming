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



class NamaPlaylistKosongError(MusikStreamingError):
    def __init__(self, nama):
        self.nama = nama
        super().__init__("Nama playlist tidak boleh kosong")


class LaguDuplikatError(MusikStreamingError):
    def __init__(self, playlist, judul):
        self.playlist = playlist
        self.judul = judul
        super().__init__(f"Lagu '{judul}' sudah ada di playlist {playlist}")