from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# کلید DES باید 8 بایت باشد (64 بیت)
key = b'mysecret'  # اینجا یک مثال کلید استفاده شده است، در کاربردهای واقعی باید کلید امن تر انتخاب شود

def encrypt_text(plain_text):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted_text).decode()

def decrypt_text(encoded_encrypted_text):
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_text = base64.b64decode(encoded_encrypted_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    return unpad(decrypted_text, DES.block_size).decode()

# مثال استفاده:
#plain_text = "Hello, World!"
plain_text = input("say something: ")
print("پیام اصلی:", plain_text)

encrypted_text = encrypt_text(plain_text)
print("پیام رمزنگاری شده:", encrypted_text)

decrypted_text = decrypt_text(encrypted_text)
print("پیام بازگشایی شده:", decrypted_text)
