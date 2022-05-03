from tkinter import *


root = Tk()
root['bg'] = 'black'
root.title('ProvodnikLevDim')
root.wm_attributes('-alpha', 1)
root.geometry('800x600')

frame=Frame(root, bg='red')
frame.place(relx=0, rely=0, relwidth=1, relheight=0.05)

Button = Button(frame, text='коп', bg='red', font=40)
Button.place(relx=0, rely=0)

root.mainloop()