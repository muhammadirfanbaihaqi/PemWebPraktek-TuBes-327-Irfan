from . import db
# Mengimpor objek db (SQLAlchemy) dari file yang sama (diinisialisasi di __init__.py).

# Mendefinisikan kelas User sebagai model yang diwarisi dari db.Model. Ini berarti kelas ini akan berhubungan dengan tabel dalam basis data.
class User(db.Model):
    # Menentukan nama tabel dalam basis data yang akan diwakili oleh model ini, yaitu users.
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True) #Mendefinisikan kolom id sebagai kolom integer dan menetapkannya sebagai kunci utama (primary key) tabel.
    name = db.Column(db.String(80), nullable = False) #Mendefinisikan kolom name sebagai string dengan panjang maksimal 80 karakter dan kolom ini tidak boleh kosong (nullable=False).
    email = db.Column(db.String(120), unique=True, nullable=False) #Mendefinisikan kolom email sebagai string dengan panjang maksimal 120 karakter, harus unik (tidak boleh ada duplikat), dan kolom ini tidak boleh kosong (nullable=False).


    # Metode __repr__ digunakan untuk menentukan representasi string dari objek User. Ini digunakan untuk debugging dan pencetakan objek.
    def __repr__(self):
        return f"<User {self.name}"
    


# FILE INI DIGUNAKAN UNTUK :
# mendefinisikan model basis data untuk entitas User. Model ini mendefinisikan tabel dalam basis data dan kolom-kolomnya.

# UNTUK MENJALANKAN MIGRASI ATAU
# MEMBUAT TABEL INI DI DALAM DATABASE YANG SUDAH DITENTUKAN
# catatan : Di __init__.py, kita menginisialisasi objek Migrate untuk mendukung migrasi basis data.

# J A L A N K A N >> PERINTAH DI BAWAH INI PADA COMMAND PROMT UNTUK MELAKUKAN MIGRATE:
# 1. python -m flask db init
# 2. python -m flask db migrate -m "Initial migration"
# 3. python -m flask db upgrade

#  A T A U bisa juga :
# flask db init
# flask db migrate -m "create users table"
# flask db upgrade

# MAKA TABEL AKAN BENAR BENAR AKAN TERBUAT DI DALAM DATABASE YANG SUDAH DITENTUKAN

