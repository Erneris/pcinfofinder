import socket
from tkinter import *
from tkinter import messagebox
tk = Tk()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
tk.geometry("500x500")

def ip_find():
    messagebox.showinfo( "IP Address", "Your IP address is: " + ip_address)

def host_find():
    messagebox.showinfo( "Host Name", "Your host name is: " + hostname)

ip_button = Button(text="IP Address", command=ip_find)
ip_button.place(x=10, y=0)

host_button = Button(text="Host Name", command=host_find)
host_button.place(x=10, y=50)






















tk.mainloop()