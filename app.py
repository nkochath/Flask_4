from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    if not check_user_exists(email):
        create_user(email, password)
    else:
        print('User exists')
        return redirect('/')

    return redirect('/user_home')

@app.route('/user_home')
def user_home():
    return render_template('user_home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    if not check_user_exists(email):
        print('You are not signed up.')
        return redirect('/')

    if check_password(email, password):
        return redirect('/user_home')

@app.route('/new_task', methods=['POST'])
def new_task():
    task_name = request.form.get('task_name')
    task_description = request.form.get('task_description')
    write_task(task_name, task_description)

    return redirect('/user_home')

@app.route('/edittask', methods=['POST'])
def edit_task():
    name = request.form.get('name')
    description = request.form.get('description')
    db = get_db()
    sql = 'UPDATE tasks SET description = :description WHERE name = :name'
    with db:
        db.cursor().execute(sql, {'name': name, 'description': description})
    return "Task Updated"

@app.route('/tasks')
def tasks():
    tasks = get_tasks()
    return render_template('tasks.html', tasks=tasks)

@app.route('/deletetask', methods=['POST'])
def delete():
    name = request.form.get('name')

    db = get_db()
    sql = 'DELETE FROM tasks WHERE name = :name'
    with db:
        db.cursor().execute(sql, {'name': name})
    return "Task Deleted"

def get_tasks():
    db = get_db()
    sql = 'SELECT * FROM tasks'
    with db:
        rows = db.cursor().execute(sql)
        return rows.fetchall()


def check_password(email, password):
    db = get_db()
    sql = 'SELECT * FROM users WHERE email = :email'
    with db:
        rows = db.cursor().execute(sql, {'email': email})
        user = rows.fetchone()
        print(user)
        return True


def create_user(email, password):
    db = get_db()
    user = {'email': email, 'password': password}
    sql = 'INSERT INTO users (email, password) VALUES (:email, :password)'
    with db:
        db.cursor().execute(sql, user)

def check_user_exists(email):
    db = get_db()
    sql = 'SELECT * FROM users WHERE email = :email'
    with db:
        users = db.cursor().execute(sql, {'email': email}).fetchall()

        if len(users) > 0:
            print('User exists returning True.')
            return True
        else:
            print('User does not exist returning False.')
            return False
def write_task(name, description):
    task = {'name': name, 'description':description}

    db = get_db()
    sql = 'INSERT INTO tasks (name, description) VALUES (:name, :description)'
    with db:
        db.cursor().execute(sql, task)

def get_db():
    db = sqlite3.connect('tasks.db')
    return db

if __name__ == '__main__':
    app.run(debug=True)
