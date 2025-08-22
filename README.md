---

🔹 1. Install Python (latest version)

1. Go to Python Downloads.


2. Download the latest Python 3.x installer for your OS.


3. During installation:

✅ Check "Add Python to PATH".

Click Install Now.



4. Verify installation:

python --version

or

python3 --version




---

🔹 2. Install Google Chrome (latest)

Windows/macOS: Download from Google Chrome and install.

Linux (Debian/Ubuntu):

sudo apt update
sudo apt install -y wget gnupg2
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install -y google-chrome-stable


Check installation:

google-chrome --version


---

🔹 3. Create a Project Folder

mkdir selenium_project
cd selenium_project


---

🔹 4. Create requirements.txt

Inside selenium_project, create a file named requirements.txt with this content:

selenium
undetected-chromedriver


---

🔹 5. Install Dependencies

Run:

pip install -r requirements.txt

Check installation:

pip show selenium undetected-chromedriver


---




Run:

python tiktok.py

👉 This should open Chrome, go to Google, print the title, and close.


---
