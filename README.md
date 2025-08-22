
````markdown
# 🚀 Selenium Project Setup Guide

## 🔹 1. Install Python (latest version)

1. Go to [Python Downloads](https://www.python.org/downloads/).  
2. Download the latest Python **3.x installer** for your OS.  
3. During installation:
   - ✅ Check **"Add Python to PATH"**  
   - Click **Install Now**  
4. Verify installation:
   ```bash
   python --version
   # or
   python3 --version
````

---

## 🔹 2. Install Google Chrome (latest)

### Windows/macOS

* Download and install from [Google Chrome](https://www.google.com/chrome/).

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install -y wget gnupg2
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install -y google-chrome-stable
```

Check installation:

```bash
google-chrome --version
```

---

## 🔹 3. Create a Project Folder

```bash
mkdir selenium_project
cd selenium_project
```

---

## 🔹 4. Create `requirements.txt`

Inside `selenium_project`, create a file named `requirements.txt` with this content:

```
selenium
undetected-chromedriver
```

---

## 🔹 5. Install Dependencies

```bash
pip install -r requirements.txt
```

Check installation:

```bash
pip show selenium undetected-chromedriver
```

---

## 🔹 6. Run the Script

Run:

```bash
python tiktok.py
```

👉 This should open Chrome, go to Google, print the title, and close.

```

