from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def close_db_connection(conn):
    if conn:
        conn.close()

@app.before_first_request
def create_table():
    conn = get_db_connection()
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, username TEXT UNIQUE, password TEXT)''')
    close_db_connection(conn)

@app.route('/')
def welcome():
    return render_template('welcome2.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        try:
            # Check if the username or email already exists in the database
            user = conn.execute("SELECT * FROM users WHERE email=? OR username=?", (email, username)).fetchone()

            if user:
                flash('Username or email already exists!', 'error')
                return redirect(url_for('signup'))

            # Hash the password
            hashed_password = generate_password_hash(password)

            # Insert the user into the database
            conn.execute("INSERT INTO users (email, username, password) VALUES (?, ?, ?)",
                         (email, username, hashed_password))
            conn.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError as e:
            flash(f'Error: {e}', 'error')
        finally:
            close_db_connection(conn)
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        try:
            # Check if the username exists in the database
            user = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()

            if user and check_password_hash(user['password'], password):
                # Store user details in session
                session['user_id'] = user['id']
                session['username'] = user['username']
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password!', 'error')
                return redirect(url_for('login'))
        finally:
            close_db_connection(conn)
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard1.html', username=session['username'])
    else:
        flash('You need to log in to access this page.', 'warning')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('welcome'))

@app.route('/user')
def user():
    if 'user_id' in session:
        return render_template('userpage.html', username=session['username'])
    else:
        flash('You need to log in to access this page.', 'warning')
        return redirect(url_for('login'))

@app.route('/allproducts')
def allproducts():
    return render_template('Allproducts.html')

@app.route('/contactus')
def contactus():
    return render_template('Contact.html')

@app.route('/facebook')
def facebook():
    return redirect('https://www.facebook.com')

@app.route('/twitter')
def twitter():
    return redirect('https://www.twitter.com')

@app.route('/youtube')
def youtube():
    return redirect('https://www.youtube.com')

@app.route('/instagram')
def instagram():
    return redirect('https://www.instagram.com')

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)
