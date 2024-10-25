# PROJECT : Scientific Calculator GUI app using Python and tkinter GUI module
# STUDENT : Moses Mugambi
# MODULE  : Python Programming (Data Science)

# Modules to use: tkinter, math
# tkinter functions to use: Entry, Label, Button, bind(), eval()
#import tkinter modules and math modules to use their built in functions
from tkinter import *
import math 

root = Tk() # instantiate the main window to work with
root.title("Scientific Calculator GUI app") # title name for the GUI app
root.geometry("660x320") # set root window size
root.resizable(False, False)

# create an entry: this will be the main display region for capturing entered numbers and displaying results
e = Entry(root, width=90, borderwidth=5, relief=RIDGE, fg="White", bg="Black", font=("Arial", 10))
e.grid(row=0, column=0, columnspan=8, padx=5, pady=20) # grid is better than pack, grid is specific. 5 rows to span. some padding


def click(to_print):
    old=e.get() # use get function to store user input in entry widget to old variable
    e.delete(0, END) # delete everything on the entry widget
    e.insert(0, old+to_print) # concatenate entered numbers sequentially. to_print is the current number entered
    return
   
def myLog():
    try:
        answer=e.get()
        answer = math.log10(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget

def myLn():
    try:
        answer=e.get()
        answer = math.log(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    
def myExp():
    try:
        answer=e.get()
        answer = math.exp(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget

def myDeg():
    try:
        answer=e.get()
        answer = math.degrees(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    
def mySin():
    try:
        answer=e.get()
        answer = math.sin(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    
def mySinh():
    try:
        answer=e.get()
        answer = math.sinh(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget

def myCos():
    try:
        answer=e.get()
        answer = math.cos(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget    
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget

def myCosh():
    try:
        answer=e.get()
        answer = math.cosh(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget  
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
        
def myTan():
    try:
        answer=e.get()
        answer = math.tan(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget  
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    
def myTanh():
    try:
        answer=e.get()
        answer = math.tanh(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget 
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget

def mySqrt():
    try:
        answer=e.get()
        answer = math.sqrt(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    
def mySquared():
    try:
        answer=e.get()
        answer = float(answer)*float(answer)
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    
def myCubed():
    try:
        answer=e.get()
        answer = float(answer)*float(answer)*float(answer)
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    
def myCubeRoot():
    try:
        answer=e.get()
        answer = math.cbrt(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    
def myFact():
    try:
        answer=e.get()
        answer = math.factorial(int(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget  
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget

def myInverse():
    try:
        answer=e.get()
        answer = (1/(float(answer)))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget  
    
def myPi():
    answer = math.pi
    e.delete(0, END) # delete everything on entry tab widget
    e.insert(0, answer) # insert evaluated answer to entry tab widget

def myRad():
    try:
        answer=e.get()
        answer = math.radians(float(answer))
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
                        
def clear():
    e.delete(0, END)
    return

def bksps():
    current=e.get()
    length=len(current)-1
    e.delete(length, END) # delete everything from the last character minus one to the end and insert to entry widget
    
def evaluate():
    answer=e.get() # store everything from entry tab to ans variable
    try:
        answer=eval(answer) # overwrite final answer when equals to button is clicked, store to ans variable. eval function takes a string that holds mathematical operations and numbers and evaluates it
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
    except:
        answer = 'Error'
        e.delete(0, END) # delete everything on entry tab widget
        e.insert(0, answer) # insert evaluated answer to entry tab widget
 
    
# Create calculator buttons using Button function in tkinter    

seven = Button(root, text="7", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("7"))
eight = Button(root, text="8", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("8"))
nine = Button(root, text="9", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("9"))
four = Button(root, text="4", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("4"))
five = Button(root, text="5", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("5"))
six = Button(root, text="6", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("6"))
one = Button(root, text="1", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("1"))
two = Button(root, text="2", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("2"))
three = Button(root, text="3", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("3"))
zero = Button(root, text="0", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Grey", fg="White", command=lambda: click("0"))

div = Button(root, text=u"\u00F7", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=lambda: click("/"))
mult = Button(root, text="*", padx=22, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=lambda: click("*"))
minus = Button(root, text="-", padx=23, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=lambda: click("-"))
plus = Button(root, text="+", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=lambda: click("+"))

par1st = Button(root, text="(", padx=33, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=lambda: click("("))
par2nd = Button(root, text=")", padx=22, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=lambda: click(")"))
dot = Button(root, text=".", padx=23, pady=4, font=("Arial Bold", 15), relief=RAISED, bg="Black", fg="White", command=lambda: click("."))

equal = Button(root, text="=", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Yellow", fg="Black", command=evaluate)

inverseb = Button(root, text="X"+u"\u207b", padx=25, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myInverse)
log = Button(root, text="log10", padx=14, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myLog)    
ln = Button(root, text="ln", padx=33, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myLn)
factb = Button(root, text="x!", padx=29, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myFact)

XpowerYb = Button(root, text="X"+u"\u02b8", padx=30, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=lambda: click("**"))
modulusb = Button(root, text="%", padx=27, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=lambda: click("%"))

sqrtb = Button(root, text=u"\u221A"+"X", padx=26, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=mySqrt)
squredb = Button(root, text="X"+u"\u00B2", padx=27, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=mySquared)
cubedb = Button(root, text="X"+u"\u00B3", padx=30, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myCubed)
cubeRootb = Button(root, text=u"\u221B"+"X", padx=27, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myCubeRoot)
expb = Button(root, text="e", padx=31, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myExp)
degb = Button(root, text="deg", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myDeg)
sinb = Button(root, text="sin", padx=25, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=mySin)
cosb = Button(root, text="cos", padx=25, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myCos)
tanb = Button(root, text="tan", padx=25, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myTan)
sinhb = Button(root, text="sinh", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=mySinh)
coshb = Button(root, text="cosh", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myCosh)
tanhb = Button(root, text="tanh", padx=20, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myTanh)

ac = Button(root, text="AC", padx=12, pady=5, font=("Arial", 15), relief=RAISED, bg="Red", fg="White", command=clear)
bksp = Button(root, text="DEL", padx=7, pady=5, font=("Arial", 15), relief=RAISED, bg="Red", fg="White", command=bksps)

pib = Button(root, text=u"\u03c0", padx=29, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myPi)
radb = Button(root, text="rad", padx=12, pady=5, font=("Arial", 15), relief=RAISED, bg="Black", fg="White", command=myRad)

# Place calculator buttons on the main root window with specified positions for row and column
inverseb.grid(row=1, column=0)
ln.grid(row=1, column=1)
log.grid(row=1, column=2)
par1st.grid(row=1, column=3)
par2nd.grid(row=1, column=4)
bksp.grid(row=1, column=5)
ac.grid(row=1, column=6)
div.grid(row=1, column=7)

factb.grid(row=2, column=0)
XpowerYb.grid(row=2, column=1)
sqrtb.grid(row=2, column=2)
modulusb.grid(row=2, column=3)
seven.grid(row=2, column=4)
eight.grid(row=2, column=5)
nine.grid(row=2, column=6)
mult.grid(row=2, column=7)

squredb.grid(row=3, column=0)
cubedb.grid(row=3, column=1)
cubeRootb.grid(row=3, column=2)
expb.grid(row=3, column=3)
four.grid(row=3, column=4)
five.grid(row=3, column=5)
six.grid(row=3, column=6)
minus.grid(row=3, column=7)

sinb.grid(row=4, column=0)
cosb.grid(row=4, column=1)
tanb.grid(row=4, column=2)
pib.grid(row=4, column=3)
one.grid(row=4, column=4)
two.grid(row=4, column=5)
three.grid(row=4, column=6)
plus.grid(row=4, column=7)

sinhb.grid(row=5, column=0)
coshb.grid(row=5, column=1)
tanhb.grid(row=5, column=2)
degb.grid(row=5, column=3)
radb.grid(row=5, column=4)
zero.grid(row=5, column=5)
dot.grid(row=5, column=6)
equal.grid(row=5, column=7)

#run the main root window continously 
root.mainloop()