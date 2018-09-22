import DB
import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
from random import *



root = Tk()
root.title("The safer")

root.configure(bg='black')

photo = PhotoImage(file = 'logo.png')
img = Label(root , image = photo , bg = "black")
img.photo = photo
####################### Sign up part #####################

un = Entry(root , width = '30')
un1 = Entry(root , width = '30')
up = Entry(root , width = '30' , show = '*')
up1 = Entry(root , width = '30', show = '*')

user = Label(root , text = "new username :" , fg = 'white' , bg ="black")
user1 = Label(root , text = "repeat new username :", fg = 'white' , bg ="black" )
passs = Label(root , text = "new password :", fg = 'white' , bg ="black")
passs1 = Label(root , text = "repeat new password :", fg = 'white' , bg ="black")

sign_uplabel = Label(root , text = ' Sign-up ' , fg = 'gray' , bg = "black")
sign_uplabel.config(width = 14 , font = ('times',20,'bold'))

img.grid(row = 1 , column = 1 ,columnspan = 2, padx = 20 )
sign_uplabel.grid(row = 2 , column = 1 , padx = 20 , pady = 20)
user.grid(row = 3 , column = 1 , padx = 20 )
un.grid(row =4 , column = 1, padx =20  )
user1.grid(row = 5 , column = 1 , padx = 20  )
un1.grid(row = 6 , column = 1 , padx = 20 )
passs.grid(row = 7 , column = 1 , padx = 20  )
up.grid(row = 8 , column = 1 , padx = 20 )
passs1.grid(row = 9 , column = 1, padx = 20  )
up1.grid(row = 10 , column = 1 , padx = 20  )


un_log = Entry(root , width = '30')
pass_log = Entry(root , width = '30' , show = '*')
userlog = Label(root , text = " username :", fg = 'white' , bg ="black")
passlog = Label(root , text = " password :", fg = 'white' , bg ="black")

login_label = Label(root , text = ' Log-in ' , fg = 'gray' , bg = "black")
login_label.config(width = 14 , font = ('times',20,'bold'))


login_label.grid(row = 2 , column = 2 , padx = 20 , pady = 20)
userlog.grid(row = 5 , column = 2 , padx = 20 )
un_log.grid(row = 6 , column = 2 , padx = 20 )
passlog.grid(row = 7 , column = 2 , padx = 20 )
pass_log.grid(row = 8 , column = 2 , padx = 20 )
trademark = Label(root , text = 'Created by  Khalil Preview @ Open-Source Softwer ' , fg='white' , bg = 'gray'  )
trademark.grid(row = 12, column = 1,columnspan = 2, padx = 20 )
#################fast db for the welcome ##################


########### sign up verification #############"############
def signupverif():
    if len(un.get()) and len(up.get()) > 4 :
        if un1.get() == un.get() and up1.get() == up.get():
            result = []
            username = str(un.get()).lower()
            userpass = str(up.get()).lower()
            result.append(username)
            result.append(userpass)
            f = open(str(username + '.sfr'), 'w')
            f.write(str(result))
            f.close()
            bd = DB.c_table(username + '.db')
            bd.create_table()
            messagebox.showinfo("Sign up Successful", "open the safer and login now !")
            root.destroy()
        else :
            messagebox.showerror("Sign up Failed", "Usernam or Password not much  !!!")
    else :
        messagebox.showerror("Sign up Failed", "Usernam or Password short than 4 character !!!")


sigupbtn = Button (root , text='Sign up'  , command = signupverif ,fg = "#e63232" , bg = "black")
sigupbtn.grid(row = 11 , column = 1 , pady = 20)
###########################################################

################### Login verification ####################
def loginverif():
    un = str(un_log.get()).lower()
    up = str(pass_log.get()).lower()
    ############ db get ############
    welcome = 'welcome '
    rand = randrange(0, 10000000000)
    conn = sqlite3.connect('memory.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS db (
                       id INTEGERPRIMARY KEY ,
                       name TEXT  )''')
    cursor.execute(''' INSERT INTO db VALUES (?,?);''', (rand, un))

    conn.commit()
    conn.close()
    ##################################
    list0 = str([un, up])
    list = open(str(un + ".sfr")).readlines()
    for i in list:
        if i == list0:
            root.destroy()
            thesaferhome()

        else :

            messagebox.showerror("Login Failed", "Usernam or Password wrong !!!")
################logout def ###################


def thesaferhome():
    root = Tk()
    root.title("The safer")


    root.minsize(315, 480)
    root.configure(bg='black')
    ############ db get ############
    conn = sqlite3.connect('memory.db')
    cursor = conn.cursor()
    k = cursor.execute('''SELECT name FROM db''')
    for raw in k:
        welc = raw[0]
        welmsg = 'welcome ' + welc
        wel = Label(root, text=welmsg, fg = "white", bg='#514d4d')
        wel.config(width = 18 , font = ('times',12,'bold'))
        wel.grid(row=1, column=1, columnspan=5, pady=5)
    conn.commit()
    conn.close()

    def logout():
        conn = sqlite3.connect('memory.db')
        cursor = conn.cursor()
        cursor.execute('''DROP TABLE db;''')
        conn.commit()
        conn.close()
        root.destroy()

    def adding_compte():

            compte = str(input('account name > '))
            email = str(input('Email > '))
            password = str(input('Password >'))

            conn = sqlite3.connect('memory.db')
            cursor = conn.cursor()
            k = cursor.execute('''SELECT name FROM db''')
            for raw in k:
                welc = raw[0]
                welmsg = welc + '.db'
                db = DB.a_table(welmsg, compte, email, password)
                db.add_to_table()

                break



    def show_compte():
        conn = sqlite3.connect('memory.db')
        cursor = conn.cursor()
        k = cursor.execute('''SELECT name FROM db''')
        for raw in k:
            welc = raw[0]
            welmsg = welc + '.db'
            db = DB.s_table(welmsg)
            a = db.show_table()
            return

    def delete_account():

            account = str(input('acount you want to delete it > '))
            conn = sqlite3.connect('memory.db')
            cursor = conn.cursor()
            k = cursor.execute('''SELECT name FROM db''')
            for raw in k:
                welc = raw[0]
                welmsg = welc + '.db'
                db = DB.d_table(welmsg, account)
                db.delete_user()

                break



    def update_account():
        search_up = str(input('Put account you want to update it > '))


        conn = sqlite3.connect('memory.db')
        cursor = conn.cursor()
        k = cursor.execute('''SELECT name FROM db''')
        for raw in k:
                welc = raw[0]
                welmsg = welc + '.db'
                onn = sqlite3.connect()
                cursor = conn.cursor()
                idd = search_up
                a = cursor.execute('''SELECT id = ? FROM  DB''', (idd))
                conn.commit()
                conn.close()
                return a












    photo = PhotoImage(file='logo.png')
    img = Label(root, image=photo ,bg = "black" )
    img.photo = photo

    photo1 = PhotoImage(file='acount.png')
    img1 = Button (root, image=photo1 ,bg = "black" , bd=0 , command = show_compte )
    img1.photo1 = photo
    photo2 = PhotoImage(file='add.png')
    img2 = Button (root, image=photo2 , bg = "black" , bd=0 , command = adding_compte )
    img2.photo2 = photo
    photo3 = PhotoImage(file='delete.png')
    img3 = Button (root, image=photo3 , bg = "black" , bd=0 , command = delete_account)
    img3.photo3 = photo
    #photo4 = PhotoImage(file='update.png')
    #img4 = Button (root, image=photo4  , bg = "black" , bd=0 , command = update_account)
    #img4.photo4 = photo
    photo5 = PhotoImage(file='logout.png')
    img5 = Button(root, image=photo5, bg="black", bd=0 , command = logout)
    img5.photo5 = photo
    tex1 = Button(root , text = 'my account' , fg ='white' , bg = 'gray' , bd = 0 , command = show_compte)
    tex2 = Button (root , text = 'add new account' ,fg ='white' , bg = 'gray' , bd = 0 , command = adding_compte)
    tex3 = Button (root , text = 'delete account' ,fg ='white' , bg = 'gray' , bd = 0 , command = delete_account)
    #tex4 = Button (root , text = 'update account' , fg ='white' , bg = 'gray' ,bd = 0  )

    img.grid(row = 2 , column = 1 ,columnspan = 4, padx = 20 )
    img1.grid(row = 3 , column = 2 ,padx = 10)
    img2.grid(row=3, column=3 , padx = 10)
    img3.grid(row=3, column=4 , padx = 10)
    #img4.grid(row=3, column=5 , padx = 10)
    img5.grid(row = 1 , column=4, columnspan=4, padx=5)
    tex1.grid(row=4, column=2 , padx = 10)
    tex2.grid(row=4, column=3 , padx = 10)
    tex3.grid(row=4, column=4 , padx = 10)
    #tex4.grid(row=4, column=5 , padx = 10)

    trademark = Label(root, text='Created by  Khalil Preview @ Open-Source Softwer ', fg='white', bg='gray')
    trademark.grid(row=5, column=2, columnspan=4, padx=20 , pady=200)

    root.mainloop()

connectionbtn = Button (root , text='Connect' , command = loginverif ,fg = "#e63232" , bg = "black")
connectionbtn.grid(row = 11 , column = 2 , pady = 20)
############################################################





root.mainloop()
