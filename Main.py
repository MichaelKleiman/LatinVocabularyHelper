'''

@author: Michael Kleiman
I've had no formal Python, so the style might not be 'correct'


'''


from tkinter import *
from random import *
import os

loc = os.path.join(os.path.dirname(__file__), 'list.txt')
sav = os.path.join(os.path.dirname(__file__), 'save.txt')

current = '' #the current word
currentint = -1 #the location of the current word

#loads a word from the source text file
def loadWord (f):
    t = f.readline()
    st = ""
    while True:
        if "Headword" in t:
            t = t.split(">")
            t = t[2].split("<")
            t = t[0]
            if " " in t:
                t = t.split(" ")
                if ',' in t[0]:
                    t[0] = t[0].split(',')[0]                    
                for i in range(len(t)):
                    st += t[i]
                    st += "&"
                    i = i + 1
            else: 
                st += t
                st += "&"
            st += "$"
            t = f.readline()
            t = f.readline()
            t = t.split(">")
            t = t[1].split("<")
            t = t[0].split(",")
            for i in range(len(t)):
                st += t[i]
                st += "&"
            return st
        
        t = f.readline()
        if (t == ""):
            return ""
        
ws = ['0'] * 997 #words
vs = ['0'] * 997 #values

saves = open(sav, "r")

for i in range(0, 997):
    vs[i] = saves.readline()
saves.close()    


s = " "
i = 0


file = open(loc, "r")
while True:
    s = loadWord(file)
    if (s != ""):
        ws[i] = s
        i = i + 1
    else:
        break

file.close()

#rewrites save.txt with the data in vs
def save():
    saves = open(sav, "w")
    global vs
    for i in range (0, 997):
        saves.write(vs[i])
        #saves.write('\n')
        
    messagebox.config(text = "")
    saves.close()
    messagebox.config(text = "saved")
      
#brings up the quit box        
def q():
    messagebox.config(text = "")
    t = Toplevel(width = 10)
    title = Label(t, height = 1, width = 29, font = "Times")
    yes = Button(t, text = "yes", command = leave, width = 3)
    no = Button(t, text = "no", command = sys.exit, width = 3)
    
    title.pack()
    title.config(text = "Do you want to save before exiting?    ")
    yes.pack()
    no.pack()

#saves then exits
def leave():   
    save()
    sys.exit()
    
#gets a random new word from ws, whose index is a 0 in vs
def newword():
    global currentint
    while True:
        x = randint(0, 997)
        if x != currentint:
            break
    
    while vs[x] == 1:
        x = randint(0, 997)
        
    global current
    current = ws[x].split("$")
    currentint = x
    clear()
    latinbox.config(text = current[0].split("&")[0])
    
#displays the English of the current word
def english():
    if current is not '':
        englishbox.config(text = "")
    if len(current) > 1:   
        s = ""
        c = current[1].split("&")
        for i in range(len(c) - 1):
            if (i > 0): 
                s = s + ","   
            s = s + c[i]
        
        englishbox.config(text = s)        
    messagebox.config(text = "")      
            
#shows the parts, if any, of the current word          
def parts():
    if current is not '':
        partsbox.config(text = "")
    if len(current) > 1:   
        c = current[0].split("&")
        no = True
        s = ""
        for i in range(1, len(c) - 1):
            if (i > 1):
                s = s + ","   
            s = s + c[i]
            no = False
        if no:    
            partsbox.config(text = '-none')
        else:
            partsbox.config(text = s)    
            
    messagebox.config(text = "")
       
#puts a 1 in vs so the current word won't be shown again 
def doneword():
    global currentint
    global vs
    if currentint != -1:
        vs[currentint] = '1'
        messagebox.config(text = "Done")

#removes all text from the boxes
def clear():
    latinbox.config(text = "")
    englishbox.config(text = "")
    partsbox.config(text = "")
    messagebox.config(text = "")




top = Tk()
saveb = Button(top, text ="save (s)", command = save,)
qb = Button(top, text = "quit (q)", command = q)
newwordb = Button(top, text = "new word (w)", command = newword)    
englishb = Button(top, text = "english (e)", command = english)
partsb = Button(top, text = "parts (p)", command = parts)
donewithwordb = Button(top, text = "Don't show this word (d)", command = doneword)
latinbox = Label(top, height = 1, width = 30, font = ("Times", '12'), bg = 'white')
englishbox = Label(top, height = 3, width = 30, font = ("Times", '12'), bg = 'white', wraplength = 250)
partsbox = Label(top, height = 1, width = 30, font = ("Times", '12'), bg = 'white')
messagebox = Label(top, height = 2, width = 30, font = ("Times", '12'))


latinbox.pack() 
newwordb.pack()
partsbox.pack()
partsb.pack()
englishbox.pack()
englishb.pack() 
donewithwordb.pack()
saveb.pack()
qb.pack()
messagebox.pack()


def key(event):
    c = event.char
    if c == 's':
        save()
    elif c == 'q':
        q()
    elif c == 'w':
        newword()
    elif c == 'e':
        english()
    elif c == 'p':
        parts()
    elif c == 'd':
        doneword()
frame = Frame(top, width=100, height=0,)
frame.bind("<Key>", key)
frame.pack()
frame.focus_set()
top.mainloop()
