from tkinter import *
import Book_backend


window = Tk()
window.wm_title("Book Store")
# binding book_list with selected_tuple
def get_selected_row(event):
    global selected_tuple
    index = book_list.curselection()[0]
    selected_tuple = book_list.get(index)
    #set entry fields to selected_tuple
    e1.delete(0, END)
    e1.insert(0, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(0, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(0, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(0, selected_tuple[4])

    # wrapper functions to avoid params


def view_command():
    # first erase anything in view
    book_list.delete(0, END)
    for row in Book_backend.view():
        book_list.insert(END, row)


def search_command():
    book_list.delete(0, END)
    for row in Book_backend.search(title_text.get(), author_text.get(),
                                   year_text.get(), isbn_text.get()):
        book_list.insert(END, row)


def add_command():
    # add the info from entry fields in gui
    Book_backend.insert(title_text.get(), author_text.get(),
                                   year_text.get(), isbn_text.get())
    # redraw the view
    view_command()


def update_command():
    Book_backend.update(selected_tuple[0], title_text.get(), author_text.get(),
                                   year_text.get(), isbn_text.get())
    view_command()


def delete_command():
    Book_backend.delete(selected_tuple[0])
    view_command()







l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)


author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

book_list = Listbox(window, height=6, width=35)
book_list.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=1, column=2, rowspan=6)

book_list.configure(yscrollcommand=sb.set)
sb.configure(command=book_list.yview)

# bind Listbox to Selected Row
book_list.bind('<<ListboxSelect>>', get_selected_row)



b1 = Button(window, text='View All', width=15, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search', width=15, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=15, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width=15, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width=15, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=15, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()