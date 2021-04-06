from Crypto.Cipher import AES
from random import randrange
from random import shuffle
from secret import flag1, flag2
import string
from hashlib import md5


ALPHABET = string.hexdigits[:-6]
ALPHABET_ALL = string.ascii_lowercase + \
    string.ascii_uppercase + string.digits


def plus(num1, num2):
    res = 0
    for i in range(4):
        tmp = (((num1 & 1) + (num2 & 1)) % 2)
        tmp = tmp << i
        res += tmp
        num1 >>= 1
        num2 >>= 1
    return res


def encrypt(msg, key, s):
    c = ''
    for i in msg:
        c_i = key[plus(key.index(i), s)]
        c += c_i
        s = key.index(i)
    return c


k = list(ALPHABET)
shuffle(k)
k = 'ca038b6194df72e5'

m = b'Welcome to NepCTF. I have a message for you '.hex() + flag1.hex()
cipher = encrypt(m, k, 7)
print(cipher)
# 93d4466bb2277405eb5265f1943efd76c5f335fab5800afdc4058ad587743555baadd4058cc21ac5e8e2130580043af40ac5e5e8e2133ac58cc66aad5880758cc66aadc46a85dcbbcee8a555dccbccc47cbf

kk = []
kk.append(k)
while len(kk) < 500:
    tmp_k = list(ALPHABET)
    shuffle(tmp_k)
    if encrypt(m, tmp_k, 7) == cipher:
        kk.append(tmp_k)

f = open('out.txt', 'w')

for k in kk:
    iv = b'i\xfd\xd1\xb9\x81U\x87\xde\xdbB\x9b\x1b\x14|\x97\x14'
    secret2 = flag2 + b'\x00' * (16 - (len(flag2) % 16))

    m = b"Hope you enjoy NepCtf"
    m = m + b"\x00" * (16 - (len(m) % 16))

    AES_keys = []
    for i in range(4):
        prefix = ALPHABET_ALL[randrange(0, len(ALPHABET_ALL))] + \
            ALPHABET_ALL[randrange(0, len(ALPHABET_ALL))]
        AES_keys.append(prefix.encode() + ''.join(k).encode() + b'\x00' * 6)

    for subkey in AES_keys:
        cipher = AES.new(subkey, AES.MODE_CBC, IV=iv)
        secret2 = cipher.encrypt(secret2)

    for subkey in AES_keys:
        cipher = AES.new(subkey, AES.MODE_CBC, IV=iv)
        m = cipher.encrypt(m)

    f.write(str((bytes.hex(secret2), bytes.hex(m), md5(
        ''.join(k).encode()).hexdigest())) + '\n')
