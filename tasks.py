import tkinter as tk
from tkinter import *
import sqlite3
import subprocess
import webbrowser
import tkinter.messagebox

import sys

global op_sys

platforms = {
    'linux1': 'Linux',
    'linux2': 'Linux',
    'darwin': 'OS X',
    'win32': 'Windows'
}
if sys.platform in platforms:
    op_sys = platforms[sys.platform]
else:
    op_sys = "Not present"




conn = sqlite3.connect('task.db')
c = conn.cursor()


entry_list = []
options = {}
entry_dict= {}
delete_dict ={}




class Tasks (object):

    def __init__(self, link, type, active):
        self.link = link
        self.type = type
        self.active = active

    def get_link(self):
        return self.link

    def set_link(self, link):
        self.link = link

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_active(self):
        return self.active

    def set_active(self, active):
        self.active = active




class Controller():

    def __init__(self):
        pass

    def edit_jobs(root):
        root.withdraw()
        page3 = Tk()
        page3.title("Edit Jobs")
        Views.create_edit_page(page3)


    def create_job(page_name):
        warning = Tk()
        warning.withdraw()

        global y
        y = entry1.get()

        c.execute('SELECT name from sqlite_master where type= "table"')
        tables = c.fetchall()

        for table in tables:
            for i in table:
                print (i)
                print (y)
                if y == str(i):
                    warning.bell()
                    tkinter.messagebox.showerror("Error","Cannot create duplicate Job names. Please re-enter Job name.",icon='warning')
                    return

        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q','r','s','t', 'u', 'v', 'w','x','y','z',
                 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '_']
        new_phrase = ""

        error = "no"
        for letter in y:
            if letter not in set(alpha):
                error = "yes"
                if letter == ' ':
                    letter = "_"
                else:
                    letter = ''
                new_phrase += letter
            else:
                new_phrase += letter

        if error == "yes":
            y = new_phrase
            warning.bell()
            if tkinter.messagebox.askokcancel("Error", 'Job name can only contain alphabetic characters. Invalid characters have been removed. OK to continue or Cancel to re-enter.', icon='warning'):

                ct_str = ('CREATE TABLE IF NOT EXISTS ' + y + '(num Integer, link Text, type Text, active Text)')
                ct_str = str(ct_str)
                c.execute(ct_str)
                page_name.withdraw()
                global page2
                page2 = Tk()
                page2.title(y)
                Views.create_task_page(page2, 1)
            else:
                return

        elif error == "no":
            ct_str = ('CREATE TABLE IF NOT EXISTS ' + y + '(num Integer, link Text, type Text, active Text)')
            ct_str = str(ct_str)
            c.execute(ct_str)
            page_name.withdraw()
            page2 = Tk()
            page2.title(y)
            Views.create_task_page(page2, 1)


        global n
        n=5

    def run_task(name):
        sql = ("SELECT * FROM " + name)
        c.execute(sql)
        rows = c.fetchall()

        for row in rows:
            print(row)

            if row[2] == "File":
                print("yes")
                a = row[1]
                print(a)
                # either one of these processes do and if statement w/radio buttons
                subprocess.call(['open', a])
            elif row[2] =="Application":
                print("yes")
                a = row[1]
                print(a)
                # either one of these processes do and if statement w/radio buttons
                subprocess.call(['open', a])

            else:
                a = row[1]
                print(a)
                print("yes web")
                webbrowser.open(a)




    def create_task(create_page):

            list1 = []
            for lnk in entry_list:
                list1.append(lnk.get())

            e = len(list1)
            t = len(options)

            for idx in range(0, t):
                a = idx+1
                b=list1[idx]
                d=options[a]
                e = "Active"

                add1 = ("INSERT INTO " + str(y) + " VALUES('" + str(a)+"','" + str(b)+"', '"+str(d) +"', '"+str(e)+"')")
                c.execute(str(add1))
                conn.commit()

            options.clear()
            entry_list.clear()

            create_page.withdraw()
            new_page = Tk()
            new_page.title("Job Manager")
            Views.home_page(new_page)


    def add_task_line(page_num, it_num):
        it_num += 1
        Views.create_task_page(page_num, it_num)

    def add_task_line2(page_num, task, it_num):
        it_num += 1
        Views.edit_task_page(page_num, task, it_num)


    def get_selection(choice, num):
        options[num] = choice
        print(options)

    def edit_task(i, page_name):
        page_name.withdraw()
        a = Tk()
        title = ("Edit " + i + " Job Tasks")
        a.title(title)
        Views.edit_task_page(a, i, 0)

    def update_task(task, update_page):

        key_list = []
        for key in options.keys():
            key_list.append(key)


        for number in key_list:

            delete = ('DELETE from ' + str(task) + ' WHERE num = ' + str(number))
            c.execute(delete)
            conn.commit()

            for entry in entry_dict.keys():
                if entry == number:

                    y = task
                    a = entry
                    b = entry_dict[entry].get()
                    d = options[entry]
                    e = "Active"

                    add1 = ("INSERT INTO " + str(y) + " VALUES('" + str(a) + "','" + str(b) + "', '" + str(d) + "', '" + str(e) + "')")
                    c.execute(str(add1))
                    conn.commit()

        string = ('SELECT * from ' + str(task) + ' ORDER BY 1')

        c.execute(string)
        tasks = c.fetchall()
        items_dict = {}
        for item in tasks:
            items_dict[item[0]] = item[1]

        entry_text_dict = {}
        for x in entry_dict:
            entry_text_dict[x] = entry_dict[x].get()


        for item2 in tasks:
            for key in entry_text_dict.keys():
                if item2[0] == key:
                    if item2[1] != entry_text_dict[key]:
                        print("no they values do not match")

                        delete = ('DELETE from ' + str(task) + ' WHERE num = ' + str(key))
                        c.execute(delete)
                        conn.commit()

                        y = task
                        a = key
                        b = entry_text_dict[key]
                        d = item2[2]
                        e = "Active"

                        add1 = ("INSERT INTO " + str(y) + " VALUES('" + str(a) + "','" + str(b) + "', '" + str(d) + "', '" + str(e) + "')")
                        c.execute(str(add1))
                        conn.commit()

        print(delete_dict)

        for idx in delete_dict.keys():
            a = delete_dict[idx]
            if a == 1:
                delete = ('DELETE from ' + str(task) + ' WHERE num = ' + str(idx))
                c.execute(delete)
                conn.commit()


        options.clear()
        entry_dict.clear()
        delete_dict.clear()
        entry_text_dict.clear()

        update_page.withdraw()
        new_page = Tk()
        new_page.title("Job Manager")
        Views.home_page(new_page)

    def delete_task(var1, line):
        print(var1.get())
        print(line)
        delete_dict[line] = var1.get()






class Views():


    def home_page(root):

        def on_mousewheel(event):
            if op_sys == 'OS X':
                canvas.yview_scroll(-1 * (event.delta), "units")
            elif op_sys == 'Windows':
                canvas.yview_scroll(-1 * (event.delta / 120), "units")
            else:
                pass

        root.grid_rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        frame_main = tk.Frame(root)
        frame_main.grid(sticky='news')


        global entry1
        entry1 = Entry(frame_main, width=35, borderwidth=1)
        entry1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        entry1.insert(0, "Enter Job Name")

        create_button = Button(frame_main, text="Create Job", command= lambda: Controller.create_job(root), fg = "blue")
        create_button.grid(row=0, column=4)

        edit_button = Button(frame_main, text="Edit Jobs", command=lambda:Controller.edit_jobs(root))
        edit_button.configure(fg="blue")
        edit_button.grid(row=1, column=4)


        executeTask = Label(frame_main, text="  Jobs to Execute", font='Helvetica 13 bold')
        executeTask.grid(row=1, column=2, sticky = 'w')

        frame_canvas = tk.Frame(frame_main)
        frame_canvas.grid(row=2, column=2, pady=(0, 0), sticky = 'nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        # frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        canvas = tk.Canvas(frame_canvas) #, bg="yellow")
        canvas.grid(row=0, column=0, sticky = 'news')

        # Link a scrollbar to the canvas
        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=2, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        canvas.bind_all("<MouseWheel>", on_mousewheel)

        frame_buttons = tk.Frame(canvas) #, bg="blue")
        canvas.create_window((0, 0), window=frame_buttons)

        c.execute('SELECT name from sqlite_master where type= "table"')
        tables = c.fetchall()
        b = 0
        for table in tables:
            for i in table:
                a = str(i)
                a = Button(frame_buttons, text=a, command=lambda i=i: Controller.run_task(i))
                a.grid(row=b, column=0)
                b = b + 1

        frame_buttons.update_idletasks()

        canvas.config(width = frame_buttons.winfo_width())

        canvas.config(scrollregion=canvas.bbox("all"))
        canvas.yview_moveto(0)
        Label(root, text="", font='Helvetica 13 bold').grid(row=b+1, column=0)

    def create_task_page(root2, num):

        link_name = ('link'+ str(num))

        Label(root2, text="Choose task type:", font='Helvetica 13 bold').grid(row=0, column=0)
        Label(root2, text="Input a task URL or local file/application path", font='Helvetica 13 bold').grid(row=0, column=2)

        if num >= 1 and num <5:
            for num in range(1,5):
                choice = StringVar(root2)
                choices = {'Application', 'File', 'Website'}
                choice.set('Choose Type')


                popUpMenu = OptionMenu(root2, choice, *choices, command = lambda choice = choice, num = num: (Controller.get_selection(choice, num)))
                popUpMenu.grid(row=num, column=0)


                link_name = Entry(root2, width=35, borderwidth = 5)
                link_name.grid(row=num, column = 1, columnspan = 3, padx= 10, pady = 10)

                entry_list.append(link_name)

                num = num + 1




        if num >= 5:

            if num > 5:
                global addTask
                addTask.destroy()
                global button2
                button2.destroy()

            choice2 = StringVar(root2)
            choices = ['Application', 'File', 'Website']
            choice2.set('Choose Type')

            popUpMenu = OptionMenu(root2, choice2, *choices, command = lambda choice2 = choice2, num = num: (Controller.get_selection(choice2, num)))
            popUpMenu.grid(row=num, column=0)

            link_name = Entry(root2, width=35, borderwidth=5)
            link_name.grid(row=num, column=1, columnspan=3, padx=10, pady=10)

            entry_list.append(link_name)

        button2 = Button(root2, text="Add Tasks to Job", command=lambda: Controller.create_task(root2), fg = "blue")
        button2.grid(row=num + 1, column=2)

        addTask = Button(root2, text="Add Task Line", command=lambda: Controller.add_task_line(root2, num), fg = "blue")
        addTask.grid(row=num + 1, column=0)


    def edit_task_page(root4, task, num):

        string = ('SELECT * from ' + str(task) + ' ORDER BY 1')

        c.execute(string)
        tasks = c.fetchall()

        Label(root4, text="Task Type", font='Helvetica 13 bold').grid(row=0, column=0)
        Label(root4, text="Task Link", font='Helvetica 13 bold').grid(row=0, column=1)
        Label(root4, text="Delete Task", font='Helvetica 13 bold').grid(row=0, column=2)

        if num <= len(tasks):
            for edit_task in tasks:
                    num = edit_task[0]
                    # a = str(edit_task)
                    # Label(root4, text=a).grid(row=num+1, column=0)

                    choice = StringVar(root4)
                    choices = ['Application', 'File', 'Website']
                    choice.set(edit_task[2])

                    popUpMenu = OptionMenu(root4, choice, *choices, command=lambda choice=choice, num= num: (Controller.get_selection(choice, num)))
                    popUpMenu.grid(row=num+1, column=0)

                    e = Entry(root4, width=35)
                    e.grid(row=num+1, column = 1, padx=10, pady=10)
                    e.insert(0, edit_task[1])

                    var1 = IntVar(root4)
                    Checkbutton(root4, text="", variable=var1, command = lambda var1 = var1, num=num:(Controller.delete_task(var1,num))).grid(row=num+1, column = 2)

                    entry_dict[num] = e

        else:
            print("true")
            global addTask
            addTask.destroy()
            global button2
            button2.destroy()
            Label(root4, text="").grid(row=num+1, column=0)

            choice = StringVar(root4)
            choices = ['Application', 'File', 'Website']
            choice.set('Choose Type')
            popUpMenu = OptionMenu(root4, choice, *choices, command=lambda choice=choice, num=num: (Controller.get_selection(choice, num)))
            popUpMenu.grid(row=num+1, column=0)

            e = Entry(root4, width=35)
            e.grid(row=num+1, column=1, padx=10, pady=10)

            var1 = IntVar(root4)
            Checkbutton(root4, text="", variable=var1, command=lambda var1=var1, num=num: (Controller.delete_task(var1,num))).grid(row=num + 1, column=2)

            entry_dict[num] = e

        button2 = Button(root4, text="Update Job Tasks", command=lambda: Controller.update_task(task, root4), fg = "blue")
        button2.grid(row=num + 2, column=2, sticky=E)

        addTask = Button(root4, text="Add Task Line", command=lambda: Controller.add_task_line2(root4,task, num), fg = "blue")
        addTask.grid(row=num + 2, column=0)




    def create_edit_page(root3):

        Label(root3, text="Choose Job to Edit:", font='Helvetica 13 bold').grid(row=0, column=0)

        def on_mousewheel(event):
            if op_sys == 'OS X':
                canvas.yview_scroll(-1 * (event.delta), "units")
            elif op_sys == 'Windows':
                canvas.yview_scroll(-1 * (event.delta / 120), "units")
            else:
                pass

        root3.grid_rowconfigure(0, weight=1)
        root3.columnconfigure(0, weight=1)

        frame_main = tk.Frame(root3)
        frame_main.grid(sticky='news')

        canvas = tk.Canvas(frame_main)
        canvas.grid(row=0, column=0, sticky='news')

        vsb = tk.Scrollbar(frame_main, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=2, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        frame_buttons = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_buttons)

        canvas.bind_all("<MouseWheel>", on_mousewheel)

        c.execute('SELECT name from sqlite_master where type= "table"')
        tables = c.fetchall()

        b = 1
        for table in tables:
            for i in table:
                a = str(i)
                a = Button(frame_buttons, text=a, command=lambda i=i: Controller.edit_task(i, root3))
                a.grid(row=b, column=1)
                Label(frame_buttons, text="        ").grid(row=b, column=0)
                Label(frame_buttons, text="        ").grid(row=b, column=2)
                b = b + 1

        frame_buttons.update_idletasks()

        canvas.config(width=frame_buttons.winfo_width())

        canvas.config(scrollregion=canvas.bbox("all"))
        canvas.yview_moveto(0)


global page
page = Tk()
page.title("Job Manager")


Views.home_page(page)






page.mainloop()