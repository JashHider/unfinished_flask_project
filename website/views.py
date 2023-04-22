import flask
from flask import Blueprint, render_template, request, url_for, redirect
from sqlalchemy import Column, Integer, String, Numeric, create_engine, text, and_, update
from website import db, conn

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/register', methods=["GET", "POST"])
def create_account():
    return render_template("register.html")

def submit_info():
    # name = request.form["Name"]
    # email = request.form["Email"]
    # password = request.form["Password"]
    # conn.execute(text(f"INSERT INTO accounts (name, email, password) VALUES({name}, {email}, {password})"))
    # print('isTeacher' in request.form)
    max_id = conn.execute(text(f"select max(accountID) + 1 from accounts"), request.form).all()[0][0]
    check = request.form.get('isTeacher')
    if flask.request.method == "POST":
        if check:
            conn.execute(text(f"INSERT INTO accounts (name, email, password, accountID) VALUES(:Name, :Email, :Password, {max_id})"), request.form)
            conn.commit()
            conn.execute(text(f"INSERT INTO teacher (accountID) VALUES({max_id})"), request.form)
            conn.commit()
        else:
            conn.execute(text(f"INSERT INTO accounts (name, email, password, accountID) VALUES(:Name, :Email, :Password, {max_id})"), request.form)
            conn.commit()
            conn.execute(text(f"INSERT INTO student (accountID) VALUES({max_id})"), request.form)
            conn.commit()

        return redirect("/register")


@views.route('/login', methods=["GET"])
def logging_in():
    return render_template("login.html")

@views.route('/login', methods=["POST"])
def login_process():
    email = request.form["Email"]
    password = request.form["Password"]
    user = conn.execute(text(f"SELECT * FROM accounts where email = '{email}' ")).all()[0]
    if user.password == password:
        return render_template("index.html")
    else:
        return "<h1>Login Failed. Email And/Or Password does not match.</h1>"

@views.route('/users', methods=["GET", "POST"])
def show_users():
    userQuery = conn.execute(text(f"SELECT * from accounts;"))
    rows = userQuery.fetchall()
    students = request.form.get("students")
    teachers = request.form.get("teachers")
    filteredStudents = conn.execute(text(f"select * from student inner join accounts on accounts.accountID = student.accountID;"))
    filteredTeachers = conn.execute(text(f"SELECT * from accounts natural join teacher;"))
    if flask.request.method == "POST":
        if students:
            rows = filteredStudents.fetchall()
            return render_template("users.html", users=rows)
        elif teachers:
            rows = filteredTeachers.fetchall()
            return render_template("users.html", users=rows)
    return render_template("users.html", users=rows)

@views.route('/tests', methods=["GET"])
def testList():
    result = db.session.execute(text("select accounts.name, teacher.TID, tests.testName, tests.testID from teacher natural join accounts natural join tests;"))
    rows = result.fetchall()
    return render_template("tests.html", tests=rows)

@views.route('/tests/create', methods=["GET", "POST"])
def create_test():
    return render_template("create_test.html")

# COME BACK TO THIS
def post_test():
    test_id = conn.execute(text(f"select max(testID) from tests"), request.form).all()[0][0]
    if flask.request.method == "POST":
        conn.execute(text(f"INSERT INTO tests (TID, testName) VALUES(:Teacher_ID, :Test_Name)"), request.form)
        conn.commit()
        conn.execute(text(f"INSERT INTO testQuestions (testID, testQuestion, answer) VALUES({test_id}, :question1, :answer1)"), request.form)
        conn.commit()
        conn.execute(text(f"INSERT INTO testQuestions (testID, testQuestion, answer) VALUES({test_id}, :question2, :answer2)"), request.form)
        conn.commit()
        conn.execute(text(f"INSERT INTO testQuestions (testID, testQuestion, answer) VALUES({test_id}, :question3, :answer3)"), request.form)
        conn.commit()
        return redirect("/tests")

@views.route('/testing', methods=["GET"])
def in_test():
    requests = request.args.get("ID")
    result1 = db.session.execute(text(f"select testName, testID, testQuestion, answer from testQuestions natural join tests where testID ={requests};"))
    rows = result1.fetchall()
    return render_template("in_test.html", testing=rows)

