# A file designed to be run as a standalone application, using the Encryptor class
# in a cmd environment

import os
import base64
import sqlite3
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os




class Encryptor():

    def getSalt(self):
        return self.salt

    def generateKeyFromPassword(self, password):
        backend = default_backend()
        salt = self.salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=backend
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def getKey(self):
        return self.key

    def encrypt(self, data):

        data = data.encode()
        f = Fernet(self.key)
        encrypted = f.encrypt(data)
        return encrypted

    def decrypt(self, data):
        f = Fernet(self.key)
        decrypted = f.decrypt(data)
        return decrypted

    def printData(self):
        print("This is the key:" + str(self.key))
        recs = self.getData()
        for record in recs:
            print(record[len(record) - 1])  # prints the ID
            for element in record:
                try:
                    encoded = self.decrypt(element)
                    print(encoded.decode())
                except:
                    pass

    def __init__(self, pwd):

        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)

        if os.path.isfile("salt.txt"):
            with open("salt.txt", "rb") as f:
                self.salt = f.read()
                f.close()
        else:
            with open("salt.txt", "wb") as f:
                self.salt = os.urandom(16)
                f.write(self.salt)
                f.close()

        self.key = self.generateKeyFromPassword(pwd)
        return


def main():
    password = input("Choose a password:")
    try:
        myEncryptor = Encryptor(password)
    except:
        print("Invalid password")
    choice = input("Do you want to encrypt (E) or decrypt (D) data (enter E or D):")
    if choice.lower() == "e":
        data = input("Write the data you want to be encrypted:")
        try:
            with open("data.txt", "a+") as f:
                f.write(myEncryptor.encrypt(data).decode()+"\n")
                f.close()
                input("Data written successfully on data.txt, press Enter to exit..")
        except Exception as e:
            print(e)
            input("Something went wrong, press Enter to exit")
    elif choice.lower() == "d":
        try:
            data = open("data.txt", "r")
            for i in data:
                print(myEncryptor.decrypt(i.encode()).decode())
            input("Data decrypted successfully, press Enter to exit..")
        except Exception as e:
            print(e)
            input("Something went wrong here, press Enter to exit..")
    else:
        input("You didn't give a valid answer, press Enter to exit..")
    return


if __name__ == '__main__':
    main()