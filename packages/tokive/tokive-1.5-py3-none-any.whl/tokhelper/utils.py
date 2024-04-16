import json
import os
import sqlite3
from cryptography.fernet import Fernet
import base64, hashlib
import string, random, uuid
def check_exists(file_path):
    return os.path.exists(file_path)

def random_text_digit(N):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))

def random_digit(N):
    return ''.join(random.choices(string.digits, k=N))
def random_cid():
    return uuid.uuid4()
def gen_fernet_key(passcode:bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))
def get_data_cookie(path):
    arr_passed = ['passport_csrf_token', 'uid_tt_ss', 'sessionid_ss', 'ssid_ucp_v1', 'msToken']
    cookies = None
    try:
        cookies={}
        sqliteConnection = sqlite3.connect(path)
        cur = sqliteConnection.cursor()
        cur.execute("SELECT name, value FROM cookies WHERE host_key LIKE '%tiktok%'")
        rows = cur.fetchall()
        for key, value in rows:
            cookies[key]=value
            try:
                arr_passed.remove(key)
            except ValueError:
                pass
        cookies = json.dumps(cookies)
    except:
        pass
    if len(arr_passed)>0:
        cookies = None
    return cookies


def encode(path):
    base64_string= ""
    with open(path, "rb") as rf:
        encoded_string = base64.b64encode(rf.read())
        base64_string=encoded_string.decode('utf-8')
    return base64_string
def encrypt_data(message):
    key=gen_fernet_key('base64.b64encode'.encode('utf-8'))
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode('utf-8'))
    base64_string = encMessage.decode('utf-8')
    return base64_string
def decrypt_data(message):
    try:
        key = gen_fernet_key('base64.b64encode'.encode('utf-8'))
        fernet = Fernet(key)
        encMessage = fernet.decrypt(message.encode('utf-8'))
        mess = encMessage.decode('utf-8')
        return mess
    except:
        pass
    return message