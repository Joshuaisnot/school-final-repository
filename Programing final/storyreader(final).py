import tkinter as tk
#stores the name of the var
name = "Josh"
# the second window is the thickest due to the story
def reader():
        butName.config(state="disabled")
        global reader
        readerText1 = "Hi "+ str(name) +" how are you? Need a story perchance? I have a short one to tell."
        readerText2 = str(name)+ " your name was once the same as a old hero's.... Yes I am not pulling your leg it is true"
        readerText3 = str(name)+ " Why are you leaving... Hey I am not an old drunk get back here you punk!"
        readerText4 = " ("+str(name)+ " has left the room) Why does no one listen when they are about to say about that area?"
        reader = tk.Toplevel()
        reader.geometry("1000x1000")
        reader.title("Story Time!")
        butExit = tk.Button(reader, text="Close",font = ("Arial",14),command = title.destroy)
        butExit.pack()
        label5 = tk.Label(reader, text=readerText1, font=("Arial",18))
        label5.pack()
        label6 = tk.Label(reader, text=readerText2, font=("Arial",18))
        label6.pack()
        label7 = tk.Label(reader, text=readerText3, font=("Arial",18))
        label7.pack()
        label8 = tk.Label(reader, text=readerText4, font=("Arial",18))
        label8.pack()
# Changes the name var for the inputed str. turning text into a str first thing should prevent security issues
def namer():
        global name
        namesave = name
        name = str(textBox.get())
        if name != "":
                label2.configure(text = name)
                return name
        else:
                name = namesave
        
#title page code
title = tk.Tk()
title.geometry("700x700")
title.title("Storyreader")

butExit = tk.Button(title, text="Exit",font = ("Arial",14),command = title.destroy)
butExit.pack()

label1 = tk.Label(title, text="Enter your name.(optional)", font=("Arial",18))
label1.pack()

textBox = tk.Entry(title)
textBox.pack()

label2 = tk.Label(title, text = "Josh", font=("Arial",18))
label2.pack()

butName = tk.Button(title, text="Change name",font = ("Arial",14),command = namer)
butName.pack()

butReader = tk.Button(title, text="Reader",font = ("Arial",14),command = reader)
butReader.pack()

# image location exact
titleImage1 = tk.PhotoImage(file = "C:/Users/katba/OneDrive/Desktop/Programing final/yellowfield.png")
label3 = tk.Label(title, image= titleImage1)
label3.pack()
# image location exact
readerImage2 = tk.PhotoImage(file = "C:/Users/katba/OneDrive/Desktop/Programing final/greenfield.png")
label4 = tk.Label(title, image= readerImage2)
label4.pack()

title.mainloop



#The link to the GitHub repository for your final project. 
