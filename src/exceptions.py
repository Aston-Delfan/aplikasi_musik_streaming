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



class BatasSkipHabisError(MusikStreamingError):
    def __init__(self, username, batas):
        self.username = username
        self.batas = batas
        super().__init__("Batas skip habis, upgrade ke Premium")


class UsernameKosongError(MusikStreamingError):
    def __init__(self, username):
        self.username = username
        super().__init__("Username tidak boleh kosong")


class UnduhanDuplikatError(MusikStreamingError):
    def __init__(self, username, judul):
        self.username = username
        self.judul = judul
        super().__init__(f"Audio '{judul}' sudah diunduh oleh {username}")