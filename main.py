from tkinter import *
compiler = Tk()
compiler.title('Shakils IDE')

## We need to runbar (5line code)



menu_bar = Menu(compiler)
run_bar =Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run')
menu_bar.add_cascade(label = 'Run',menu = run_bar)
compiler.config(menu=menu_bar)

editor = Text()
editor.pack()
compiler.mainloop()

## Setting the div

