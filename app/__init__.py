# pip install flask python-dotenv flask-sqlalchemy flask-migrate || MODUL YANG DIBUTUHKAN
# flask: kerangka kerja web

# python-dotenv: memuat variabel lingkungan dari file .env

# flask-sqlalchemy: integrasi SQLAlchemy dengan Flask untuk manajemen basis data

# flask-migrate: mendukung migrasi basis data untuk aplikasi Flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
# from .config import Config  # JIKA INGIN MENGKONFIG DENGAN LEBIH RAPI

load_dotenv() 
# load_dotenv(): Memuat variabel lingkungan dari file .env ke dalam lingkungan aplikasi.

# menginisialisasi objek SQLAlchemy (db) dan Migrate (migrate):
db = SQLAlchemy() 
# SQLAlchemy(): Digunakan untuk mengelola basis data.

migrate = Migrate()
# Migrate(): Digunakan untuk mendukung migrasi basis data.

def create_app(): #Fungsi create_app adalah fungsi pabrik yang membuat dan mengonfigurasi instance aplikasi Flask:
    app = Flask(__name__)


    # Aplikasi dikonfigurasi untuk menggunakan URI basis data dari variabel lingkungan (DATABASE_URI) dan menonaktifkan pelacakan modifikasi:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    # os.getenv('DATABASE_URI'): Mengambil nilai variabel lingkungan DATABASE_URI.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # JIKA INGIN MENGGUNAKAN PENGATURAN YANG LEBIH RAPI, BISA MEMANFAATKAN PENGATURAN DI FILE CONFIG.PY
    # app.config.from_object(Config)

    # Inisialisasi SQLAlchemy dan Migrate dengan aplikasi
    db.init_app(app)
    migrate.init_app(app, db)

    # Mendaftarkan blueprint utama (main) yang berisi route-route yang akan digunakan di aplikasi
    from .routes import main
    app.register_blueprint(main)
    return app

