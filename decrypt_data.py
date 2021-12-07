import rsa
from cryptography.fernet import Fernet

# load private key untuk mendekripsi public key
prkey = open('privkey.key','rb')
pkey = prkey.read()
private_key = rsa.PrivateKey.load_pkcs1(pkey)

e = open('kunci_enskripsi.txt', 'rb')
ekey = e.read()

dpubkey = rsa.decrypt(ekey,private_key)

cipher = Fernet(dpubkey)

encrypted_data = open('kode_dienkripsi.txt', 'rb')
edata = encrypted_data.read()


decrypted_data = cipher.decrypt(edata)

# mmebuat file baru dari hasil dekripsi
edata = open('hasil_dekripsi.txt', 'wb')
edata.write(decrypted_data)
edata.close()
#


