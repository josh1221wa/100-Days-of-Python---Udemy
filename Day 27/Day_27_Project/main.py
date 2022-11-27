from tkinter import *

def convert():
    mile = int(input.get())
    km = round(mile * 1.609)
    answer_label["text"] = str(km)

window = Tk()
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")

label1 = Label(text="is equal to")
label1.grid(row=1, column=0)

answer_label = Label(text="0")
answer_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=3)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=3)

input = Entry(width=7)
input.insert(END, string="0")
input.grid(row=0, column=1)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()