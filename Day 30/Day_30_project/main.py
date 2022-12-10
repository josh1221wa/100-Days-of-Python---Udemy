from tkinter import *
from tkinter import messagebox  #Since messagebox is not a class or a constant we have to import it
import random
import pyperclip    #Helps to copy or paste to/fro from the clipboard
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    global password_entry

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)    #Adds text to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global website_entry, email_entry, password_entry
    website = website_entry.get()
    user_id = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email" : user_id,
            "password" : password
        }
    }

    if len(website) * len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
        return
    try:
        with open("Day 30/Day_30_Project/data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
    except FileNotFoundError:
        with open("Day 30/Day_30_Project/data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)            
    else:
        with open("Day 30/Day_30_Project/data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    website_entry.delete(0, "end")
    password_entry.delete(0, "end")

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    global website_entry
    search_website = website_entry.get()
    
    try:    
        with open("Day 30/Day_30_Project/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if search_website in data:
            messagebox.showinfo(title=search_website, message=f"Email: {data[search_website]['email']}\nPassword: {data[search_website]['password']}")
        else:
            messagebox.showinfo(title="", message=f"No details for {search_website} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file=r"Day 30/Day_30_Project/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=17)
website_entry.grid(row=1, column=1, sticky=EW)    #columnspan helps the element to span across multiple columns in the grid
website_entry.focus()   #focus keeps the cursor on this entry field when we open the GUI

search_but = Button(text="Search", command=find_password)
search_but.grid(row=1, column=2, sticky=EW)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_entry.insert(0, "james@gmail.com")    #First argument is the index where to be inserted. Since we are adding in the beginning we give in 0

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1, sticky=EW)

generate_password_but = Button(text="Generate Password", command=generate_password)
generate_password_but.grid(row=3, column=2)

add_password_but = Button(text="Add", width=30, command=save)
add_password_but.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()

