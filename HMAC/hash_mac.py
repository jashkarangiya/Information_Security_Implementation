# This is the implementation of HMAC
# Submitted by: CSB20047

import des
from des import DesKey


# Function to add zeros at the end of the bytes string
def add_zeros_at_last(a, length):
    while len(a) < length:
        a += b'0'
    return a

# Function to add zeros at the beginning of the bytes string
def add_zeros_at_start(a, length):
    while len(a) < length:
        a = b'0' + a
    return a

# Function for Bitwise XOR
def xor(a, b):
    ans = b""
    if(len(a) != len(b)):
        b = add_zeros_at_start(b, len(a))
    for i in range(len(a)):
        if a[i] == b[i]:
            ans += b"0"
        else:
            ans += b"1"
    return ans

# Function to convert hexadecimal string to binary string
def hex2bin(hex_string):
    binary_string = bin(int(hex_string, 16))[2:]
    return '0' * (4 * len(hex_string) - len(binary_string)) + binary_string

# Function to ensure the key length is 8 bytes
def ensure_key_length(key):
    key_bytes = bytes.fromhex(key.decode('utf-8'))
    while len(key_bytes) < 8:
        key_bytes += key_bytes  # Repeat the key if its length is less than 8 bytes
    return key_bytes[:8]  # Trim the key to 8 bytes if its length is greater than 8

# Function to perform DES encryption
def des_func(data, key):
    # Initialize DES key object
    des_key = DesKey(key)

    # Encrypt the data using DES
    encrypted_data = des_key.encrypt(data)

    return encrypted_data

# Function for HMAC
def hmac(key, pt1):
    #opad
    opad = "5C"
    b_opad = hex2bin(opad)

    #ipad
    ipad = "36"
    b_ipad = hex2bin(ipad)

    print("IPad in hexadecimal and binary are", ipad, b_ipad)
    print("oPad in hexadecimal and binary are", opad, b_opad)
    
    # constant IV
    IV = "1234ABCDEFF98765" #64
    print("IV: ", IV)

    #generating k+
    b_key = ensure_key_length(key)
    
    print("Key: ", b_key)
    
    #divide message into blocks
    splitted = [pt1[i:i+16] for i  in range(0, len(pt1), 16)]
    print ("\nMessage blocks: ", splitted)

    # k XOR ipad
    si = xor(b_key, b_ipad)
    si = add_zeros_at_start(si, 64)

    print("\nk XOR ipad: ",si)

    # k XOR opad
    s0 = xor(b_key, b_opad)
    s0 = add_zeros_at_start(s0, 64)
    print("k XOR ipad: ",s0)

    # first round
    IV1 = des_func(si, IV)
    print("\nh((ipad XOR k), IV): " + IV)

    count = 0
    # for message blocks of 64 bits each
    for i in range(0, len(splitted)):
        # padding 
        s = add_zeros_at_last(splitted[i], 16)
        IV1 = des.des_func(hex2bin(s), IV1)
        print("h(m[" + str(count) +"], IV'): "+ IV1)
        count += 1

    # for opad XOR k
    IV2 = des_func(s0, IV)
    print("h((opad XOR k), IV):", IV2)

    # tag
    tag = des_func(hex2bin(IV1), IV2)
    print("tag: ", tag)

if __name__ == "__main__":
    
    pt1 = input("Type message in hexadecimal\n") # message
    key = "123456789ABC" # 48 bits

    hmac(key.encode('utf-8'), pt1.encode('utf-8'))
