import subprocess
import requests

def tempc(c: int = None, f: int = None, cboth: bool = None):
  if c is not None:
    fc = (c * 9/5) + 32
    return fc
  elif f is not None:
    cc = (f - 32) * 5/9
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
def HTTPServer(host: str = 127.0.0.1, port: int = 8000, debug: bool = False):
  print(f"Server running in {host} on port {port}\nDebug={debug}")
  
