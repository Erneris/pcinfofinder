from psutil import virtual_memory
import cpuinfo
import socket
from tkinter import *
from tkinter import messagebox
tk = Tk()
tk.geometry("500x500")
tk.wm_iconbitmap('icons/icon.ico')
tk.title("PC Info Finder 0.3.0")
hostname = socket.gethostname()

def ip_find():
    ip_address = socket.gethostbyname(hostname)
    messagebox.showinfo("IP Address", "Your IP address is: " + ip_address)

def cpu_find():
    cpu_name = cpuinfo.get_cpu_info()["brand_raw"]
    messagebox.showinfo("CPU Name", "Your processor name is: " + cpu_name)

def ram_find():
    ram_bytes = virtual_memory()
    used_gb = round(ram_bytes.total / 1073741824)
    ram_gb = str(used_gb)
    messagebox.showinfo("RAM Number", "You have: " + ram_gb + "GB of RAM")

def host_find():
    messagebox.showinfo("Host Name", "Your host name is: " + hostname)


ip_button = Button(text="IP Address", command=ip_find, width = 15)
ip_button.place(x=10, y=10)

host_button = Button(text="Host Name", command=host_find, width = 15)
host_button.place(x=10, y=60)

cpu_button = Button(text="CPU Name", command=cpu_find, width = 15)
cpu_button.place(x=10, y=110)

ram_button = Button(text="RAM Number", command=ram_find, width = 15)
ram_button.place(x=10, y=160)










tk.mainloop()