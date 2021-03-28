from tkinter import *
import backend


# This function helps to display selected texts in the various boxes
def get_selected_row(event):
    try:  # Use the try function to catch the IndexError error and print a friendly message. The index error occurs
        # when you click on an empty list box
        global selected_tuple
        index = list1.curselection()[0]  # selects the index of the selected tuple when clicked
        selected_tuple = list1.get(index)
        # Now we will call each of the text boxes and empty them
        textbox1.delete(0, END)
        # Now we will insert the value of selected item from the list into the text box so the user can see it
        textbox1.insert(END, selected_tuple[1])
        # This has to be repeated for each of the text boxes.
        textbox2.delete(0, END)
        textbox2.insert(END, selected_tuple[2])

        textbox3.delete(0, END)
        textbox3.insert(END, selected_tuple[3])

        textbox4.delete(0, END)
        textbox4.insert(END, selected_tuple[4])
    except IndexError:
        print("List is Empty. Click View Entries to display the list or add an entry to the database")


def view_command():
    list1.delete(0, END)  # This ensures the listbox is empty at first call
    for row in backend.view():
        list1.insert(END, row)  # insert result at end of list


def search_command():
    list1.delete(0, END)  # This ensures the listbox is empty at first call
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):  # the .get()
        # method allows the input to be passed in as plain text from the Stringvar() variable
        list1.insert(END, row)  # The end ensures that the new entry does not overwrite what is already there


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))  # Displays the text after adding


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def clear_command():
    textbox1.delete(0, END)
    textbox2.delete(0, END)
    textbox3.delete(0, END)
    textbox4.delete(0, END)


# This capitalises each word typed by the user so that it is easy to search the database later
def autocapitalize_title(*args):
    title_text.set(title_text.get().title())


def autocapitalize_author(*args):
    author_text.set(author_text.get().title())

# Create an empty tkinter window
window = Tk()
window.title("App Library v1.0")

# Set the size of the window if you want to
# window.geometry("600x200")


l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Create text boxes for the title
title_text = StringVar()  # This receives input from the box
title_text.trace_add('write', autocapitalize_title)
textbox1 = Entry(window, textvariable=title_text)
textbox1.grid(row=0, column=1)



# Create text boxes for the author
author_text = StringVar()
author_text.trace_add('write', autocapitalize_author)
textbox2 = Entry(window, textvariable=author_text)
textbox2.grid(row=0, column=3)

# Create text boxes for the year
year_text = StringVar()
textbox3 = Entry(window, textvariable=year_text)
textbox3.grid(row=1, column=1)

# Create text boxes for the isbn
isbn_text = StringVar()
textbox4 = Entry(window, textvariable=isbn_text)
textbox4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# create scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# Configure scroll bar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Bind
list1.bind('<<ListboxSelect>>', get_selected_row)

# Create a button widget. The commands they bind to are created in functions at the top of the script

b1 = Button(window, text="View Entries", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entries", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Entry", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Entry", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Clear Inputs", width=12, command=clear_command)
b6.grid(row=7, column=3)

b7 = Button(window, text="Close Program", width=12, command=window.destroy)
b7.grid(row=8, column=3)



window.mainloop()  # Keeps the window open till it is closed by user
