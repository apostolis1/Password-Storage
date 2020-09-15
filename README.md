# Password-Storage
A native password storage, with encrypted database. Nothing is sent nowhere, everything is kept locally.
Run the PasswordStorageGui.py 

# How does it work 
You pick a master password, which is then used to encrypt and decrypt every other entry on the program.
Only the encrypted data are stored, which means that if someoene (even you) does not have access to the password, all they see is random bytes

# Demo

! [Demo Gif] (/demo/demo.gif)

# Libraries/Frameworks Used

- PyQt for the GUI part
- Sqlite3 for the databse
- Cryptography for the encryption
