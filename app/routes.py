from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash, session
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from generate_id import GenerateID as GI

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def awal():
    if 'loggedin' in session:
        # membedakan tampilan home untuk admin dan user biasa
        if session['role'] == 'admin':
            return redirect(url_for('main.homeadmin'))
        else:
            return redirect(url_for('main.home'))
    else:
        flash('Please log in to acces this page.', 'warning')
        return redirect(url_for('main.login'))
    
@main.route('/home')
def home():
    if 'loggedin' in session:
        if session['role'] == 'user':
            data = User.query.all()
            return render_template('home.html', users=data)
        else:
            flash('You are not authorized to access this page.', 'danger')
            return redirect(url_for('main.logout'))
    else:
        flash('Please log in to acces this page.', 'warning')
        return redirect(url_for('main.login'))
    

@main.route('/homeadmin', methods=['GET', 'POST'])
def homeadmin():
    if 'loggedin' in session:
        if session['role'] == 'admin':
            data = User.query.all()
            return render_template('homeadmin.html', users=data, session_id=session['id'])
        else:
            flash('You are not authorized to access this page.', 'danger')
            return redirect(url_for('main.logout'))
    else:
        flash('Please log in to acces this page.', 'warning')
        return redirect(url_for('main.login'))
    
@main.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if 'loggedin' in session and session['role'] == 'admin':
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
    else:
        flash('You are not authorized to perform this action.', 'danger')
        return redirect(url_for('main.logout'))



@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):  # Verifikasi password
            # MEMBUAT SESSION
            session['loggedin'] = True 
            session['id'] = user.id
            session['name'] = user.username
            session['role'] = user.role
            flash('Login successful!', 'success')
            # membedakan akses login untuk admin dengan user biasa
            if user.role == 'admin':
                return redirect(url_for('main.homeadmin'))
            else:
                return redirect(url_for('main.home'))

        else:
            flash('Invalid email or password!', 'danger')

    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = 'user' # Default role is 'user' , jika membuat dari form register, maka role defaultnya user
        id_user = GI.generate_id()

        # Hash password before saving to the database
        hashed_password = generate_password_hash(password)

        # Create a new user and add it to the database
        new_user = User(username=username, email=email, password_hash=hashed_password, role=role, id=id_user)
        db.session.add(new_user)
        db.session.commit()

        flash('You have successfully registered! Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/logout', methods=['POST', 'DELETE', 'GET'])
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('role', None)  # Remove role from session too, in case it exists.
    #The None argument ensures that no error is raised if the key doesn't exist. 
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.login'))


@main.route('/adduser', methods=['POST', 'GET','PUT'])
def adduser():
    if 'loggedin' in session and  session['role'] == 'admin':
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            role = request.form['role']
            id_user = GI.generate_id()
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, email=email, password_hash=hashed_password, role=role, id=id_user)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('main.adduser'))
        return render_template('adduser.html')
    else:
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('main.logout'))





# @main.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = User.query.get(user_id)
#     if user:
#         return jsonify(
#             {'id':user.id, 'username': user.username, 'email': user.email }, 201
#         )
#     else:
#         return jsonify({'message': 'User not found'},404)
    

# @main.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({'message': 'User not found'},404)
#     data = request.get_json()
#     name = data.get('name')
#     email = data.get('email')
#     if not name or not email:
#         return jsonify({'message': 'Name and email are required'}), 400
#     user.name = name
#     user.email = email
#     db.session.commit()
#     return jsonify({'message': 'User updated successfully', "user": {"id" : user.id, "name": user.name, "email": user.email}}), 200



