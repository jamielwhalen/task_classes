import os
import tkinter as tk
from tkinter import *
import sqlite3
import subprocess
import webbrowser
import tkinter.messagebox

import sys

global op_sys





conn1 = sqlite3.connect('Users.db')
c1 = conn1.cursor()

ct_tbl = ('CREATE TABLE IF NOT EXISTS users (username Text, password Text)')
ct_tbl = str(ct_tbl)
c1.execute(ct_tbl)

class Controller():
    def login(username, password, window):
        warning = Tk()
        warning.withdraw()

        name = username.get()
        pw = password.get()

        error = 'Y'
        c1.execute('SELECT * FROM users')
        table = c1.fetchall()
        for row in table:
            if row[0] == name:
                if row[1] == pw:
                    error = 'N'

        if error == 'Y':
            warning.bell()
            tkinter.messagebox.showerror("Error",
                                         "Username or password do not match.")
        else:
            conn1.close()
            a = (name +'.db')
            conn = sqlite3.connect(a)
            c = conn.cursor()

            go home

    def verify_username(name, pwd, window):
        warning = Tk()
        warning.withdraw()

        error = 'N'
        c1.execute('SELECT * FROM users')
        table = c1.fetchall()
        for row in table:
            print(row)
            if row[0] != name:
                pass
            else:
                error = 'Y'
        if error == 'N':
            add1 = ("INSERT INTO users VALUES('" + name + "','" + pwd + "')")
            c1.execute(str(add1))
            conn1.commit()

            window.destroy()
            page3 = Tk()
            Views.login(page3)


        else:
            warning.bell()
            tkinter.messagebox.showerror("Error",
                                         "Username already exists.")

            return



    def create_user(username, password, verify, window):

        warning = Tk()
        warning.withdraw()

        name = username.get()
        pw = password.get()
        pw2 = verify.get()

        if pw == pw2:
            print(username.get())
            print(password.get())
            print(verify.get())


            Controller.verify_username(name, pw, window)

        else:
            warning.bell()
            tkinter.messagebox.showerror("Error",
                                           "Passwords do not match.")





    def sign_up_page(window):
        window.destroy()
        page2 = Tk()
        Views.sign_up(page2)



class Views():
    def login(root):

        root.title("Job Manager Log In")
        root.geometry('400x200+100+100')

        Label(root, text="Username").grid(row=0, column=0)

        username = Entry(root, width=30)
        username.grid(row=0, column=1, columnspan = 2 ,padx=10, pady=10)

        Label(root, text="Password").grid(row=1, column=0)

        password = Entry(root,width=30)
        password.grid(row=1, column=1, columnspan = 2 ,padx=10, pady=10)

        sign_up = Button(root, text="Create User", command=lambda: Controller.sign_up_page(root), fg="blue")
        sign_up.grid(row=2, column=1, sticky=E)

        log_in = Button(root, text="Log In", command = lambda: Controller.login(username, password, root), fg="blue")
        log_in.grid(row=2, column=2, sticky=W)


    def sign_up(root2):

        root2.title("Job Manager Log In")
        root2.geometry('450x200+100+100')

        Label(root2, text="Username").grid(row=0, column=0)

        username = Entry(root2, width=30)
        username.grid(row=0, column=1, columnspan = 2 ,padx=10, pady=10)

        Label(root2, text="Password").grid(row=1, column=0)

        password = Entry(root2, show = '*', width=30)
        password.grid(row=1, column=1, columnspan = 2 ,padx=10, pady=10)

        Label(root2, text="Verify Password").grid(row=2, column=0)

        verify = Entry(root2, show = '*', width=30)
        verify.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        create_user = Button(root2, text="Create User", command = lambda: Controller.create_user(username, password, verify, root2), fg="blue")
        create_user.grid(row=3, column=1, sticky=E)



page = Tk()
Views.login(page)
page.mainloop()