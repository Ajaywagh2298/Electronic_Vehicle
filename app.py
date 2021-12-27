#how to create simple GUI registration form.
#importing tkinter module for GUI application
from tkinter import *

#Creating object 'root' of Tk()
import click
from sympy.physics.units import action

root = Tk()

#Providing Geometry to the form
root.geometry("500x500")

#Providing title to the form
root.title('Electric vehicle')

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Electric vehicle data", width=20,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)

#this creates 'Label' widget for Fullname and uses place() method.
label_1 =Label(root,text="FullName", width=20,font=("bold",10))
label_1.place(x=80,y=130)

#this will accept the input string text from the user.
entry_1=Entry(root)
entry_1.place(x=240,y=130)


label_2 =Label(root,text="entry_1", width=20,font=("bold",10))
label_2.place(x=68,y=180)

entry_2=Entry(root)
entry_2.place(x=240,y=180)

#this creates 'Label' widget for Email and uses place() method.
label_3 =Label(root,text="Email", width=20,font=("bold",10))
label_3.place(x=68,y=230)

entry_3=Entry(root)
entry_3.place(x=240,y=230)

#this creates 'Label' widget for Gender and uses place() method.
label_4 =Label(root,text="Gender", width=20,font=("bold",10))
label_4.place(x=70,y=280)


#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#this creates 'Radio button' widget and uses place() method
#


##this creates 'Label' widget for country and uses place() method.
label_5=Label(root,text="Country",width=20,font=("bold",10))
label_5.place(x=70,y=330)

#this creates list of countries available in the dropdownlist.
list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

#the variable 'c' mentioned here holds String Value, by default ""
c=StringVar()
droplist=OptionMenu(root,c, *list_of_country)
droplist.config(width=15)
c.set('Select your Country')
droplist.place(x=240,y=330)

##this creates 'Label' widget for Language and uses place() method.
label_6=Label(root,text="Language",width=20,font=('bold',10))
label_6.place(x=75,y=380)


#the variable 'var1' mentioned here holds Integer Value, by default 0
var1=IntVar()
#this creates Checkbutton widget and uses place() method.
Checkbutton(root,text="English", variable=var1).place(x=230,y=380)


#the variable 'var2' mentioned here holds Integer Value, by default 0
var2=IntVar()
Checkbutton(root,text="German", variable=var2).place(x=290,y=380)

#this creates button for submitting the details provides by the user
Button(root, text='Submit' , width=20,bg="black",fg='white',command=click).place(x=180,y=380)

action.pack()

#this will run the mainloop.
root.mainloop()