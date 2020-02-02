from flask import Flask, render_template, request, redirect
import sqlite3

def get_db():
    db = sqlite3.connect('students')
    return db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('firstName').strip()
    last_name = request.form.get('lastName').strip()
    email = request.form.get('email').strip()
    university = request.form.get('university').strip()

    rows = { 'first': first_name, 'last': last_name, 'email': email, 'university':university }

    db = get_db()

    insert_statement = "INSERT INTO students VALUES (:first, :last, :email, :university)"
    
    db.cursor().execute(insert_statement, rows)
    db.commit()
    db.close()

    return redirect('/registered')

@app.route('/registered')
def registered():
    db = get_db()

    select_statement = "SELECT * FROM students"
    rows = db.cursor().execute(select_statement)

    return render_template('registered.html', rows=rows)
