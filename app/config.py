import os

# mendefinisikan sebuah kelas konfigurasi (Config) untuk aplikasi Flask.
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # Mengambil nilai DATABASE_URI dari variabel lingkungan yang diatur dalam file .env 
    # (yaitu mysql+pymysql://root:@localhost:3306/meetsepuluh). Ini digunakan untuk mengonfigurasi URI basis data yang akan digunakan oleh SQLAlchemy.

    SQLALCHEMY_TRACK_MODIFICATIONS = False


#    C A T A T A N
# kode di file config.py sebenarnya tidak perlu digunakan
# jika semua konfigurasi sudah diatur langsung di dalam fungsi create_app() di file __init__.py. 
# Kedua cara ini pada dasarnya melakukan hal yang sama, yaitu mengonfigurasi aplikasi Flask, tetapi dengan pendekatan yang berbeda.