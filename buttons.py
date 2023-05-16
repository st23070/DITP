from tkinter import * #imports everything from TK

root = Tk() # top level window


def callback():
    label.config(text='You clicked me', fg='red', bg='yellow')




#create label
label = Label(root, text="Hello Python")
label.pack()

#Create button
button = Button(root, text='Click Me!', command=callback)
button['state'] = 'disabled' 
button['state'] = 'normal'
button.pack()

root.geometry("350x300")
root.mainloop()
                  