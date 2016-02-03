'''

@author: Michael Kleiman
'''


from tkinter import *
from random import *
import os

loc = os.path.join(os.path.dirname(__file__), 'list.txt')
sav = os.path.join(os.path.dirname(__file__), 'save.txt')

current = '' #the current word
currentint = -1 #the location of the current word

#loads a word
def getWord (f):
    t = f.readline()
    st = ""
    while True:
        if "Headword" in t:
            t = t.split(">")
            t = t[2].split("<")
            t = t[0]
            if " " in t:
                t = t.split(" ")
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
        
ws = ['0'] * 1000 #words
vs = ['0'] * 1000 #values

saves = open(sav, "r")

for i in range(0, 1000):
    vs[i] = saves.readline()

saves.close()    


s = " "
i = 0


file = open(loc, "r")
while True:
    s = getWord(file)
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
    for i in range (0, 1000):
        if (vs[i] == 0 or vs[i] == 1):
            saves.write(str(vs[i]))
        else:
            saves.write(str(0))
        
        saves.write('\n')
        
    messagebox.delete(1.0, END)
    saves.close()
    messagebox.insert(INSERT, "saved")
      
#brings up the quit box        
def q():
    messagebox.delete(1.0, END)
    t = Toplevel(width = 10)
    title = Text(t, height = 1, width = 29, font = "Times")
    yes = Button(t, text = "yes", command = leave)
    no = Button(t, text = "no", command = sys.exit)
    
    title.pack()
    title.insert(INSERT, "Do you want to save before quitting?")
    yes.pack()
    no.pack()

#saves then exits
def leave():   
    save()
    sys.exit()
    
#gets a random new word from ws, whose index is a 0 in vs
def newword():
    x = randint(0, 999)
    global current
    current = ws[x].split("$")
    while vs[x] == 1:
        x = randint(0, 999)
    global currentint
    currentint = x
    clear()
    latinbox.insert(INSERT, current[0].split("&")[0])
    
#displays the English of the current word
def english():
    if current is not '':
        englishbox.delete(1.0, END)
    if len(current) > 1:   
        c = current[1].split("&")
        for i in range(len(c) - 1):
            if (i > 0): 
                englishbox.insert(INSERT, ',')   
            englishbox.insert(INSERT,c[i])
    messagebox.delete(1.0, END)        
            
#shows the parts, if any, of the current word          
def parts():
    if current is not '':
        partsbox.delete(1.0, END)
    if len(current) > 1:   
        c = current[0].split("&")
        no = True
        for i in range(1, len(c) - 1):
            if (i > 1):
                partsbox.insert(INSERT, ', ')   
            partsbox.insert(INSERT,c[i])
            
            no = False
        if no:    
            partsbox.insert(INSERT, '-none')
            
    messagebox.delete(1.0, END)
       
#puts a 1 in vs so the current word won't be shown again 
def doneword():
    global currentint
    global vs
    if currentint != -1:
        vs[currentint] = 1
        messagebox.insert(INSERT, "Done")

#removes all text from the boxes
def clear():
    latinbox.delete(1.0, END)
    englishbox.delete(1.0, END)
    partsbox.delete(1.0, END)
    messagebox.delete(1.0, END)




top = Tk()
saveb = Button(top, text ="save (s)", command = save)
qb = Button(top, text = "quit (q)", command = q)
newwordb = Button(top, text = "new word (w)", command = newword)    
englishb = Button(top, text = "english (e)", command = english)
partsb = Button(top, text = "parts (p)", command = parts)
donewithwordb = Button(top, text = "Don't show this word (d)", command = doneword)
latinbox = Text(top, height = 1, width = 25, font = "Times")
englishbox = Text(top, height = 1, width = 25, font = "Times")
partsbox = Text(top, height = 1, width = 25, font = "Times")
messagebox = Text(top, height = 2, width = 25, font = "Times")


 
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
frame = Frame(top, width=100, height=0)
frame.bind("<Key>", key)
frame.pack()
frame.focus_set()
top.mainloop()
