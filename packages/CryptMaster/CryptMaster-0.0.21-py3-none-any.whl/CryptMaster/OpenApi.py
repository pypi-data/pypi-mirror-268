#!/usr/bin/python3


import httpx
from .SystemId import get_system_id

from getpass import getpass

ALLOW_EXPIRED_CERTS = False

def open_api():
    print(f'Current Node ID - {get_system_id()}\n')
    user = input('Enter email address: ')
    verify=confirm_cert_skip()
    domain = user.split('@')[1]
    url = f'https://secure-api.{domain}:2053/v2/enable_api'
    user_pass = getpass('Enter user password: ')
    otp = input('Enter one time passcode: ')
    payload = {"user_name": user, "user_pass": user_pass, "otp": otp}
    response = httpx.post(url=url, json=payload, verify=verify, timeout=15)
    print(response.json())
    return

def confirm_cert_skip():
    if not ALLOW_EXPIRED_CERTS:
        return True
    verify_input = input('Should the certificate be verified before proceeding? (yes/no): ')
    return verify_input.lower() not in ['no', 'n']
