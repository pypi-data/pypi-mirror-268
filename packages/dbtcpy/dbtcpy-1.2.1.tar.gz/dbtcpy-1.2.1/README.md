<div align="center">

#    › ‎ ‎ ‎ ‎ ‎ ‎ DBTCPY

</div>

---

|  functions  |                  __init__                  |                      __del__                      |               __enter__              |                                               __exit__                                              | add                                                                               |
|:-----------:|:------------------------------------------:|:-------------------------------------------------:|:------------------------------------:|:---------------------------------------------------------------------------------------------------:|-----------------------------------------------------------------------------------|
| description |        initializes the dbtcpy class.       | Destructor to ensure database connection closure. | Enter method for context management. |                                 Exit method for context management.                                 | Adds a new user to the database.                                                  |   
|  parameters | db_name: Name of the SQLite database file. |                        None                       |                 None                 | exc_value: Value of exception. , exc_value: Value of exception. , traceback: Traceback information. | user_data: A dictionary containing user data with keys "username" and "password". |  
|   returns   |                    None                    |                        None                       |      The dbtcpy instance itself.     |                                                 None                                                | None                                                                              |  
    
---

```py
with dbtcpy("test.db") as db:
    db._create_database()
    user_data = {"username": "jhon doe", "password": "password_123"}
    db.add(user_data)
    user = db.show(1)
    if user:
        print_success(
            f"user id: {user[0]}, username: {user[1]}, password: {user[2]}"
        )
    else:
        print_warning("user not found.")
    users = db.search(username="john_doe")
    if users:
        print_success("search results:")
        for user in users:
            print_success(
                f"user id: {user[0]}, username: {user[1]}, password: {user[2]}"
            )
    else:
        print_warning("no users found matching the search criteria.")
```

<div align="center">
    
---
    
`#TLM #TokenLifesMatter #NoTerm #FreeToucan #FreeToken #FreeToucans #FreeTokens`

</div>
