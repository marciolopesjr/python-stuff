from tkinter import * 

root = None 
textBox = None

def buttonPress():
    global entryBox
    txt = textBox.get()
    print ("O conteúdo do form é:", txt)

def createTextBox(parent):
    global textBox
    textBox = Entry(parent)
    textBox.pack()

def main():
    global root
    root =  Tk()

    btn = Button(root, text="Show!", command=buttonPress)
    btn.pack()
    createTextBox(root)
    root.mainloop()

main()
