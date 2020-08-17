import cpuinfo
import socket
from tkinter import *
from tkinter import messagebox
tk = Tk()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
tk.geometry("500x500")
tk.title("PC Info Finder 0.2.1")
cpu_name = cpuinfo.get_cpu_info()["brand_raw"]

def ip_find():
    messagebox.showinfo("IP Address", "Your IP address is: " + ip_address)

def cpu_find():
    messagebox.showinfo("CPU Name", "Your processor name is: " + cpu_name)


def host_find():
    messagebox.showinfo("Host Name", "Your host name is: " + hostname)


ip_button = Button(text="IP Address", command=ip_find)
ip_button.place(x=10, y=0)

host_button = Button(text="Host Name", command=host_find)
host_button.place(x=10, y=50)

cpu_button = Button(text="CPU Name", command=cpu_find)
cpu_button.place(x=10, y=100)












tk.mainloop()