from flask import Flask , render_template ,request , redirect , flash ,url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = "sharif"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    grade = db.Column(db.String(100))

    def __init__(self, name, email, grade):
        self.name = name
        self.email = email
        self.grade = grade


@app.route('/')
def index():
    all_data = Data.query.all()
    return render_template('index.html' , students = all_data)



@app.route('/insert' , methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        grade = request.form['grade']
    
    my_data = Data(name, email, grade)

    db.session.add(my_data)
    db.session.commit()

    flash("added Student successfully") 


    return redirect(url_for('index'))



@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        student_id = request.form.get('student_id')  # Corrected to match the form field name

        # Fetch the data from the database using the correct ID
        my_data = Data.query.get(student_id)

        # Update the fields
        my_data.name = request.form['student_name']
        my_data.email = request.form['student_email']
        my_data.grade = request.form['grade']

        # Commit the changes to the database
        db.session.commit()

        # Flash a success message
        flash("Updated Student successfully")

        # Redirect to the index page
        return redirect(url_for('index'))

                                     
        

@app.route('/delete/<id>' , methods=['GET', 'POST'])
def delete():
    my_data = Data.QUE


if __name__ == '__main__':
    app.run(debug=True)