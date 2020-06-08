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

    def addData(self, site, username, password):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        c.execute("INSERT INTO passwords VALUES(:site, :username, :password)",
        {
            'site': self.encrypt(site),
            'username': self.encrypt(username),
            'password': self.encrypt(password)
        }
        )
        conn.commit()
        conn.close()
        return

    def getData(self):#Establishes a connection and returns a list of records
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        c.execute("SELECT *, oid FROM passwords")
        records = c.fetchall()
        conn.commit()
        conn.close()
        return records

    def getDecreptedData(self):
        tempData = self.getData()
        result = []
        for i in tempData:
            tempRow = []
            for element in i:

                try:
                    tempRow.append((self.decrypt(element)))
                except:
                    pass
            result.append(tempRow)
        return result

    def deleteData(self):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        c.execute("DELETE FROM passwords")
        conn.commit()
        c.execute("VACUUM")
        conn.commit()

        conn.close()
        return

    def deleteCustomData(self, index):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        c.execute("DELETE FROM passwords WHERE ROWID=:row_id", {'row_id': index})
        conn.commit()
        c.execute("VACUUM")
        conn.commit()
        conn.close()
        return

    def printData(self):
        print("This is the key:" + str(self.key))
        recs = self.getData()
        for record in recs:
            print(record[len(record)-1]) #prints the ID
            for element in record:
                try:
                    encoded = self.decrypt(element)
                    print(encoded.decode())
                except:
                    pass
    

    def encryptWithNewPassword(self, newpswd):
        tempData = self.getDecreptedData()
        self.deleteData()
        self.key = self.generateKeyFromPassword(newpswd)
        # newEncryptor = Encryptor(newpswd)
        print("TEMP DATA:")
        print(type(tempData))
        print(tempData)
        for data in tempData:
            try:
                self.addData((data[0].decode()), (data[1].decode()), (data[2].decode()))
            except:
                print("FOUND")


    def __init__(self, pwd):

        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        self.database = "data.db"
        try:
            c.execute(""" CREATE TABLE passwords(
        site text,
        username text,
        encrypted_password text
        )
            
        """)
        except:
            pass

        conn.commit()
        conn.close()

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
    password = "YOUR PASSWORD HERE"
    encryptor = Encryptor(password)
    encryptor.deleteData()
    encryptor.addData("SITE 1", "USERNAME 1", "PASSWORD 1")
    encryptor.addData("SITE 2", "USERNAME 2", "PASSWORD 2")
    result = encryptor.getDecreptedData()
    print(result)

if __name__ == '__main__':
    main()