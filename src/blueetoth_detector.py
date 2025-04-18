import subprocess
import time

def bluetooth_scan(duration=10):
    print("🔍 Starte Bluetooth-Scan für", duration, "Sekunden...\n")

    # Starte bluetoothctl
    process = subprocess.Popen(['bluetoothctl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

    process.stdin.write("power on\n")
    process.stdin.write("scan on\n")
    process.stdin.flush()

    time.sleep(duration)

    process.stdin.write("scan off\n")
    process.stdin.write("exit\n")
    process.stdin.flush()

    output, _ = process.communicate()

    seen = set()
    for line in output.splitlines():
        if "Device" in line and "NEW" in line:
            parts = line.strip().split(" ", 3)
            if len(parts) >= 3:
                mac = parts[2]
                name = parts[3] if len(parts) > 3 else "(Unbenannt)"
                if mac not in seen:
                    seen.add(mac)
                    print(f"📡 {name} ({mac})")

bluetooth_scan()
