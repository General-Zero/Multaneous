import subprocess
import requests

def tempc(c: int = None, f: int = None, cboth: bool = None):
  if c is not None:
    fc = (c * 9/5) + 32
    r = str(fc) + "°F"
    return r
  elif f is not None:
    cc = (f - 32) * 5/9
    r = str(cc) + "°C"
    return r
  else:
    print('No temperature is given, please provide one.')
    return
def emailvalidate(emailn: str, mailprovider: str):
  emailn = emailn.lower()
  mailprovider = mailprovider.lower()
  mailproviders = {
    "gmail": "@gmail.com",
    "yahoo": "@yahoo.com",
    "outlook": "@outlook.com",
    "mail": "@mail.com",
    "icloud": "@icloud.com",
    "protonmail": "@protonmail.com",
    "zoho": "@zoho.com"
  }
  if mailprovider in mailproviders:
    r = emailn + mailproviders[mailprovider]
    print(r)
  else:
    print("Invalid email name or mailprovider.")
    return
def RHTTPServer(host: str = "127.0.0.1", port: int = 8000, debug: bool = False):
    subprocess.run([f"python", "-m", "http.server", str(port), "--bind", host])
    print(f"Server running on {host}:{port}\nDebug={debug}")
