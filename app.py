from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_mysqldb import MySQL
import MySQLdb.cursors
import random
import json

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
                response_data = {
                    'success': True,
                    'userData': {
                        'LoginID': user['LoginID'],
                        'UserRole': user['UserRole'],
                        'Name': user['Name']
                    },
                    'redirectUrl': '',
                    'message': ''
                }
                # Check the userrole and return the corresponding redirect URL
                if user['UserRole'] == 'student':
                    response_data['redirectUrl'] = '/student-home'
                elif user['UserRole'] == 'Admin':
                    response_data['redirectUrl'] = '/admin-home'
                elif user['UserRole'] == 'teacher':
                    response_data['redirectUrl'] = '/teacher-home'
                else:
                    return jsonify({'success': False, 'message': 'Invalid user role!'})
                
                return jsonify(response_data)
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
        for class_data in classes:
            class_data['classid'] = f"{class_data['CourseName']}-{class_data['ClassDate']}-{class_data['StartTime']}"
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
    data = request.get_json()
    name = data.get('Name')
    BirthDate = data.get('BirthDate')
    phoneNumber = data.get('phoneNumber')
    Status = data.get('Status')
    Major = data.get('Major')
    gender = data.get('Gender')
    if Major == 'Computer Science':
        grade_data = [
            {"CourseName": "S312FJavaApplication", "Grade": "N/A"},
            {"CourseName": "S320FDataBaseManagement", "Grade": "N/A"},
            {"CourseName": "S350FSoftwareEngineering", "Grade": "N/A"},
            {"CourseName": "S381FServer-Side", "Grade": "N/A"}
        ]
    else:
        grade_data = []
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    student_id = random.randint(10000000, 99999999)
    email = "s" + str(student_id)[:7] + "@live.hkmu.edu.hk"
    cursor.execute('INSERT INTO studentrecords (StudentID, Name, StudentEmail, Gender, BirthDate, PhoneNumber, Status, Major, Grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                   (student_id, name, email, gender, BirthDate, phoneNumber, Status, Major, json.dumps(grade_data)))
    mysql.connection.commit()
    cursor.execute('INSERT INTO useraccount (LoginID, password, Name, UserRole) VALUES (%s, %s, %s, %s)',
                   (student_id, "123123", name, "student"))
    mysql.connection.commit()

    return jsonify({'success': True, 'message': 'Student added successfully'})

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
@app.route('/api/updateGrade/<student_id>', methods=['PUT'])
def update_grade(student_id):
    if request.method == 'PUT':
        data = request.get_json()
        course_name = data['coursename']
        grade_value = data['grade']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT Grade FROM studentrecords WHERE StudentID = %s', (student_id,))
        result = cursor.fetchone()
        existing_grades = json.loads(result['Grade']) if result and 'Grade' in result else []
        for grade in existing_grades:
            if grade.get('CourseName') == course_name:
                grade['Grade'] = grade_value
                break
        cursor.execute('UPDATE studentrecords SET Grade = %s WHERE StudentID = %s', (json.dumps(existing_grades), student_id))
        mysql.connection.commit()

        return jsonify({'success': True, 'message': 'Grade updated successfully'})
    else:
        return 'Method Not Allowed'
    
@app.route('/api/user-profile', methods=['POST'])
def get_user_profile():
        data = request.get_json()
        loginID = data.get('loginID')
        UserRole = data.get('UserRole')
        if UserRole == 'student':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM studentrecords WHERE StudentID = %s',(loginID,))
            result = cursor.fetchone()
            result['Grade'] = json.loads(result['Grade'])
        elif UserRole == 'teacher':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM teacherrecords WHERE TeacherID = %s',(loginID,))
            result = cursor.fetchone()
        print(result)
        return jsonify(result)

@app.route('/api/students/update-profile', methods=['POST'])
def update_student_profile():
        data = request.get_json()
        student_id = data.get('StudentID')
        name = data.get('Name')
        email = data.get('StudentEmail')
        gender = data.get('Gender')
        birth_date = data.get('BirthDate')
        phone_number = data.get('PhoneNumber')
        status = data.get('Status')
        major = data.get('Major')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE studentrecords SET Name = %s, StudentEmail = %s, Gender = %s, BirthDate = %s, PhoneNumber = %s, Status = %s, Major = %s WHERE StudentID = %s',
                   (name, email, gender, birth_date, phone_number, status, major, student_id))
        mysql.connection.commit()
        cursor.execute('UPDATE useraccount SET Name = %s WHERE LoginID = %s',
                   (name, student_id))
        mysql.connection.commit()
        return jsonify({'success': True, 'message': 'Profile updated successfully'})

@app.route('/api/teachers/update-profile', methods=['POST'])
def update_teacher_profile():
        data = request.get_json()
        teacher_id = data.get('TeacherID')
        name = data.get('Name')
        email = data.get('Email')
        gender = data.get('Gender')
        employment_date = data.get('EmploymentDate')
        phone_number = data.get('PhoneNumber')
        department = data.get('Department')
        designation = data.get('Designation')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE teacherrecords SET Name = %s, Email = %s, Gender = %s, EmploymentDate = %s, PhoneNumber = %s, Department = %s, Designation = %s WHERE TeacherID = %s',
                   (name, email, gender, employment_date, phone_number, department, designation, teacher_id))
        cursor.execute('UPDATE useraccount SET Name = %s WHERE LoginID = %s',
                   (name, teacher_id))
        mysql.connection.commit()
        return jsonify({'success': True, 'message': 'Profile updated successfully'})

@app.route('/api/classes/<class_id>', methods=['GET'])
def get_class_details(class_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM ClassSchedule WHERE ClassID = %s', (class_id,))
    class_data = cursor.fetchone()
    return jsonify(class_data)
    data = request.get_json()
    Grade = data.get('Grade')
    StudentID = data.get('StudentID')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("UPDATE studentrecords SET Grade = %s  WHERE StudentID = %s ;", (Grade,StudentID ))
    mysql.connection.commit()
    
    return jsonify({'success': True, 'message': 'Edited successfully'})


@app.route('/api/attendance/<student_id>', methods =['GET'])
def get_class_id(student_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT ClassID FROM AttendanceRecords WHERE StudentID = %s', (student_id,))
    class_data = cursor.fetchall()
    return jsonify(class_data)


@app.route('/api/student-details/<student_id>', methods =['GET'])
def get_student_details(student_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM studentrecords WHERE StudentID = %s', (student_id,))
    student_data = cursor.fetchone()
    student_data['Grade'] = json.loads(student_data['Grade'])
    return jsonify(student_data)

@app.route('/api/classes/<class_id>/students', methods=['GET'])
def get_class_students(class_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT AttendanceRecords.*, studentrecords.Name FROM AttendanceRecords JOIN studentrecords ON AttendanceRecords.StudentID = studentrecords.StudentID WHERE AttendanceRecords.ClassID = %s', (class_id,))
    students = cursor.fetchall()
    return jsonify(students)

@app.route('/api/attendance/<class_id>/<student_id>', methods=['PUT'])
def update_student_attendance(class_id, student_id):
    if request.method == 'PUT':
        data = request.get_json()
        new_status = data.get('Status')
        new_remarks = data.get('Remarks') 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE AttendanceRecords SET Status = %s, Remarks = %s WHERE ClassID = %s AND StudentID = %s', (new_status, new_remarks, class_id, student_id))
        mysql.connection.commit()

        return jsonify({'success': True, 'message': 'Student attendance updated successfully'})
    else:
        return 'Method Not Allowed'
    
@app.route('/api/attendance/<student_id>/<class_id>', methods=['GET'])
def get_attendance_status_remark(student_id, class_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT Status, Remarks FROM AttendanceRecords WHERE StudentID = %s AND ClassID = %s', (student_id, class_id))
    attendance_data = cursor.fetchone()
    return jsonify(attendance_data)

if __name__ == '__main__':
        app.run()