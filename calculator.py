# Importing Libraries
from tkinter import *
import expsolve as esol

# defining globals
curr = "0"

# define button functions
def clr():
    global curr
    e.delete( 0 , 'end' )
    e.insert(0 , "0")
    curr = "0"

def id0():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "0"
    else:
        curr += "00"
    e.insert(0,curr)

def i0():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "0"
    else:
        curr += "0"
    e.insert(0,curr)

def i1():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "1"
    else:
        curr += "1"
    e.insert(0,curr)

def i2():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "2"
    else:
        curr += "2"
    e.insert(0,curr)

def i3():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "3"
    else:
        curr += "3"
    e.insert(0,curr)

def i4():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "4"
    else:
        curr += "4"
    e.insert(0,curr)

def i5():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "5"
    else:
        curr += "5"
    e.insert(0,curr)

def i6():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "6"
    else:
        curr += "6"
    e.insert(0,curr)

def i7():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "7"
    else:
        curr += "7"
    e.insert(0,curr)

def i8():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "8"
    else:
        curr += "8"
    e.insert(0,curr)

def i9():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "9"
    else:
        curr += "9"
    e.insert(0,curr)

def isum():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "0"
    else:
        curr += "+"
    e.insert(0,curr)

def idif():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "-"
    else:
        curr += "-"
    e.insert(0,curr)

def idiv():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "0"
    else:
        curr += "/"
    e.insert(0,curr)

def ipro():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "0"
    else:
        curr += "*"
    e.insert(0,curr)

def ipow():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "0"
    else:
        curr += "^"
    e.insert(0,curr)

def imod():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "0"
    else:
        curr += "%"
    e.insert(0,curr)

def ibro():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "("
    else:
        curr+="("
    e.insert(0,curr)

def ibrc():
    global curr
    e.delete( 0 , 'end' )
    if( curr == "0" ):
        curr = "0"
    else:
        curr+=")"
    e.insert(0,curr)

def execute():
    global curr
    e.delete( 0 , 'end' )
    curr = esol.solve_expression(curr)
    if(type(curr)==str):
        e.insert(0,curr)
        curr="0"
    else:
        e.insert(0,curr)
        curr=str(curr)

# Initializing window
root = Tk()
root.title("Calculator")
root.geometry( "640x480+500+200" )
root.minsize( 640 , 480 )
root.maxsize( 640 , 480 )
root.configure( background = "#2f3640" )

# main layout
def init_layout():
    buttonclr = Button( root , text = "CC / CA" , width = 12, height = 2 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = clr )
    buttnd0 = Button( root , text = "00" , width = 12 , height = 11 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = id0 )
    button0 = Button( root , text = "0" , width = 12 , height = 11 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i0 )
    button1 = Button( root , text = "1" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i1 )
    button2 = Button( root , text = "2" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i2 )
    button3 = Button( root , text = "3" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i3 )
    button4 = Button( root , text = "4" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i4 )
    button5 = Button( root , text = "5" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i5 )
    button6 = Button( root , text = "6" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i6 )
    button7 = Button( root , text = "7" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i7 )
    button8 = Button( root , text = "8" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i8 )
    button9 = Button( root , text = "9" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = i9 )
    buttonsum = Button( root , text = "+" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = isum )
    buttondif = Button( root , text = "-" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = idif )
    buttondiv = Button( root , text = "/" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = idiv )
    buttonmod = Button( root , text = "%" , width = 12 , height = 11 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = imod )
    buttonpro = Button( root , text = "*" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = ipro )
    buttonpow = Button( root , text = "^" , width = 12 , height = 11 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = ipow )
    buttonbro = Button( root , text = "(" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = ibro )
    buttonbrc = Button( root , text = ")" , width = 12 , height = 7 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = ibrc )
    buttonequ = Button( root , text = "=" , width = 12 , height = 11 , relief = "raised" , bg = "#353b48" , activebackground = "#2f3640" , highlightbackground = "#ffffff" , fg = "#ffffff" , command = execute )

    # defining out area
    global e
    e = Entry( root , font = "Ariel 20 bold" , justify = "right" , width =  35 , state = "normal"  , cursor = "arrow" , bg = "#282e46" , fg = "#ffffff" , highlightbackground = "#ffffff" , highlightthickness = 3 , borderwidth = 0 )
    e.insert( 0 , "0" )

    # placing everything together
    button0.grid( row = 4 , column = 0 )
    buttnd0.grid( row = 4 , column = 1 )
    buttonequ.grid( row = 4 , column = 2 )
    buttonpow.grid( row = 4 , column = 3 )
    buttonmod.grid( row = 4 , column = 4 )
    button1.grid( row = 3 , column = 0 )
    button2.grid( row = 3 , column = 1 )
    button3.grid( row = 3 , column = 2 )
    buttonpro.grid( row = 3 , column = 3 )
    buttondiv.grid( row = 3 , column = 4 )
    button4.grid( row = 2 , column = 0 )
    button5.grid( row = 2 , column = 1 )
    button6.grid( row = 2 , column = 2 )
    buttonsum.grid( row = 2 , column = 3 )
    buttondif.grid( row = 2 , column = 4 )
    button7.grid( row = 1 , column = 0 )
    button8.grid( row = 1 , column = 1 )
    button9.grid( row = 1 , column = 2 )
    buttonbro.grid( row = 1 , column = 3 )
    buttonbrc.grid( row = 1 , column = 4 )
    e.grid( row = 0 , column = 1 , columnspan = 4 , padx = 10 , pady = 10 )
    buttonclr.grid( row = 0 , column = 0 , padx = 5 )

# start window loop
init_layout()
root.mainloop()
