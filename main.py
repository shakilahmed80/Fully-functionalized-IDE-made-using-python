from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilenames, askopenfilename

compiler = Tk()
compiler.title('Shakils IDE')
file_path = ''

def set_file_path(path):
    
    global file_path 
    file_path = path


def open_file():
    path = askopenfilename(filetypes = [('Python Files ', '*.py')])
    with open (path,'r') as file :
         code = file.read()
         editor.delete('1.0',END)
         editor.insert('1.0',code)
         set_file_path(path)

def save_as():
    
    if file_path == '' :

        path = asksaveasfilename(filetypes = [('Python Files ', '*.py')])
    
    else :
        path = file_path
    
    with open (path,'w') as file :
         code = editor.get('1.0',END)
         file.write(code)


def run():
    code = editor.get('1.0',END)
    exec (code)
    print('Your Code Will Be Run')


menu_bar = Menu(compiler)


file_bar =Menu(menu_bar,tearoff=0)
file_bar.add_command(label='Open File',command = open_file)
file_bar.add_command(label='Open Folder',command = run)
file_bar.add_command(label='Save',command = save_as)
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



