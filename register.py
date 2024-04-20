import sqlite3
import encode_decode

connection = sqlite3.connect('playlist.db')
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE Users(
# Id INTEGER PRIMARY KEY NOT NULL,
# Username CHAR NOT NULL,
# Password CHAR NOT NULL
# )''')

try:
    Pass = encode_decode.base64_encode(input("input user password"))
    user = input("input name")
    cursor.execute(f'SELECT* FROM Users WHERE Username = "{user}"')
    if cursor.fetchall() == user:
        print("Username already exist")
    else:
        cursor.execute(f''' INSERT INTO Users (Id,  Username, Password) VALUES  ('{input("input your id")}', '{input("input your username")}', '{Pass}')''')
        connection.commit()
        connection.close()

except Exception:
    print("Run the file again and give the id one more")





