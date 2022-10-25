from tkinter import*

windows = Tk()
windows.title("Miles-to-Kilometer Converter")
windows.minsize(width= 300, height= 200)
windows.config( padx=30, pady=30)


#Convert_function
def convert():
    miles = float(miles_entry.get()) #Getting the miles from input
    km = miles * 1.609
    result_lable.config(text =f'{km}')

#miles


miles_entry = Entry()
miles_entry.grid(column=1, row=0)


miles = Label(text="Miles", font=('Arial',12, 'bold'))
miles.grid(column=2, row=0)

is_equal = Label(text = "is equal to", font=('Arial',12, 'bold'))
is_equal.grid(column=0, row=1)



#kilometer
result_lable = Label(text = 'result lable', font=('Arial',12, 'bold'))
result_lable.grid(column=1, row=1)


kilometer = Label(text="kilometer", font=('Arial',12, 'bold'))
kilometer.grid(column=2, row=1)



#Button
button = Button( text="Convert", command=convert)
button.grid(column=1, row=2)

windows,mainloop()
