import tkinter as tk

def reader():
	global reader
	reader = tk.Toplevel()
	reader.geometry("1000x1000")
	reader.title("Story Time!")


def quit():
	reader.quit

title = tk.Tk()
title.geometry("700x700")
title.title("Storyreader")
butexit = tk.Button(title, text="Exit",font = ("Arial",14),command = quit)
butexit.pack()

butreader = tk.Button(title, text="Reader",font = ("Arial",14),command = reader)
butreader.pack()


#reader = tk.Tk()
#reader.geometry("1000x1000")
#reader.title("Story Time!")


title.mainloop