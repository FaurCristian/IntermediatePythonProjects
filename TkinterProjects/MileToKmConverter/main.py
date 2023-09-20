from tkinter import *


def action():
    miles = float(entry.get())
    km = miles * 1.609344
    result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Convertor")
window.config(padx=20, pady=20)


entry = Entry(width=7)
entry.grid(column=1, row=0)

miles_text = Label(text="Miles", font=("Arial", 10, "bold"))
miles_text.grid(column=2, row=0)

is_equal_to_text = Label(text="is equal to ", font=("Arial", 10, "bold"))
is_equal_to_text.grid(column=0, row=1)

result = Label(text="0", font=("Arial", 10, "bold"))
result.grid(column=1, row=1)

km_text = Label(text="Km", font=("Arial", 10, "bold"))
km_text.grid(column=2, row=1)

button = Button(text="Calculate", command=action, font=("Arial", 10, "bold"))
button.grid(column=1, row=2)

window.mainloop()
