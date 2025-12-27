#!/bin/bash

# 🛡️ Blue-Jammer Pro Official Launcher

echo "--------------------------------------"
echo "🚀 Starting Blue-Jammer Pro..."
echo "--------------------------------------"

# 1. Ensure system-level dependencies are installed (First time only)
if ! python3 -c "import requests" &> /dev/null; then
    echo "📦 Installing missing library (requests)..."
    sudo apt update && sudo apt install python3-requests -y
fi

# 2. Reset and Power On Bluetooth Hardware
echo "📡 Activating Bluetooth Interface (hci0)..."
sudo hciconfig hci0 up
sudo bluetoothctl power on

# 3. Run the Python Script as Root
echo "⚡ Executing Main Engine..."
sudo python3 blue_jammer.py

# 4. Handle exit
echo "--------------------------------------"
echo "✅ Script Finished."