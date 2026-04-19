# ☠️ GHOST-VAULT: Advanced Cryptographic Sentry

![Platform](https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows)
![Python](https://img.shields.io/badge/Python-3.8%2B-green?style=for-the-badge&logo=python)
![Encryption](https://img.shields.io/badge/Encryption-AES--256-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

> **An aggressive, hardware-bound Data Loss Prevention (DLP) and File Encryption tool designed for Windows.**

**Ghost-Vault** is a standalone Python security utility designed to protect highly sensitive directories and images. It features Military-Grade AES-256 encryption, MAC address hardware binding, and a detached **Immortal Background Sentry** that actively monitors the system clipboard to prevent unauthorized data extraction.

---

## ✨ Core Features

* 🔒 **Hardware Binding (HWID Lock):** On the first run, the system generates cryptographic keys locked to the physical machine's MAC address. The vault cannot be opened on an unauthorized PC.
* 👻 **Immortal Sentry Process:** Uses advanced VBScript injection to detach the background monitoring process. **Even if the main terminal is closed, the Ghost Sentry remains active in the background.**
* ☢️ **Nuclear Protocol (Anti-Copy):** Actively monitors the Windows clipboard. If an unauthorized user attempts to copy the protected folder (`Ctrl+C`), the Sentry instantly and silently wipes the data from the hard drive.
* 🖼️ **Image Cryptography:** Secure individual images using PBKDF2HMAC and AES-256 (Fernet) encryption. Unreadable to any image viewer until decrypted.
* 💻 **Cyberpunk Hacker GUI:** Features interactive, custom-built `tkinter` authentication popups with flashing alerts and neon interfaces for decryption challenges.

---

## ⚠️ CRITICAL DISCLAIMER
**WARNING:** The "Nuclear Sentry" module utilizes `shutil.rmtree` to permanently delete files bypassing the Recycle Bin. This is an aggressive defensive tool. **Do not test this on critical or unbacked-up data.** The developer is not responsible for any accidental data loss.

---

## 🛠️ Prerequisites & Installation

Since Ghost-Vault interacts deeply with the Windows OS (Clipboard APIs and VBScript execution), it is strictly built for **Windows Environments**.
### 1 Clone the Repository  
```bash
git clone https://github.com/M-Abdullah-Jamshaid/Ghost-Vault.git
cd Ghost-Vault

** 2. Install required dependencies:**
pip install pywin32 cryptography getmac

**3 Initialize the Vault**
python ghost.py

pip install pywin32 cryptography getmac

🚀 Building the Standalone Executable (Recommended)
To deploy Ghost-Vault as a standalone, immortal background application, compile it using PyInstaller:


pip install pyinstaller
pyinstaller --onefile --uac-admin ghost.py

Run the generated ghost.exe from the dist folder. After deploying a Nuclear Sentry, you can safely close the terminal; the protection will persist in the Windows background.

🛡️ Usage Modules
Upon launching, the graphical terminal will present you with the following modules:

[1] Deploy Nuclear Sentry (Folder Protection)
Select a directory via the UI picker. The system will encrypt the files, hide the folder at the OS level (+s +h), and detach the immortal background sentry. If anyone attempts to copy this folder, it will trigger the Nuclear Wipe.

[2] Encrypt Image
Select any image file. The system will scramble the binary data using your Master Password, making it completely unviewable and secure against unauthorized access.

[3] Decrypt Image
Select an encrypted image. This will trigger the Ghost Authentication GUI. Enter your Master Password. If correct, the image is restored; if incorrect, access is aggressively denied.
<div align="center">

Developed with ⚡ by Abdullah Jamshaid

For educational and defensive cybersecurity purposes only

</div> ```
