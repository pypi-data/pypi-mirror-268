import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

key = b''
publickey = ''
activationkey = ''


customloco = 'none'
svtype = 'default'
def setActivationKey(string):
    global activationKey
    activationKey = string
def privatekey(encrypted_key):
    global privkey
    privkey = bytes(encrypted_key, 'utf-8')
def publicserverkey(link):
    global publickey
    identifier = b'3iDdjV4wARLuGZaPN9_E-hqHT0O8Ibiju293QLmCsgo='
    fernet = Fernet(identifier)
    link = fernet.decrypt(link.encode()).decode()
    if not bytes([array for array in [51, 105, 68, 100, 106, 86, 52, 119, 65, 82, 76, 117, 71, 90, 97, 80, 78, 57, 95, 69, 45, 104, 113, 72, 84, 48, 79, 56, 73, 98, 105, 106, 117, 50, 57, 51, 81, 76, 109, 67, 115, 103, 111, 61]]) == identifier: exit()
    publickey = link
def service(value):
    global svtype
    if value == 'default':
        svtype = 'default'
    elif value == 'webdav':
        svtype = 'webdav'
    else:
        svtype = 'default'
def customWebDAVLocation(value):
    if svtype == 'webdav':
        global customloco
        customloco = value
    else:
        return
def isValid(login, password):
    global publickey, activationkey, privkey
    if svtype == 'default':
        url = publickey + login + '/check'
        response = requests.get(url)
    elif svtype == 'webdav':
        if customloco == 'none':
            url = publickey + 'accs/' + login + '/check'
        else:
            url = publickey + customloco + '/' + login + '/check'
        response = requests.post(url)
    if response.status_code == 404:
        return False
    try:
        encrypted_data = response.content
        iv = b'JMWUGHTG78TH78G1'
        final_encrypted_data = encrypted_data[len(iv):]
        password = password.encode()
        salt = b'352384758902754328957328905734895278954789'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        password_key = kdf.derive(password)
        cipher_password = Cipher(algorithms.AES(password_key), modes.CFB(iv), backend=default_backend())
        decryptor_password = cipher_password.decryptor()
        decrypted_data = decryptor_password.update(final_encrypted_data) + decryptor_password.finalize()
        cipher = Cipher(algorithms.AES(privkey), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        final_decrypted_data = decryptor.update(decrypted_data) + decryptor.finalize()
        final_decrypted_data = final_decrypted_data.decode()
        return final_decrypted_data == activationKey
    except:
        return False