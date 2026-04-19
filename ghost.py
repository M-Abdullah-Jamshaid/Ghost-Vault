import os, sys, time, shutil, ctypes, json, subprocess, base64
import win32clipboard
import tkinter as tk
from tkinter import filedialog
from getmac import get_mac_address
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# ==========================================
# 0. UNIVERSAL PATH & CONFIG
# ==========================================
def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_path()
CONFIG_FILE = os.path.join(BASE_DIR, "ghost_config.json")
CONFIG_DATA = {}

# ==========================================
# 1. SETUP & HARDWARE BINDING
# ==========================================
def load_config():
    global CONFIG_DATA
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                CONFIG_DATA = json.load(f)
            return True
        except: return False
    return False

def first_run_setup():
    if os.name == 'nt': os.system('color 0A'); os.system('cls')
    print("\n" + "█"*60)
    print(" ██ [!] GHOST-VAULT: SYSTEM INITIALIZATION PROTOCOL ██")
    print("█"*60)
    
    current_mac = get_mac_address().lower()
    print(f"\n [+] Scanning Hardware... \n [✓] Machine Bound to HWID: {current_mac}")
    
    while True:
        pwd = input("\n root@ghost-vault:~# Create Master Password (min 4 chars): ").strip()
        if len(pwd) >= 4: 
            break
        print(" [x] FATAL ERROR: Password too weak! Must be at least 4 characters.")
    
    global CONFIG_DATA
    CONFIG_DATA = {"mac_address": current_mac, "password": pwd}
    
    ctypes.windll.kernel32.SetFileAttributesW(CONFIG_FILE, 128)
    with open(CONFIG_FILE, "w") as f: json.dump(CONFIG_DATA, f)
    ctypes.windll.kernel32.SetFileAttributesW(CONFIG_FILE, 0x02 | 0x04)
    print("\n [✓] SECURITY OVERRIDE ACCEPTED. System Ready.")
    time.sleep(2)

def print_banner():
    if os.name == 'nt': os.system('color 0A'); os.system('cls')
    banner = """
    ===============================================================
         .-.
       -(o o)-    G H O S T - V A U L T   v14.0
         \=/      ADVANCED CRYPTOGRAPHIC SENTRY
        .-"-.     BY: ABDULLAH JAMSHAID
       //| |\\\\
      _//| |\\\\_   [ SYSTEM STATUS: SECURE & ACTIVE ]
     '-- '--' '--
    ===============================================================
    """
    print(banner)

# ==========================================
# 2. CRYPTOGRAPHY ENGINE (IMAGES & FOLDERS)
# ==========================================
def get_master_key():
    salt = b"ghost_vault_secure_salt_786"
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    key = base64.urlsafe_b64encode(kdf.derive(CONFIG_DATA["password"].encode()))
    return Fernet(key)

def process_image(image_path, mode):
    f = get_master_key()
    try:
        with open(image_path, "rb") as file: data = file.read()
        
        if mode == "encrypt":
            processed = f.encrypt(data)
            print("\n [██████████] 100%")
            print(" [✓] IMAGE SECURED! Encryption Matrix Applied.")
        else:
            processed = f.decrypt(data)
            print("\n [██████████] 100%")
            print(" [✓] ACCESS GRANTED! Image Successfully Decrypted.")
            
        with open(image_path, "wb") as file: file.write(processed)
    except Exception as e:
        print("\n [x] CRITICAL ERROR: File corrupted or unauthorized decryption attempt!")

def seal_folder(path):
    f = Fernet(Fernet.generate_key())
    for root, _, files in os.walk(path):
        for file in files:
            fp = os.path.join(root, file)
            try:
                with open(fp, "rb") as bf: d = bf.read()
                with open(fp, "wb") as bf: bf.write(f.encrypt(d))
            except: pass
    ctypes.windll.kernel32.SetFileAttributesW(path, 0x02 | 0x04) # Hidden + System

# ==========================================
# 3. HACKER GUI COMPONENTS (UPGRADED)
# ==========================================
def select_file_gui(title="Select File", is_folder=False):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    if is_folder:
        path = filedialog.askdirectory(title=title)
    else:
        path = filedialog.askopenfilename(title=title, filetypes=[("Images & Files", "*.*")])
    root.destroy()
    return path

class ImageAuthGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.configure(bg="#050505") # Deep Hacker Black
        
        w, h = 500, 300
        ws, hs = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry(f'{w}x{h}+{int(ws/2 - w/2)}+{int(hs/2 - h/2)}')
        
        # Neon Green Border Frame
        self.frame = tk.Frame(self.root, bg="#000000", highlightbackground="#00FF41", highlightthickness=2)
        self.frame.pack(expand=True, fill="both", padx=2, pady=2)
        
        # Header / Logo
        tk.Label(self.frame, text="☠ GHOST DECRYPTION PROTOCOL ☠", fg="#00FF41", bg="black", font=("Consolas", 16, "bold")).pack(pady=(20, 5))
        tk.Label(self.frame, text="RESTRICTED AREA. ENCRYPTED PAYLOAD.", fg="red", bg="black", font=("Consolas", 10, "bold")).pack()
        
        tk.Label(self.frame, text="Enter Master Authentication Key:", fg="white", bg="black", font=("Consolas", 11)).pack(pady=(20, 5))
        
        # Input Box
        self.entry = tk.Entry(self.frame, show="*", bg="#0D0D0D", fg="#00FF41", font=("Consolas", 16, "bold"), insertbackground="#00FF41", justify="center", relief=tk.SOLID, bd=1)
        self.entry.pack(pady=10, padx=50, fill="x")
        self.entry.focus()
        self.entry.bind('<Return>', self.validate)
        
        # Status Label
        self.status_lbl = tk.Label(self.frame, text="[ AWAITING INPUT ]", fg="yellow", bg="black", font=("Consolas", 10))
        self.status_lbl.pack(pady=10)
        
        self.success = False
        self.root.mainloop()

    def validate(self, e=None):
        if self.entry.get() == CONFIG_DATA.get("password"):
            self.success = True
            self.status_lbl.config(text="[ ACCESS GRANTED. DECRYPTING... ]", fg="#00FF41")
            self.frame.config(highlightbackground="#00FF41")
            self.root.update()
            time.sleep(0.5) # Give a cool half-second delay for realistic feel
            self.root.destroy()
        else:
            self.entry.delete(0, tk.END)
            self.frame.config(highlightbackground="red") # Turn border red on fail
            self.status_lbl.config(text="[ FATAL ERROR: ACCESS DENIED ]", fg="red")
            self.root.update()

# ==========================================
# 4. NUCLEAR SENTRY WORKER
# ==========================================
def nuclear_sentry(target_path):
    while True:
        if get_mac_address().lower() != CONFIG_DATA.get("mac_address"): sys.exit()
        try:
            win32clipboard.OpenClipboard()
            if win32clipboard.IsClipboardFormatAvailable(15):
                files = win32clipboard.GetClipboardData(15)
                win32clipboard.CloseClipboard()
                for f in files:
                    if os.path.abspath(target_path).lower() in f.lower():
                        # INSTANT NUCLEAR WIPE
                        if os.path.exists(target_path): shutil.rmtree(target_path)
                        sys.exit()
            else: win32clipboard.CloseClipboard()
        except: pass
        time.sleep(1)

# ==========================================
# 5. MAIN MENU & DETACHMENT
# ==========================================
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--worker":
        load_config()
        nuclear_sentry(sys.argv[2])
        sys.exit()

    if not load_config(): first_run_setup()
    load_config()
    
    while True:
        print_banner()
        print(" [+] SELECT TARGET MODULE:")
        print("     [1] DEPLOY NUCLEAR SENTRY (Folder Guard)")
        print("     [2] ENCRYPT IMAGE (File Guard)")
        print("     [3] DECRYPT IMAGE (Access Payload)")
        print("     [4] EXIT TERMINAL")
        
        choice = input("\n root@ghost-vault:~# ").strip()
        
        if choice == "1":
            print("\n [*] Launching File Explorer UI...")
            path = select_file_gui("Select Folder to Protect", is_folder=True)
            if path:
                print(f" [+] Locking Target: {path}")
                seal_folder(path)
                
                # VBScript Detachment
                vbs_path = os.path.join(BASE_DIR, "launch.vbs")
                if getattr(sys, 'frozen', False):
                    worker_cmd = f'"{sys.executable}" --worker "{path}"'
                else:
                    worker_cmd = f'python "{os.path.abspath(__file__)}" --worker "{path}"'
                
                escaped_cmd = worker_cmd.replace('"', '""')
                with open(vbs_path, "w") as v:
                    v.write(f'CreateObject("WScript.Shell").Run "{escaped_cmd}", 0, False')
                
                os.startfile(vbs_path)
                time.sleep(1)
                if os.path.exists(vbs_path): os.remove(vbs_path)
                
                print("\n [██████████] 100%")
                print(" [✓] NUCLEAR SENTRY DEPLOYED & DETACHED.")
                print(" [!] You may now safely terminate this console.")
                input("\n Press [ENTER] to continue...")
                
        elif choice == "2":
            print("\n [*] Launching File Explorer UI...")
            path = select_file_gui("Select Image to Encrypt")
            if path:
                process_image(path, "encrypt")
                input("\n Press [ENTER] to continue...")
                
        elif choice == "3":
            print("\n [*] Launching File Explorer UI...")
            path = select_file_gui("Select Image to Decrypt")
            if path:
                # Launch GUI for Password
                auth = ImageAuthGUI()
                if auth.success:
                    process_image(path, "decrypt")
                else:
                    print("\n [x] AUTHENTICATION FAILED. DECRYPTION ABORTED.")
                input("\n Press [ENTER] to continue...")
                
        elif choice == "4":
            print("\n [!] Terminating Ghost-Vault Protocol...")
            time.sleep(1)
            sys.exit()