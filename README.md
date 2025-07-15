## 📦 Project: **Linux System Monitoring Dashboard with UI**

---

## 📌 Project Description:

Build a Linux system monitoring tool that gathers real-time system metrics (like CPU usage, memory, disk, running processes, network traffic) and displays them on a **user interface**.
You can choose between:

* **Tkinter GUI app** (desktop)
* **Flask web dashboard** (accessible in browser)

---

## 📊 Features:

✅ CPU usage
✅ Memory usage
✅ Disk space
✅ Running processes
✅ Network traffic stats
✅ System uptime
✅ Log viewer

---

## 📁 Project Structure:

```
linux-monitor/
├── monitor.py             # Backend metrics collection
├── ui.py                  # Tkinter UI or Flask app
├── templates/             # For Flask HTML templates
│   └── dashboard.html
├── static/                # CSS/JS (if Flask)
├── requirements.txt
└── README.md
```

---

## 📜 Backend: monitor.py

**Example (getting CPU and memory usage using `psutil`):**

```python
import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_uptime():
    return psutil.boot_time()
```

Install psutil:

```bash
pip install psutil
```

---

## 📺 Option 1: Tkinter GUI (ui.py)

```python
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
```

---

## 📺 Option 2: Flask Web Dashboard

**templates/dashboard.html**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Linux Monitor</title>
</head>
<body>
  <h1>Linux Monitoring Dashboard</h1>
  <p>CPU Usage: {{ cpu }}%</p>
  <p>Memory Usage: {{ memory }}%</p>
  <p>Disk Usage: {{ disk }}%</p>
</body>
</html>
```

**ui.py**

```python
from flask import Flask, render_template
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html',
                           cpu=get_cpu_usage(),
                           memory=get_memory_usage(),
                           disk=get_disk_usage())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## 📦 requirements.txt

```
Flask
psutil
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📖 README.md

> ### Linux System Monitoring Dashboard
>
> A simple Linux system monitoring tool with a GUI and Web UI option.
>
> **Run GUI**:
>
> ```
> python ui.py
> ```
>
> **Run Web App**:
>
> ```
> python ui.py
> Visit http://localhost:5000
> ```

---

## ✅ How to Deploy (EC2 optional)

On a Linux server:

```bash
sudo yum update -y
sudo yum install python3 -y
pip3 install -r requirements.txt
python3 ui.py
```

---

## ⭐ Enhancement Ideas:

* Add process manager (list & kill processes)
* Real-time charts using Chart.js in Flask
* Log viewer for /var/log/messages
* Network monitoring: bandwidth usage
* Service status check (Apache, MySQL, etc.)

---
