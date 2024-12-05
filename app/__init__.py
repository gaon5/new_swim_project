
from flask import Flask, url_for, request, redirect, render_template, session
from datetime import date, datetime, timedelta
import mysql.connector
from app import config
import math
# import bcrypt
import re

app = Flask(__name__)
app.config.from_object(config)
app.config['PERMANENT_SESSION_LIFETIME'] = 86400
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
                                         ssl_ca=config.SSL_CA_PATH,  
                                         autocommit=True)
    db_conn = connection.cursor()
    return db_conn


first_select = get_cursor()
first_select.execute("""SELECT * FROM `region`;""")
region_list = first_select.fetchall()
first_select.execute("""SELECT * FROM `title`;""")
title_list = first_select.fetchall()
first_select.execute("""SELECT * FROM `city`;""")
city_list = first_select.fetchall()
first_select.close()


def check_permissions():
    is_member = session['is_member']
    is_instructor = session['is_instructor']
    is_admin = session['is_admin']
    is_root = session['is_root']
    if is_root == 1:
        return 4
    elif is_admin == 1:
        return 3
    elif is_instructor == 1:
        return 2
    elif is_member == 1:
        return 1
    else:
        return 0


from app import admin, member, instructor, root, guest