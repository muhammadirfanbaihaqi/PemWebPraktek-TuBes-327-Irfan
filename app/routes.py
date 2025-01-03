from flask import Blueprint, jsonify, request
from .models import User
from . import db

main = Blueprint('main', __name__)

# C A T A T A N
# Blueprint adalah objek yang digunakan untuk mengelompokkan rute-rute (route) dalam aplikasi Flask.
# __name__ adalah nama modul saat ini, yang digunakan untuk mengidentifikasi blueprint.

#  QUERY KE DATABASE berbeda dengan query sql biasa
# hal ini dikarenakan pada kasus ini kita menggunakan ORM (Object-Relational Mapping) , dengan SQLAlchemy
# ORM adalah teknik pemrograman yang menghubungkan kelas-kelas dalam kode kita dengan tabel-tabel dalam basis data.
# Dengan ORM, kita bisa menggunakan objek dan metode dalam bahasa pemrograman yang kita gunakan (dalam hal ini Python) untuk berinteraksi dengan basis data, 
# tanpa perlu menulis kueri SQL secara langsung.
# alih-alih mengembalikan baris-baris sebagai hasil kueri SQL, 
# QUERY dengan ORM  mengembalikan daftar objek yang dapat kita manipulasi dalam kode Python.

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all() #QUERY BERBEDA DENGAN SQL BIASA, TAPI SAMA SAMA DIGUNAKAN UNTUK MENGAMBIL DATA DARI DATABASE
    return jsonify(
        [
            {'id':user.id, 'name': user.name, 'email': user.email } for user in users
        ]
    )

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(
            {'id':user.id, 'name': user.name, 'email': user.email }, 201
        )
    else:
        return jsonify({'message': 'User not found'},404)
    
@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', "user": {"id" : new_user.id, "name": new_user.name, "email": new_user.email}}), 201

@main.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'},404)
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400
    user.name = name
    user.email = email
    db.session.commit()
    return jsonify({'message': 'User updated successfully', "user": {"id" : user.id, "name": user.name, "email": user.email}}), 200


@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'},404)

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

