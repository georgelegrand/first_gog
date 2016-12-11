def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def key_check(msg2bits,key2bits):
    if len(msg2bits) > len(key2bits):
        n = len(msg2bits) // len(key2bits)
        add = len(msg2bits) % len(key2bits)
        new_key2bits = (key2bits * n) + key2bits[:add]
        print("new_key2bits: ", new_key2bits)
        print(len(msg2bits), len(new_key2bits))
        return new_key2bits
    else:
        return key2bits

def gamma_xor(msg2bits, key2bits):
    msg_num = int(msg2bits,2)
    key_num = int(key2bits,2)
    print(bin(msg_num ^ key_num))
    res_xor = bin(msg_num ^ key_num)[2:]
    print(res_xor)
    print(text_from_bits(res_xor))
    return text_from_bits(res_xor)



msg = input("Enter the message for encryption: ")
msg2bits = text_to_bits(msg)
print(type(msg2bits), msg2bits)

key = input("Enter the key: ")
key2bits = text_to_bits(key)
print(type(key2bits), key2bits)

key2bits = key_check(msg2bits,key2bits)

crypted_msg = gamma_xor(msg2bits, key2bits)

d_msg = input("Enter the message for decryption: ")
d_msg2bits = text_to_bits(crypted_msg)
#print(type(msg2bits), msg2bits)
decrypted_msg = gamma_xor(d_msg2bits, key2bits)

#print(text_to_bits('hello'))
#print(text_from_bits('110100001100101011011000110110001101111'))
