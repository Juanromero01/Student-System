from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Coopeer123@4",
    database="student_db"
)

cursor = db.cursor()


@app.route('/')
def home():

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    return render_template("home.html", students=students)

@app.route('/add', methods=['POST'])
def add():

    name = request.form['name']
    age = request.form['age']
    major = request.form['major']

    sql = "INSERT INTO students (name, age, major) VALUES (%s, %s, %s)"
    values = (name, age, major)

    cursor.execute(sql, values)
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)