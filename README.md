# ☠️ GHOST-VAULT: Advanced Cryptographic Sentry

> **An advanced, hardware-bound Data Loss Prevention (DLP) and Encryption tool for Windows.**

Ghost-Vault is a standalone Python security tool designed to protect highly sensitive directories and images. It features AES-256 encryption, MAC address hardware binding, and a detached, immortal background sentry process that actively monitors the system clipboard for unauthorized data extraction.

## ✨ Features
* **Hardware Binding:** Locks the cryptographic keys to the physical machine's MAC address on the first run.
* **Immortal Sentry Process:** Uses VBScript detachment to keep monitoring the clipboard even if the main terminal is closed.
* **Nuclear Mode:** Instantly and silently deletes the protected folder if an unauthorized copy attempt is detected.
* **Hacker-Themed GUI:** Features an interactive, cyberpunk-styled `tkinter` authentication popup for decryption and timer-based challenges.
* **File & Folder Encryption:** Uses PBKDF2HMAC and AES-256 (Fernet) to completely scramble images and directories.

## ⚠️ Disclaimer
**WARNING:** The "Nuclear Mode" utilizes `shutil.rmtree` to permanently delete files without sending them to the Recycle Bin. This is an aggressive DLP tool. **Do not test this on critical or unbacked-up data.** The author is not responsible for any accidental data loss.

## 🛠️ Prerequisites
* Python 3.8+
* Windows OS (Required for Win32 API clipboard monitoring and VBScript detachment)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Ghost-Vault.git](https://github.com/YOUR_USERNAME/Ghost-Vault.git)

cd Ghost-Vault
Install dependencies:

Bash
pip install -r requirements.txt
Run the Initialization Protocol:

Bash
python ghost.py
On the first run, the system will bind to your hardware and prompt you to create a Master Sentry Password.

💻 Building the Executable
To deploy this as a standalone, immortal background application, compile it using PyInstaller:

Bash
pip install pyinstaller
pyinstaller --onefile --uac-admin ghost.py
(Run the generated ghost.exe from the dist folder. You can safely close the terminal after deploying a Sentry; it will persist in the background).

🛡️ Usage Modules
[1] Deploy Nuclear Sentry: Select a folder to hide, encrypt, and actively guard against copying.

[2] Encrypt Image: Select a single image to lock with AES-256.

[3] Decrypt Image: Unlocks a secured image (Triggers the Hacker Authentication GUI).