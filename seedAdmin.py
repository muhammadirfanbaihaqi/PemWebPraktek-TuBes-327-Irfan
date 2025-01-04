from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Menghapus admin jika sudah ada sebelumnya (opsional)
    User.query.filter_by(username='admin').delete()
    db.session.commit()

    # Membuat admin baru
    admin = User(
        id=12345,
        username='admin',
        email='admin@example.com',
        password_hash=generate_password_hash('adminpassword', method='pbkdf2:sha256'),
        role='admin'
    )

    # Menambahkan admin ke database
    db.session.add(admin)
    db.session.commit()

    print('Admin berhasil ditambahkan ke database.')

#  JALANKAN KODE INI UNTUK MENAMBAHKAN SEED ADMIN ATAU ADMIN ROOT