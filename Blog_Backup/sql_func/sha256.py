import binascii
import hashlib
import os

# 学习字节串 16进制
def know_hash():
    # 字节串
    salt = b"\xe5\x2b\x46"
    #salt = b"\xe5+F"
    # 字节码 #\xe5+F在完整的字节串表示中应该是\xe5\x2b\x46 #print转换成了ASCII码
    print(f"salt:{salt}")
    # 字节码 hexlify显示为16进制
    print(f"salt:{binascii.hexlify(salt)}")
    # 字符码
    print(f"salt:{binascii.hexlify(salt).decode('utf-8')}")
    # 十六进制 字符码 转 字节串
    print(binascii.unhexlify("e52b46"))  # b'\xe5+F'
    # 字符码 转 字节串 并hexlify显示为16进制
    print(binascii.hexlify("+".encode('utf-8')))

def unhash_password(password):
    # 创建一个随机的盐值
    salt = "1".encode('utf-8')
    # 十六进制 字符码
    print(f"salt:{binascii.hexlify(salt).decode('utf-8')}")

    # 使用sha256哈希函数和盐值对密码进行哈希
    key = hashlib.pbkdf2_hmac('sha256', password, salt, 1)
    print(f"key:{binascii.hexlify(key).decode('utf-8')}")

    # 存储盐值和哈希值
    storage = salt + key
    return storage

def hash_password(password):
    # 创建一个随机的盐值
    #salt = os.urandom(32)
    salt = "IamSB".encode('utf-8')
    print(f"salt:{binascii.hexlify(salt).decode('utf-8')}")

    # 使用sha256哈希函数和盐值对密码进行哈希
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 2)
    print(f"key:{binascii.hexlify(key).decode('utf-8')}")

    # 存储盐值和哈希值
    #storage = salt + key

    return key

know_hash()
hash_password("1")
