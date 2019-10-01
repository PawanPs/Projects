from tkinter import *
import tkinter.messagebox
#init
#------------------------
font_style = ('Times',13)

#function
#-----------------------
def callback():
    if tkinter.messagebox.askokcancel("Save file", "File might not be saved!\nExit anyway?"):
        root.destroy()


#mainloop-----------------
root = Tk()
root.title('Expense Tracker')    #set_title
#root.iconbitmap('File_loc')     #set_icon
root.geometry('800x600')         #set_default window size
root.resizable(0, 0)             #no_resize

#lable_file name
label1 = Label(root, text='Enter date  :', font=font_style)
label1.place(x=5, y=5, height= 50, width= 120)

label2 = Label(root, text='(mmm-yyyy)', font=('Times',10))
label2.place(x=135, y=40, height= 50, width= 120)

#entry_box - filename
file_name = Entry(root, font=font_style)
file_name.place(x=120, y=12, height= 35, width= 150)

#ok_button
submit = Button(root, text=' SELECT ', font =('Times',11))
submit.place(x= 285, y=12, height= 35, width= 75)

#create_frame_listbox
frame_lb = Frame(root,bg='blue')
frame_lb.place(x= 5, y=115, height= 405, width= 680)

frame_add = Frame(root,bg='black')
frame_add.place(x= 5, y=530, height= 35, width= 680)

frame_info = Frame(root,bg='black')
frame_info.place(x= 5, y=80, height= 35, width= 680)

#add_button
add = Button(root, text=' ADD ', font =('Times',11))
add.place(x= 705, y=530, height= 35, width= 75)

#delete_button
del1 = Button(root, text=' DELETE ', font =('Times',11))
del1.place(x= 705, y=460, height= 35, width= 75)

#graph_button
graph = Button(root, text=' GRAPH ', font =('Times',11))
graph.place(x= 705, y=230, height= 35, width= 75)

#listboxes_frame_lb
date = Listbox(frame_lb)
date.pack(side=LEFT,expand=True,fill='both')

description = Listbox(frame_lb)
description.pack(side=LEFT,expand=True,fill='both')

DA = Listbox(frame_lb)
DA.pack(side=LEFT,expand=True,fill='both')

CA = Listbox(frame_lb)
CA.pack(side=LEFT,expand=True,fill='both')

BAL = Listbox(frame_lb)
BAL.pack(side=LEFT,expand=True,fill='both')

#frame_info
date1 = Label(frame_info,text = 'DATE', font = font_style,bg='grey')
date1.pack(side=LEFT,expand=True,fill='both')

description1 = Label(frame_info,text = 'DESCRIPTION', font = font_style,bg='grey')
description1.pack(side=LEFT,expand=True,fill='both')

DA1 = Label(frame_info,text = 'DEBIT', font = font_style,bg='grey')
DA1.pack(side=LEFT,expand=True,fill='both')

CA1 = Label(frame_info,text = 'CREDIT', font = font_style,bg='grey')
CA1.pack(side=LEFT,expand=True,fill='both')

BAL1 = Label(frame_info,text = 'BALANCE', font = font_style,bg='grey')
BAL1.pack(side=LEFT,expand=True,fill='both')


root.protocol("WM_DELETE_WINDOW", callback) # exit popup
#---------
root.mainloop
