# Web-Based Automated Reconnaissance Tool

A browser-based security reconnaissance platform built with Python and Django.
Automates information gathering tasks like port scanning, directory brute-forcing,
and HTTP security header analysis through a user-friendly web interface.

---

## Features

- Port scanning and service fingerprinting
- Directory brute-force enumeration
- HTTP security header analysis
- Multi-user authentication and session management
- Scan history and result storage
- Report generation (HTML / text format)

---

## Tech Stack

Python · Django · SQLite · Nmap · HTML · CSS

---

## Requirements

- Python 3.x
- Django
- Nmap installed on your system

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/Automated-Reconnaissance-Tool.git
cd recon-tool
```

**2. Create and activate virtual environment**
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up the database**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Create admin user (optional)**
```bash
python manage.py createsuperuser
```

**6. Run the server**
```bash
python manage.py runserver
```

**7. Open in browser**
```
http://127.0.0.1:8000
```

---

## Project Modules

| Module | Description |
|---|---|
| User Authentication | Registration, login, logout, session management |
| Scan Management | Create and manage scans by target |
| Port Scanning | Identifies open ports on target system |
| Service Detection | Detects running services and versions |
| Directory Brute Force | Enumerates hidden directories using wordlists |
| Security Header Analysis | Checks for missing HTTP security headers |
| Result Storage | Stores scan results in database |


---


## Author

**Aditya Suresh Ujgaonkar**  
[LinkedIn](https://www.linkedin.com/in/adityaujgaonkar) · [TryHackMe](https://tryhackme.com/p/Adyt3ch)
