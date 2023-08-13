from flask import Flask, url_for, request, redirect, render_template, session
from datetime import datetime
import mysql.connector
import config
import math
import bcrypt

# When you gonna start, pip install -r requirements.txt

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = 'aHn6Zb7MstRxC8vEoF2zG3B9wQjKl5YD'


db_conn = None
connection = None


def get_cursor():
    global db_conn
    global connection
    connection = mysql.connector.connect(user=config.dbuser,
                                         password=config.dbpass,
                                         host=config.dbhost,
                                         database=config.dbname,
                                         autocommit=True)
    db_conn = connection.cursor()
    return db_conn


@app.route('/', methods=['GET', 'POST'])
def welcome():
    sample_value = 1
    sql_data = get_cursor()
    sql = """SELECT * FROM sample_database WHERE sample_id=%s;"""
    sql_value = (sample_value,)
    sql_data.execute(sql, sql_value)
    sample_list = sql_data.fetchall()
    sql_data.close()
    return render_template('welcome_page.html', sample_list=sample_list)

@app.route('/admin')
def admin():
    return render_template('admin_dashboard.html')

@app.route('/member')
def member():
    return render_template('member_dashboard.html')

@app.route('/instructor')
def instructor():
    return render_template('instructor_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

