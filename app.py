from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Create a connection to the SQLite database
conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()

# Create a table for users if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, username TEXT UNIQUE, password TEXT)''')
conn.commit()


@app.route('/')
def welcome():
    return render_template('welcome2.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Check if the username or email already exists in the database
        c.execute("SELECT * FROM users WHERE email=? OR username=?", (email, username))
        result = c.fetchone()

        if result:
            error = 'Username or email already exists!'
            return render_template('signup.html', error=error)
        else:
            # Hash the password
            hashed_password = generate_password_hash(password)

            # Insert the user into the database
            c.execute("INSERT INTO users (email, username, password) VALUES (?, ?, ?)",
                      (email, username, hashed_password))
            conn.commit()
            return redirect(url_for('login'))
    else:
        error = request.args.get('error')
        return render_template('signup.html', error=error)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists in the database
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()

        if user and check_password_hash(user[3], password):
            # Store user details in session
            session['user_id'] = user[0]
            session['username'] = user[2]
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password!'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        # User is logged in, retrieve user details from session
        user_id = session['user_id']
        username = session['username']
        return render_template('dashboard1.html', username=username)
    else:
        return render_template('welcome2.html')

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return render_template('welcome2.html')


@app.route('/user')
def user():
    user_id = session['user_id']
    username = session['username']
    return render_template('userpage.html', username=username)


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
