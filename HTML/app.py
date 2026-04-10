from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from urllib.parse import quote_plus
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

#EMAIL : SMBANK@GMAIL.COM
password = "SHRI@2005"  
encoded_password = quote_plus(password)
app.config['MONGO_URI'] = f'mongodb+srv://SHRI:{encoded_password}@web.hmirxrb.mongodb.net/edu_portal?retryWrites=true&w=majority&appName=WEB'

mongo = PyMongo(app)

################################### MAIN PAGE #################################################### 

@app.route('/')
def home_page():
    return render_template('home-page.html')

@app.route('/professor-login')
def professor_login():
    return render_template('PROF_SEC/FacLogin.html') 

@app.route('/contact')
def contact():
    return render_template('STUDENT_SEC/help&supp.html') 

###################################STUDENT SECTION###########################################

@app.route('/student-register', methods=['GET', 'POST'])
def student_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        
        if mongo.db.students.find_one({'username': username}):
            flash('Username already exists! Please choose another.', 'error')
        else:
            
            mongo.db.students.insert_one({
                'username': username,
                'password': password,
                'email': email,
                'created_at': datetime.now()
            })
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('student_login'))
    
    return render_template('STUDENT_SEC/stu-register.html')

@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        student = mongo.db.students.find_one({
            'username': username,
            'password': password
        })
        
        if student:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('student_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('STUDENT_SEC/StudLogin.html')

@app.route('/student-dashboard')
def student_dashboard():
    username = session.get('username', 'Student')
    return render_template('STUDENT_SEC/Studash.html', username=username)

@app.route('/communicate')
def communicate():
    return render_template('STUDENT_SEC/Communicate.html')

@app.route('/cor')
def cor():
    return render_template('STUDENT_SEC/Courses.html')

@app.route('/grades')
def grade():
    return render_template('STUDENT_SEC/Grades.html')

@app.route('/AN')
def AN():
    return render_template('STUDENT_SEC/AN.html')

@app.route('/event')
def event():
    return render_template('STUDENT_SEC/events.html')

@app.route('/attendance')
def attendance():
    return render_template('STUDENT_SEC/attendance.html')

@app.route('/aca')
def aca():
    return render_template('STUDENT_SEC/Academic.html')

################################################################################################################################################
#PROFESSOR SECTION

@app.route('/prof_register', methods=['GET', 'POST'])
def prof_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        
        if mongo.db.professors.find_one({'username': username}):
            flash('Professor username already exists!', 'error')
        else:
            
            mongo.db.professors.insert_one({
                'username': username,
                'password': password,
                'email': email,
                'created_at': datetime.now()
            })
            flash('Professor registration successful! Please login.', 'success')
            return redirect(url_for('prof_login'))
    
    return render_template('PROF_SEC/prof-register.html')

@app.route('/prof_login', methods=['GET', 'POST'])
def prof_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
    
        professor = mongo.db.professors.find_one({
            'username': username,
            'password': password
        })
        
        if professor:
            session['prof_username'] = username
            session['user_type'] = 'professor'
            flash('Professor login successful!', 'success')
            return redirect(url_for('prof_dashboard'))
        else:
            flash('Invalid professor credentials', 'error')
    
    return render_template('PROF_SEC/FacLogin.html')

@app.route('/prof-dashboard')
def prof_dashboard():
    username = session.get('prof_username', 'Professor')
    return render_template('PROF_SEC/profDASH.html', username=username)

@app.route('/logout')
def logout():
    return render_template('home-page.html')

@app.route('/technical')
def technical():
    return render_template('STUDENT_SEC/help&supp.html')





if __name__ == '__main__':
    app.run(debug=True)