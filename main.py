## Setting the div
from tkinter import *

##this is for pop up save file window and open file name
from tkinter.filedialog import asksaveasfilename, askopenfilenames, askopenfilename

compiler = Tk()
compiler.title('Shakils IDE')

def open_file():
    path = askopenfilename(filetypes = [('Python Files ', '*.py')])
    with open (path,'r') as file :
## here w means that write
         code = file.read()
         editor.delete('1.0',END)

## 1.0 MEANS INDEX 1.0 AND END MEANS TILL THE END OF THE DOCUMENT

         editor.insert('1.0',code)
## code means read form that file
def save_as():
    path = asksaveasfilename(filetypes = [('Python Files ', '*.py')])
    with open (path,'w') as file :
         code = editor.get('1.0',END)
         file.write(code)


def run():
    ## here i am capturing all thing like forloop,whileloop all staff
    code = editor.get('1.0',END)
    exec (code)
    print('Your Code Will Be Run')

## We need to runbar (5line code)

menu_bar = Menu(compiler)


file_bar =Menu(menu_bar,tearoff=0)
file_bar.add_command(label='Open File',command = open_file)
file_bar.add_command(label='Open Folder',command = run)
file_bar.add_command(label='Save',command = run)
file_bar.add_command(label='Save As',command = save_as)
file_bar.add_command(label='Exit',command = exit)
menu_bar.add_cascade(label = 'File',menu = file_bar)



run_bar =Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command = run)
menu_bar.add_cascade(label = 'Run',menu = run_bar)


compiler.config(menu=menu_bar)

editor = Text()
editor.pack()
compiler.mainloop()



