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
def emailvalidate(email: str, mailprovider: str):
  email = email.lowercase()
  mailprovider = mailprovider.lowercase()
  mailproviders = {
    "gmail": "@gmail.com",
    "yahoo": "@yahoo.com",
    "outlook": "@outlook.com",
    "mail": "@mail.com",
    "icloud": "@icloud.com",
    "protonmail": "@protonmail.com",
    "zoho": "@zoho.com"
  }
  if mailprovider == mailproviders:
    r = email + mailproviders[mailprovider]
    print(r)
  else:
    print("Invalid email or mailprovider.")
    return
