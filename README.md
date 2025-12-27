# 🛡️ Blue-Jammer Pro: Advanced Bluetooth Intelligence & Auditor

**Blue-Jammer Pro** is a high-performance Bluetooth security auditing framework. It identifies nearby devices, performs vendor lookups, and conducts protocol-level stress testing on Kali Linux.

---

## 🔥 Key Features
- **🔍 Intel Engine:** Instant MAC OUI vendor identification (Apple, Samsung, etc.).
- **📡 Stealth Scan:** Continuous background monitoring for new targets.
- **💥 Hardware Stressing:** L2CAP and SDP flooding capabilities for auditing.
- **💻 Dual-Mode:** Automatic simulation for Windows and raw hardware access for Linux.

---

## 🛠️ Installation & Setup (Kali Linux)

Follow these exact steps to set up the tool:

### 1. Clone the Repository
```bash
git clone [https://github.com/RAJ015HACKING/Blue_jammer.git](https://github.com/RAJ015HACKING/Blue_jammer.git)
```
```bash
cd Blue_jammer
```
### 2. Install Dependencies
Install the required Python modules globally on your system:
```bash
pip3 install -r requirements.txt --break-system-packages
```
(Note: Use --break-system-packages if you are on the latest Kali Linux version).

### 3. Grant Execution Permissions
Make the Linux launcher executable:
```bash
chmod +x Blue_jammer.sh
```
### 4. Launch the Tool
Run the automated launcher to start auditing:
```bash
./Blue_jammer.sh
```
---
## 📂 Project Structure
- blue_jammer.py: Main Python engine.

- Blue_jammer.sh: Automation script for hardware and environment setup.

- requirements.txt: Python dependency list.

- .gitignore: Files excluded from the repository.

## ⚠️ Legal Disclaimer
This tool is strictly for educational and authorized security auditing purposes. Misuse of this tool is illegal. The developer is not responsible for your actions.

## Developed by RAJ015HACKING
