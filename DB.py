#############################################
# DB.py for sqlite3 create db easly         #
# ho to use it :                            #
#############################################
# import db     //to create table           #
# db = db.c_table('name of db.db')          #
# bd.create_table()                         #
#                      //to add to table    #
#db = db.a_table('name of table' + )        #
#db.add_to_table()                          #
#############################################
#         created by khalil preview         #
#############################################

import sqlite3

class c_table(object):
    def __init__(self , table):
        self.table = table

    def create_table(self):
        db = str(self.table)
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS db (
                  id TEXT  ,
                  email TEXT ,
                  password TEXT               )''')

class a_table(object):
    def __init__(self , table , id , email , password):
        self.table = table
        self.id = id
        self.email = email
        self.password = password

    def add_to_table(self):
        conn = sqlite3.connect(self.table)
        cursor = conn.cursor()

        cursor.execute(''' INSERT INTO db VALUES (?,?,?);''',(self.id , self.email , self.password))
        conn.commit()
        conn.close()

class d_table(object):
    def __init__(self , table , dell ):
        self.table = table
        self.dell = dell

    def delete_user(self):
        conn = sqlite3.connect(self.table)
        cursor = conn.cursor()
        delete = self.dell
        cursor.execute('''DELETE FROM db WHERE id = '%s';''' %delete.strip())
        conn.commit()
        conn.close()

class u_userid(object):
    def __init__(self , table , userid , uuserid): #userid argument c le nom changé
        self.table = table
        self.userid = userid
        self.uuserid = uuserid

    def update_userid(self):
        conn = sqlite3.connect(self.table)
        cursor = conn.cursor()
        idd = self.userid
        iddd = self.uuserid
        cursor.execute('''UPDATE db SET id = ? WHERE id = ?''', (idd , iddd))
        conn.commit()
        conn.close()

class u_useremail(object):
    def __init__(self , table , useremail , uuseremail):
        self.table = table
        self.useremail = useremail
        self.uuseremail = uuseremail

    def update_useremail(self):
        conn = sqlite3.connect(self.table)
        cursor = conn.cursor()
        idd = self.useremail
        iddd = self.uuseremail
        cursor.execute('''UPDATE db SET email = ? WHERE email = ?''', (idd, iddd))
        conn.commit()
        conn.close()

class u_userpass(object):
    def __init__(self , table , userpass , uuserpass):
        self.table = table
        self.userpass = userpass
        self.uuserpass = uuserpass

    def update_userpass(self):
        conn = sqlite3.connect(self.table)
        cursor = conn.cursor()
        idd = self.userpass
        iddd = self.uuserpass
        cursor.execute('''UPDATE db SET password = ? WHERE password = ?''', (idd, iddd))
        conn.commit()
        conn.close()

class s_table(object):
    def __init__(self , table ):
        self.table = table

    def show_table(self):
        conn = sqlite3.connect(self.table)
        cursor = conn.cursor()
        tab = cursor.execute('''SELECT * FROM db''')
        for raw in tab :
            print (raw)
        conn.commit()
        conn.close()

