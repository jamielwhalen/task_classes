#scrollbar for enter tasks


def on_mousewheel(event):
    if op_sys == 'OS X':
        canvas.yview_scroll(-1 * (event.delta), "units")
    elif op_sys == 'Windows':
        canvas.yview_scroll(-1 * (event.delta / 120), "units")
    else:
        pass

root2.grid_rowconfigure(1, weight=1)
root2.columnconfigure(1, weight=1)

frame_main = tk.Frame(root2)
frame_main.grid(sticky='news', row = 1, column = 0, ipady= 30)

link_name = ('link'+ str(num))

Label(root2, text="Choose task type:        Input a task URL or local file/application path", font='Helvetica 13 bold').grid(row=0, column=0, sticky = 'w')
# Label(root2, text="Input a task URL or local file/application path", font='Helvetica 13 bold').grid(row=0, column=1)

frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=1, column=0, pady=(0, 0), sticky='nw', ipady= 30)
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
# frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas)  # , bg="yellow")
canvas.grid(row=0, column=0, sticky='news')

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=2, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

canvas.bind_all("<MouseWheel>", on_mousewheel)

frame_buttons = tk.Frame(canvas)  # , bg="blue")
canvas.create_window((0, 0), window=frame_buttons)

if num >= 1 and num < 5:
    for number in range(1, 5):
        choice = StringVar(frame_buttons)
        choices = {'Application', 'File', 'Website'}
        choice.set('Choose Type')

        popUpMenu = OptionMenu(frame_buttons, choice, *choices,
                               command=lambda choice=choice, num=num: (Controller.get_selection(choice, num)))
        popUpMenu.grid(row=num, column=0)

        link_name = Entry(frame_buttons, width=35, borderwidth=5)
        link_name.grid(row=num, column=1, columnspan=3, padx=10, pady=10)

        entry_list.append(link_name)

        num = num + 1

if num >= 5:

    if num > 5:
        global addTask
        addTask.destroy()
        global button2
        button2.destroy()

    for number in range(num):

        choice2 = StringVar(frame_buttons)
        choices = ['Application', 'File', 'Website']
        choice2.set('Choose Type')

        popUpMenu = OptionMenu(frame_buttons, choice2, *choices,
                               command=lambda choice2=choice2, num=num: (Controller.get_selection(choice2, num)))
        popUpMenu.grid(row=number, column=0)

        link_name = Entry(frame_buttons, width=35, borderwidth=5)
        link_name.grid(row=number, column=1, columnspan=3, padx=10, pady=10)

        entry_list.append(link_name)
        print(number)

frame_buttons.update_idletasks()

canvas.config(width=frame_buttons.winfo_width())

canvas.config(scrollregion=canvas.bbox("all"))

if num <= 5:
    canvas.yview_moveto(0)
else:
    canvas.yview_moveto(num)

button2 = Button(root2, text="Add Tasks to Job", command=lambda: Controller.create_task(root2), fg = "blue")
button2.grid(row=num + 1, column=0, sticky = 'e')

addTask = Button(root2, text="Add Task Line", command=lambda: Controller.add_task_line(root2, num), fg = "blue")
addTask.grid(row=num + 1, column=0, sticky = 'w')
