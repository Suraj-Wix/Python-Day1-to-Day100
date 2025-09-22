
import subprocess

def connect_wifi(ssid, password):
  """Connects to a Wi-Fi network with the given SSID and password."""
  command = f"netsh wlan connect ssid={ssid} name={ssid} interface=Wi-Fi"
  subprocess.run(command, shell=True)

  # You might want to add error handling and password encryption here

if __name__ == "__main__":
  ssid = "YourSSID"
  password = "YourPassword"
  connect_wifi(ssid, password)
