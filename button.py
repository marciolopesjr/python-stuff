from tkinter import * 

root = None 

def buttonPressed():
    global root 
    root.destroy()

def main():
    global root
    root = Tk()
    w = Label(root, text="Hello!")
    w.pack()

    btn = Button(root, text="Exit", command=buttonPressed)
    btn.pack()
    root.mainloop()

main()
