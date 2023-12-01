from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_mysqldb import MySQL
import MySQLdb.cursors
import random

app = Flask(__name__)
CORS(app)
app.secret_key = 'xyzsdfg'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 's350f_groupproject_gp50'

mysql = MySQL(app)

@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        LoginID = data.get('loginID')
        print(f"Received LoginID: {LoginID}")
        password = data.get('password')
        print(f"Received Password: {password}")
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM useraccount WHERE LoginID = %s AND password = %s', (LoginID, password))
        user = cursor.fetchone()
        if user:
            # Check the userrole and return the corresponding redirect URL
            if user['UserRole'] == 'student':
                return jsonify({'success': True, 'redirectUrl': '/student-home','Name': user['Name']})
            elif user['UserRole'] == 'Admin':
                return jsonify({'success': True, 'redirectUrl': '/admin-home','Name': user['Name']})
            elif user['UserRole'] == 'teacher':
                return jsonify({'success': True, 'redirectUrl': '/teacher-home','Name': user['Name']})
            else:
                return jsonify({'success': False, 'message': 'Invalid user role!'})
        else:
            message = 'Please enter correct LoginID or password!'
            return jsonify({'success': False, 'message': message})
    else:
        return 'Method Not Allowed'
    
@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True, 'message': 'Logout successful'})

@app.route('/api/students', methods=['GET'])
def get_students():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM studentrecords')
    students = cursor.fetchall()
    return jsonify(students)

@app.route('/api/teachers', methods=['GET'])
def get_teachers():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM teacherrecords')
    teachers = cursor.fetchall()
    return jsonify(teachers)

@app.route('/api/classes', methods=['GET'])
def get_classes():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM ClassSchedule')
    classes = cursor.fetchall()
    return jsonify(classes)

@app.route('/api/students/count', methods=['GET'])
def get_total_students():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT COUNT(*) as total_students FROM useraccount WHERE UserRole = "student"')
    result = cursor.fetchone()
    if result:
        total_students = result['total_students']
        return jsonify({'total_students': total_students})
    else:
        return jsonify({'total_students': 0})
    
@app.route('/api/teachers/count', methods=['GET'])
def get_total_teachers():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT COUNT(*) as total_teachers FROM useraccount WHERE UserRole = "teacher"')
    result = cursor.fetchone()
    if result:
        total_teachers = result['total_teachers']
        return jsonify({'total_teachers': total_teachers})
    else:
        return jsonify({'total_teachers': 0})   
    
@app.route('/api/Addteachers', methods=['POST'])
def add_teacher():
    data = request.get_json()
    name = data.get('name')
    dateOfEmployment = data.get('dateOfEmployment')
    phoneNumber = data.get('phoneNumber')
    department = data.get('department')
    email = data.get('email')
    designation = data.get('designation')
    gender = data.get('gender')
    stringdate= dateOfEmployment.replace("-","")
    teacher_id = f"{name}{stringdate}"
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO teacherrecords (TeacherID, Name, EmploymentDate, PhoneNumber, Department, Email, Designation, Gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                   (teacher_id, name, dateOfEmployment, phoneNumber, department, email, designation, gender))
    mysql.connection.commit()
    cursor.execute('INSERT INTO useraccount (LoginID, password, Name, UserRole) VALUES (%s, %s, %s, %s)',
                   (teacher_id,"123123", name, "teacher"))
    mysql.connection.commit()
    return jsonify({'success': True, 'message': 'Teacher added successfully'})

@app.route('/api/AddStudents', methods=['POST'])
def add_student():
    student_ids = []
    for _ in range(8):
        student_id = random.randint(10000000, 99999999)
    student_ids.append(student_id)
    data = request.get_json()
    name = data.get('Name')
    BirthDate = data.get('BirthDate')
    phoneNumber = data.get('phoneNumber')
    Status = data.get('Status')
    emails = []
    for student_id in student_ids:
        email = "s" + str(student_id)[:7] + "@live.hkmu.edu.hk"
        emails.append(email)
    Major = data.get('Major')
    gender = data.get('Gender')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO studentrecords (StudentID, Name, StudentEmail, Gender, BirthDate, PhoneNumber, Status, Major) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                   (student_ids, name, emails, gender, BirthDate, phoneNumber, Status, Major))
    mysql.connection.commit()
    cursor.execute('INSERT INTO useraccount (LoginID, password, Name, UserRole) VALUES (%s, %s, %s, %s)',
                   (student_ids,"123123", name, "student"))
    mysql.connection.commit()
    return jsonify({'success': True, 'message': 'Teacher added successfully'})


@app.route('/api/teachers/<teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM teacherrecords WHERE TeacherID = %s', (teacher_id,))
    mysql.connection.commit()
    cursor.execute('DELETE FROM useraccount WHERE LoginID = %s', (teacher_id,))
    mysql.connection.commit()
    return jsonify({'success': True, 'message': 'Teacher deleted successfully'})

@app.route('/api/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM studentrecords WHERE StudentID = %s', (student_id,))
    mysql.connection.commit()
    cursor.execute('DELETE FROM useraccount WHERE LoginID = %s', (student_id,))
    mysql.connection.commit()
    return jsonify({'success': True, 'message': 'Teacher deleted successfully'})

@app.route('/api/AddClass', methods=['POST'])
def add_Class():
    data = request.get_json()
    CourseName = data.get('CourseName')
    ClassDate = data.get('ClassDate')
    ClassType = data.get('ClassType')
    Venue = data.get('Venue')
    StartTime = data.get('StartTime')
    EndTime = data.get('EndTime')
    InstructorName = data.get('InstructorName')
    ClassID = f"{CourseName}-{ClassDate}-{StartTime}"
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO ClassSchedule (ClassID, CourseName, ClassType, ClassDate, StartTime, EndTime, Venue, InstructorName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                   (ClassID, CourseName, ClassType,  ClassDate,StartTime, EndTime, Venue, InstructorName))
    mysql.connection.commit()
    cursor.execute('INSERT INTO AttendanceRecords (ClassID, StudentID, Date, Status, Remarks) SELECT %s, StudentID, %s, NULL, NULL FROM studentrecords WHERE Major IN (SELECT Department FROM teacherrecords WHERE Name = %s)',
               (ClassID, ClassDate, InstructorName))
    mysql.connection.commit()
    return jsonify({'success': True, 'message': 'added successfully'})


@app.route('/api/EditGrade', methods=['POST'])
def edit_student():
    data = request.get_json()
    Grade = data.get('Grade')
    
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("UPDATE studentrecords SET Grade = %s ;", (Grade,))
    mysql.connection.commit()
    
    return jsonify({'success': True, 'message': 'Edited successfully'})






if __name__ == '__main__':
    app.run()