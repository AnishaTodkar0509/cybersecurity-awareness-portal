import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift % 26
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def vigenere_cipher(text, keyword, mode='encrypt'):
    result = ""
    keyword = keyword.upper()
    keyword_idx = 0
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift = ord(keyword[keyword_idx % len(keyword)]) - 65
            
            if mode == 'decrypt':
                shift = -shift
                
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            keyword_idx += 1
        else:
            result += char
    return result

def generate_hash(text, algo='sha256'):
    if algo == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    return hashlib.sha256(text.encode()).hexdigest()

def rsa_demo(text):
    # Generate keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    
    # Encrypt
    ciphertext = public_key.encrypt(
        text.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Decrypt
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    return {
        'public_key_preview': str(public_key.public_numbers().n)[:50] + "...",
        'ciphertext_base64': base64.b64encode(ciphertext).decode('utf-8'),
        'decrypted_text': plaintext.decode('utf-8')
    }

def aes_demo(text):
    key = os.urandom(32) # AES-256
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    
    # Encrypt
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(text.encode()) + encryptor.finalize()
    
    # Decrypt
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    return {
        'key_base64': base64.b64encode(key).decode('utf-8'),
        'iv_base64': base64.b64encode(iv).decode('utf-8'),
        'ciphertext_base64': base64.b64encode(ciphertext).decode('utf-8'),
        'decrypted_text': plaintext.decode('utf-8')
    }
