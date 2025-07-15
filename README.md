# 📦 `linux-monitor-dashboard` — Full Code

---

## 📁 Final Project Structure:

```
linux-monitor-dashboard/
├── monitor.py
├── gui.py
├── web_ui.py
├── templates/
│   └── dashboard.html
├── static/
├── requirements.txt
├── .gitignore
└── README.md
```
// ec2
```
sudo yum install python -y
sudo yum install python3-tkinter
python3 --version
sudo yum install pip -y
sudo pip install flask 
```
// ubuntu
```
sudo apt install git -y
sudo apt install python -y 
sudo apt install python3-tk
sudo apt install python3-pip 
sudo apt install python3-venv -y  
python3 -m venv flaskenv
source flaskenv/bin/activate

pip3 install flask
pip install -r requirements.txt

git clone https://github.com/atulkamble/linux-monitor-dashboard.git
cd linux-monitor-dashboard
```

---

## 📜 monitor.py

```python
import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_string = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    return uptime_string
```

---

## 📺 gui.py (Tkinter GUI)

```python
import tkinter as tk
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_uptime

def update_stats():
    cpu_label.config(text=f"CPU Usage: {get_cpu_usage()}%")
    mem_label.config(text=f"Memory Usage: {get_memory_usage()}%")
    disk_label.config(text=f"Disk Usage: {get_disk_usage()}%")
    uptime_label.config(text=f"Uptime: {get_uptime()}")
    root.after(1000, update_stats)

root = tk.Tk()
root.title("Linux Monitor Dashboard")
root.geometry("300x200")

cpu_label = tk.Label(root, text="CPU Usage:", font=("Helvetica", 12))
cpu_label.pack(pady=5)

mem_label = tk.Label(root, text="Memory Usage:", font=("Helvetica", 12))
mem_label.pack(pady=5)

disk_label = tk.Label(root, text="Disk Usage:", font=("Helvetica", 12))
disk_label.pack(pady=5)

uptime_label = tk.Label(root, text="Uptime:", font=("Helvetica", 12))
uptime_label.pack(pady=5)

update_stats()
root.mainloop()
```

---

## 🌐 web\_ui.py (Flask Web Dashboard)

```python
from flask import Flask, render_template
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_uptime

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html',
                           cpu=get_cpu_usage(),
                           memory=get_memory_usage(),
                           disk=get_disk_usage(),
                           uptime=get_uptime())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## 📄 templates/dashboard.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>Linux Monitor Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
    h1 { color: #333; }
    p { font-size: 20px; }
  </style>
</head>
<body>
  <h1>Linux System Monitoring Dashboard</h1>
  <p>CPU Usage: {{ cpu }}%</p>
  <p>Memory Usage: {{ memory }}%</p>
  <p>Disk Usage: {{ disk }}%</p>
  <p>Uptime: {{ uptime }}</p>
</body>
</html>
```

---

## 📦 requirements.txt

```
Flask>=2.0
psutil
```

---

## 📄 .gitignore

```
__pycache__/
*.pyc
.env
```

---

## 📖 README.md

```markdown
# 📦 Linux System Monitoring Dashboard

A simple Linux system monitoring tool with both a desktop GUI and web-based dashboard.

---

## 📊 Features:
- CPU usage
- Memory usage
- Disk space
- System uptime

---

## 📁 Project Structure:
```

linux-monitor-dashboard/
├── monitor.py
├── gui.py
├── web\_ui.py
├── templates/
│   └── dashboard.html
├── static/
├── requirements.txt
├── .gitignore
└── README.md

````

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
````

---

## 📺 Run Desktop GUI

```bash
python gui.py
```

---

## 🌐 Run Web Dashboard

```bash
python web_ui.py
```

Visit `http://localhost:5000` in your browser.

---

## ⭐ Enhancement Ideas:

* Add running process monitor
* Log viewer for /var/log
* Real-time charts using Chart.js
* Network usage stats
* Service status checker

---

## 📌 Tested on:

* Amazon Linux 2 EC2
* Ubuntu 22.04
* Python 3.8+

```
---
## 👨‍💻 Author

**Atul Kamble**

- 💼 [LinkedIn](https://www.linkedin.com/in/atuljkamble)
- 🐙 [GitHub](https://github.com/atulkamble)
- 🐦 [X](https://x.com/Atul_Kamble)
- 📷 [Instagram](https://www.instagram.com/atuljkamble)
- 🌐 [Website](https://www.atulkamble.in)
