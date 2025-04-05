from flask import Flask, render_template, request, url_for, flash, redirect
# from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.secret_key = 'many random bytes'

# MySQL Connection
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='1234',
    db='crud',
    charset='utf8'
)

@app.route('/')
def Index():
    curs = conn.cursor()
    # SQL문 실행
    sql = 'select * from students'
    curs.execute(sql)
    #data fetch
    data = curs.fetchall()
    curs.close()
    
    return render_template('index.html', students = data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        flash('Data Inserted Successfully')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        curs = conn.cursor()
        curs.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash('Record Has Been Successfully')
    curs = conn.cursor()
    curs.execute("DELETE FROM students WHERE id=%s", (id_data))
    conn.commit()
    return redirect(url_for('Index'))

@app.route('/update', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        curs = conn.cursor()
        curs.execute('''
        UPDATE students SET name=%s, email=%s, phone=%s
        WHERE id=%s
        ''', (name, email, phone, id_data))
        flash("Data Updated Successfully")
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug = True)