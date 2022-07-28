from cgitb import text
import imp
from ttkwidgets.font import askfont
import tkinter
from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename
from click import command, edit
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo

def Copy():
    textArea.event_generate(("<<Copy>>"))
    
def Cut():
    textArea.event_generate(("<<Cut>>"))

def Paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Learn Gui programming using tkinter with code with Aditya")

def exit():
    top.destroy()

def open_file():
    filetype = [("text files","*.txt"),("All files","*.*")]
    file = askopenfilename(filetypes=filetype)

    if not file:
        return

    textArea.delete(1.0, END)
    with open(file, "r") as input_file:
        text = input_file.read()
        textArea.insert(END,text)
    top.title(f"{file} - notepad by aditya")  


def save_file():
    filetype = [("text files","*.txt"),("All files","*.*")]
    filetype = asksaveasfilename(defaultextension="txt",filetypes=filetype)   
    if not file:
        return
        
    with open(file,"w") as output_file:
        text = textArea.get(1.0, END)  
        output_file.write(text)
    top.title(f"{file} - notpad by aditya")  


def  changeFont():
    font = askfont()
    if font[0] is not None:
        textArea.config(font=font[0])
    
            

top = Tk()
top.geometry("400x500")
top.title("adi software")

menubar = Menu(top)

filemenu = Menu(menubar,tearoff=0)
editmenu = Menu(menubar,tearoff=0)
formatmenu = Menu(menubar,tearoff=0)
viewmenu = Menu(menubar,tearoff=0)
helpmenu = Menu(menubar,tearoff=0)


filemenu.add_command(label="New                                        Ctrl+N")
filemenu.add_command(label="New Window              Ctrl+Shift+N")
filemenu.add_command(label="Open                                       Ctrl+O",command=open_file)
filemenu.add_command(label="Save                                         Ctrl+S", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Save As...                      Ctrl+Shift+S")
filemenu.add_command(label='underline')
filemenu.add_command(label="Page Setup...")
filemenu.add_command(label="Print                                         Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit)


editmenu.add_command(label="Undo                                   Ctrl+Z")
editmenu.add_separator()
editmenu.add_command(label="Cut                                      Ctrl+X",command=Cut)
editmenu.add_command(label="Copy                                   Ctrl+C",command=Copy)
editmenu.add_command(label="Paste                                   Ctrl+V",command=Paste)
editmenu.add_command(label="Delete                                       Del")
editmenu.add_separator()
editmenu.add_command(label="Search with Bing...             Ctrl+E")
editmenu.add_command(label="Find...                                   Ctrl+F")
editmenu.add_command(label="Find Next                                   F3")
editmenu.add_command(label="Find Previous                  Shift+F3")
editmenu.add_command(label="Replace                              Ctrl+H")
editmenu.add_command(label="Go To...                               Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All                             Ctrl+A")
editmenu.add_command(label="Time/Date                                  F5")

formatmenu.add_command(label="word wrap")
formatmenu.add_command(label="font",command=changeFont)


viewmenu.add_command(label="   zoom                       >")
viewmenu.add_command(label="   status bar")

helpmenu.add_command(label="   view help")
helpmenu.add_command(label="   send feedback")
helpmenu.add_separator()
helpmenu.add_command(label="   About notepad")




menubar.add_cascade(label="file",menu=filemenu)
menubar.add_cascade(label="edit",menu=editmenu)
menubar.add_cascade(label="format",menu=formatmenu)
menubar.add_cascade(label="view",menu=viewmenu)
menubar.add_cascade(label="help",menu=helpmenu)



textArea = Text(top)
textArea.pack(expand=True,fill=BOTH)

sb = Scrollbar(textArea)
sb.pack(side=RIGHT,fill=Y)
sb.config(command=textArea.yview)
textArea.config(yscrollcommand=sb.set)



top.config(menu=menubar)
top.mainloop()