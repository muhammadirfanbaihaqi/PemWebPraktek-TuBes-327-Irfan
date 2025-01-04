from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()  # Memuat variabel lingkungan dari file .env

# Menginisialisasi objek SQLAlchemy (db) dan Migrate (migrate)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Fungsi create_app adalah fungsi pabrik yang membuat dan mengonfigurasi instance aplikasi Flask
    # Inisialisasi aplikasi Flask
    app = Flask(__name__)  # Mengarahkan ke folder templates
    app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

    # Mengonfigurasi aplikasi untuk menggunakan URI basis data dari variabel lingkungan dan menonaktifkan pelacakan modifikasi
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inisialisasi SQLAlchemy dan Migrate dengan aplikasi
    db.init_app(app)
    migrate.init_app(app, db)

    # Mendaftarkan blueprint utama (main) yang berisi rute-rute yang akan digunakan di aplikasi
    from . routes import main
    app.register_blueprint(main)

    return app
