import subprocess
import time

def scan_wifi():
    try:
        result = subprocess.check_output(args=['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'])
        data = result.decode('utf-8').strip().split('\n')

        print("\n🔄 WLAN-Scan gestartet:")
        for line in data:
            if ':' in line:
                active, ssid = line.split(':', 1)
                if active == "ja":
                    print(f"✅ Verbunden mit: {ssid}")
                else:
                    print(f"📡 Gefunden: {ssid}")
    except subprocess.CalledProcessError as e:
        print("⚠️ Fehler beim WLAN-Scan:", e)

if __name__ == "__main__":
    while True:
        scan_wifi()
        time.sleep(10)
