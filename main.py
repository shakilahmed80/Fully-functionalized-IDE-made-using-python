## Setting the div
from tkinter import *
compiler = Tk()
compiler.title('Shakils IDE')

def run():
    print('Your Code Will Be Run')

## We need to runbar (5line code)

menu_bar = Menu(compiler)
run_bar =Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command = run)
menu_bar.add_cascade(label = 'Run',menu = run_bar)
compiler.config(menu=menu_bar)

editor = Text()
editor.pack()
compiler.mainloop()



