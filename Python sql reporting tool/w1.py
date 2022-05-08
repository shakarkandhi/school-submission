import tkinter as tk
def cmd():
    win2=tk.Tk()
    w1=tk.Button(win2,text='W2',command=cmd).grid(row=0,column=0)
    win2.mainloop()
main=tk.Tk()
main.title('Window1')
w1=tk.Button(main,text='W1',command=cmd).grid(row=0,column=0)
main.mainloop()
