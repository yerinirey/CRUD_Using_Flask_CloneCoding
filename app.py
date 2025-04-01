from flask import Flask, render_template, request, url_for, flash
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

if __name__ == "__main__":
    app.run(debug = True)