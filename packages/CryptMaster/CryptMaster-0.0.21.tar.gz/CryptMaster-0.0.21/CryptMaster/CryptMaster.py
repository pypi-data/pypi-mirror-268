import httpx
import os
import platformdirs
import random


from argon2 import PasswordHasher
from time import sleep
from .SystemId import get_system_id







def get_create_config():
    crypt_file = platformdirs.user_config_dir('.crypt_file')
    if not os.path.isfile(crypt_file):
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        salt = ''
        for i in range(32):
            salt += (random.choice(ALPHABET))
        with open(crypt_file, 'w+') as f:
            f.write(salt)
    with open(crypt_file, 'r') as f:
        crypt_config = f.readline()
    return crypt_config





class CryptMaster:
    def __init__(self, server, port=2053):
        self.SALT = get_create_config()
        self.system_id = get_system_id()
        self.server = f'https://{server}:{port}'

    def get_secret(self, requested_secret):
        url = f'{self.server}/v2/get_secret'
        auth_url = f'{self.server}/v2/start_auth'
        while True:
            payload = {"requested_password": requested_secret, 'system_id': self.system_id}
            response = httpx.post(url=auth_url, json=payload, timeout=5, verify=False)
            if response.status_code != 200:
                print('Did not get a good response') #ToDo - Change response to be more useful
                sleep(20)
                continue
            response = response.json()
            nonce = response.get('nonce', None)
            if nonce == None:
                print('Failed to get auth nonce')
                return
            ph = PasswordHasher()
            payload['auth_response'] = ph.hash(nonce + self.SALT)
            response = httpx.post(url=url, json=payload, timeout=5, verify=False)
            if response.status_code != 200:
                print('Did not get a good response') #ToDo - Change response to be more useful
                sleep(20)
                continue
            response = response.json()
            secret = response.get('secret', None)
            status = response.get('response', None)
            if secret is not None:
                break
            else:
                print(status)
                sleep(20)
                continue
        return secret

    def enroll_server(self):
        payload = {'system_id': self.system_id, 'system_salt': self.SALT}
        url = f'{self.server}/v2/enroll_server'
        response = httpx.post(url=url, json=payload, timeout=5, verify=False)
        #while True:
        #    if response.status_code != 200 or response.status_code != 429:
        #        print('Did not get a good response')
        #        sleep(20)
        #        continue
        #    response = response.json()
        #    status = response.get('response', None)
        #    if status is not None:
        #        break
        #    else:
        #        print('Did not get a good response')
        #        sleep(20)
        #        continue
        status = response.text
        return status



