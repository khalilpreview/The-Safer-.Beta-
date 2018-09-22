##############################
# import Verif               #
# var = Verif.class(object)  #
# var.def()                  #
##############################
# this lib it's verification #
# maked by khalil preview    #
##############################

import tkinter
from tkinter import *
from tkinter import messagebox




class sign_in(object):
    def __init__(self , un , up ,un1 , up1) :
        self.un = un
        self.up = up
        self.un1 = un1
        self.up1 = up1

    def sign_in_verif(self):
        if self.un1 == self.un  and self.up1 == self.up :
            result = []
            username = str(self.un1)
            userpass = str(self.up1)
            result.append(username)
            result.append(userpass)
            f = open(str(username + '.sfr'), 'w')
            f.write(str(result))
            f.close()

        else :
            messagebox.showinfo("Sign up Failed", "Usernam or Password wrong !!!")



