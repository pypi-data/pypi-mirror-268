```py
'            ████████▄  ▀█████████▄    ▄▄▄▄███▄▄▄▄      ▄███████▄ ▄██   ▄  
            ███   ▀███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███   ██▄
            ███    ███   ███    ███ ███   ███   ███   ███    ███ ███▄▄▄███
            ███    ███  ▄███▄▄▄██▀  ███   ███   ███   ███    ███ ▀▀▀▀▀▀███
            ███    ███ ▀▀███▀▀▀██▄  ███   ███   ███ ▀█████████▀  ▄██   ███
            ███    ███   ███    ██▄ ███   ███   ███   ███        ███   ███
            ███   ▄███   ███    ███ ███   ███   ███   ███        ███   ███
            ████████▀  ▄█████████▀   ▀█   ███   █▀   ▄████▀       ▀█████▀             
           𝑂𝑝𝑒𝑛 𝑆𝑜𝑢𝑟𝑐𝑒 𝑙𝑖𝑏𝑟𝑎𝑟𝑦 𝑡𝑜 𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑡 𝑤𝑖𝑡𝘩 𝑎 𝑆𝑄𝐿𝑖𝑡𝑒 𝑑𝑎𝑡𝑎𝑏𝑎𝑠𝑒, 𝑝𝑟𝑜𝑣𝑖𝑑𝑖𝑛𝑔 𝑚𝑒𝑡𝘩𝑜𝑑𝑠 𝑓𝑜𝑟           
           𝑎𝑑𝑑𝑖𝑛𝑔, 𝑑𝑒𝑙𝑒𝑡𝑖𝑛𝑔, 𝑒𝑑𝑖𝑡𝑖𝑛𝑔, 𝑎𝑛𝑑 𝑠𝑒𝑎𝑟𝑐𝘩𝑖𝑛𝑔 𝑢𝑠𝑒𝑟 𝑑𝑎𝑡𝑎 𝑖𝑛 𝑡𝘩𝑒 𝑑𝑎𝑡𝑎𝑏𝑎𝑠𝑒.           '
```

<div align="center">

 ![PyPI - Main](https://img.shields.io/pypi/v/dbmpy)
 ![PyPI - License](https://img.shields.io/pypi/l/dbmpy)


 
 ---
 
 
 ## Features
 
         Easy-to-use methods for database interaction.

         Automatically handles database connection opening and closing.

         Built-in error handling for robustness.

         Supports Create, Read, Update, and Delete operations on database records.
 
</div>
 
 ## Installation
 
 You can install dbtcpy using pip:
 
 ```bash
 pip install dbmpy
 ```
 
 ## Usage
 
 ### init
 
 ```python
 from dbmpy import dbmpy
 
 # Initialize the dbtcpy object with the name of your SQLite database
 db = dbmpy("my_database.db")
 ```
 
 ### add user
 
 ```python
 # Define user data
 user_data = {
     "username": "john_doe",
     "password": "password123"
 }
 
 # Add the user to the database
 db.add(user_data)
 ```
 
 ### delete user
 
 ```python
 # Delete a user by their ID
 db.delete(1)
 ```
 
 ### edit user info
 
 ```python
 # Update user information
 new_data = {
     "username": "jane doe",
     "password": "password2324"
 }
 db.edit(1, new_data)
 ```
 
 ### show user info
 
 ```python
 # Retrieve user information by ID
 user = db.show(1)
 print(user)
 ```
 
 ### search users with
 
 ```python
 # Search for users based on specific criteria
 users = db.search(username="john_doe")
 print(users)
 ```
