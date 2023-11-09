from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_mysqldb import MySQL
import MySQLdb.cursors

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
if __name__ == '__main__':
    app.run()