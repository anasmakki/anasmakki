from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "newdatabase.db"))


app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class Teacher(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    father_name = db.Column(db.String())
    address = db.Column(db.String())
    gender = db.Column(db.String())
    state = db.Column(db.String())
    city = db.Column(db.String())
    birth_date = db.Column(db.String())
    pincode = db.Column(db.Integer())
    course = db.Column(db.String())
    email = db.Column(db.String())

#db.create_all()



class Student(db.Model):
    new_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    father_name = db.Column(db.String())
    address = db.Column(db.String())
    gender = db.Column(db.String())
    state = db.Column(db.String())
    city = db.Column(db.String())
    birth_date = db.Column(db.String())
    pincode = db.Column(db.Integer())
    course = db.Column(db.String())
    email = db.Column(db.String())

#db.create_all()


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/teacher', methods = ['GET', 'POST'])
def teacher():
    if (request.method == 'POST'):
        name = request.form.get('name')
        father_name = request.form.get('father_name')
        address = request.form.get('address')
        gender = request.form.get('gender')
        state = request.form.get('state')
        city = request.form.get('city')
        birth_date = request.form.get('birth_date')
        pincode = request.form.get('pincode')
        course = request.form.get('course')
        email = request.form.get('email')
        entry = Teacher(name=name, father_name=father_name, address=address, gender=gender, state=state, city=city,
                        birth_date=birth_date, pincode=pincode, course=course, email=email)
        db.session.add(entry)
        db.session.commit()

        return ("<h1>Data has been saved in database successfully</h1>")

    return render_template('teacher.html')



@app.route('/student', methods = ['GET', 'POST'])
def student():
    if (request.method == 'POST'):
        name = request.form.get('name')
        father_name = request.form.get('father_name')
        address = request.form.get('address')
        gender = request.form.get('gender')
        state = request.form.get('state')
        city = request.form.get('city')
        birth_date = request.form.get('birth_date')
        pincode = request.form.get('pincode')
        course = request.form.get('course')
        email = request.form.get('email')
        std_entry = Student(name=name, father_name=father_name, address=address, gender=gender, state=state, city=city,
                        birth_date=birth_date, pincode=pincode, course=course, email=email)
        db.session.add(std_entry)
        db.session.commit()

        return ("<h1>Data has been saved in database successfully</h1>")

    return render_template('student.html')


app.run(debug=True)
