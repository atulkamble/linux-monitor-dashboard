import tkinter as tk
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage
import time

def update_stats():
    cpu_label.config(text=f"CPU Usage: {get_cpu_usage()}%")
    mem_label.config(text=f"Memory Usage: {get_memory_usage()}%")
    disk_label.config(text=f"Disk Usage: {get_disk_usage()}%")
    root.after(1000, update_stats)

root = tk.Tk()
root.title("Linux Monitor Dashboard")

cpu_label = tk.Label(root, text="CPU Usage:")
cpu_label.pack()

mem_label = tk.Label(root, text="Memory Usage:")
mem_label.pack()

disk_label = tk.Label(root, text="Disk Usage:")
disk_label.pack()

update_stats()
root.mainloop()
