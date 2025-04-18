import subprocess
import time

result = subprocess.check_output([
    'nmcli', '--colors', 'no', '-t', '-f', 'ssid,signal,active', 'dev', 'wifi'
])
data = result.decode('utf-8').strip().split('\n')

# Netzwerke als Liste speichern
networks = []
for line in data:
    if ':' in line:
        parts = line.split(':')
        if len(parts) == 3:
            ssid, signal, active = parts
            try:
                signal_clean = int(signal)
                is_active = active.lower() in ['yes', 'ja']
                networks.append((ssid, signal_clean, is_active))
            except ValueError:
                print(f"⚠️ Fehlerhafte Signalstärke: {signal}")
                
# Nach Signalstärke sortieren
networks.sort(key=lambda x: x[1], reverse=True)

# Ausgabe
print("\n📶 Netzwerke sortiert nach Signalstärke:")
for ssid, signal, is_active in networks:
    status = "✅ Verbunden" if is_active else "📡"
    print(f"{status}: {ssid} ({signal}%)")
