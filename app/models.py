from . import db

# Mendefinisikan kelas User sebagai model yang diwarisi dari db.Model. Ini berarti kelas ini akan berhubungan dengan tabel dalam basis data.
class User(db.Model):
    # Menentukan nama tabel dalam basis data yang akan diwakili oleh model ini, yaitu users.
    __tablename__ = 'users'

    # Mendefinisikan kolom id sebagai kolom integer dan menetapkannya sebagai kunci utama (primary key) tabel.
    id = db.Column(db.Integer, primary_key=True)
    # Mendefinisikan kolom username sebagai string dengan panjang maksimal 80 karakter dan kolom ini tidak boleh kosong (nullable=False).
    username = db.Column(db.String(80), nullable=False)
    # Mendefinisikan kolom role sebagai string dengan panjang maksimal 80 karakter dan kolom ini tidak boleh kosong (nullable=False).
    role = db.Column(db.String(80), nullable=False)
    # Mendefinisikan kolom email sebagai string dengan panjang maksimal 120 karakter, harus unik (tidak boleh ada duplikat), dan kolom ini tidak boleh kosong (nullable=False).
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Mendefinisikan kolom password_hash sebagai string dengan panjang maksimal 128 karakter dan kolom ini tidak boleh kosong (nullable=False).
    password_hash = db.Column(db.String(128), nullable=False)

    # Metode __repr__ digunakan untuk menentukan representasi string dari objek User. Ini digunakan untuk debugging dan pencetakan objek.
    def __repr__(self):
        return f"<User {self.username}>"


# untuk melakuan migrasi  database, harus menggunakan flask db init, flask db migrate, dan flask db upgrade