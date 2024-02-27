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

    return binascii.hexlify(key).decode('utf-8')

#know_hash()
#hash_password("2")
#code = b'+'
code = "中国".encode('utf-8')
print(code)
# 字节码转16进制
code_16 = binascii.hexlify(code).decode('utf-8')
# 将16进制字符串转换为数组，每两个字符作为一个元素
code_16_array = [code_16[i:i+2] for i in range(0, len(code_16), 2)]
print(code_16_array)

# 16进制转10进制
code_10_array = [int(item, 16) for item in code_16_array]
print(code_10_array)

# 进制解码网站 https://www.toolhelper.cn/EncodeDecode/ByteArrayEncodeDecode