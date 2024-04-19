from    utils          import    print_success
from    utils          import    print_warning
from    utils          import    clear_screen
from    utils          import    print_error
from    utils          import    install

import webbrowser
import sqlite3
import time

try:
    install('sqlite3')
except:
    print_error("your system cannot install sqlite3, please check your internet connection and try again later.")
    
try:
    clear_screen()
except:
    print_error("the screen could not be cleared.")

class dbtcpy:
    """
    A class for interacting with a SQLite database.
    """
    
    def __init__(self, db_name):
        """
        Initialize the Dbtcpy class.
        """
        self.db_name = db_name

        self.conn = None
        self.cursor = None

        self._connect()

    def __del__(self):
        """Destructor to ensure database connection closure."""
        self._disconnect()

    def __enter__(self):
        """Enter method for context management."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit method for context management."""
        self._disconnect()

    def _connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            raise RuntimeError(f"failed to connect to database: {e}")

    def _disconnect(self):
        """Close the connection to the SQLite database."""
        try:
            if self.conn:
                self.conn.close()
        except sqlite3.Error as e:
            raise RuntimeError(f"failed to disconnect from database: {e}")

    def _create_database(self):
        """Create the necessary table if it doesn't exist in the database."""
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """
            )
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"failed to create database: {e}")

    def add(self, user_data):
        """
        Add a new user to the database.
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO users (username, password)
                VALUES (?, ?)
            """,
                (user_data["username"], user_data["password"]),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"failed to add user: {e}")

    def delete(self, user_id):
        """
        Delete a user from the database.
        """
        try:
            self.cursor.execute(
                """
                DELETE FROM users WHERE id=?
            """,
                (user_id,),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"failed to delete user: {e}")

    def edit(self, user_id, new_data):
        """
        Edit user data in the database.
        """
        try:
            self.cursor.execute(
                """
                UPDATE users
                SET username=?, password=?
                WHERE id=?
            """,
                (new_data["username"], new_data["password"], user_id),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"failed to edit user: {e}")

    def show(self, user_id):
        """
        Retrieve user data from the database.
        """
        try:
            self.cursor.execute(
                """
                SELECT * FROM users WHERE id=?
            """,
                (user_id,),
            )
            user = self.cursor.fetchone()
            return user
        except sqlite3.Error as e:
            raise RuntimeError(f"failed to show user: {e}")

    def search(self, **kwargs):
        """
        Search for users in the database based on specified criteria.
        """
        try:
            conditions = []
            values = []
            for key, value in kwargs.items():
                conditions.append(f"{key}=?")
                values.append(value)
            conditions_str = " AND ".join(conditions)
            self.cursor.execute(
                f"""
                SELECT * FROM users WHERE {conditions_str}
            """,
                tuple(values),
            )
            users = self.cursor.fetchall()
            return users

        except sqlite3.Error as e:
            raise RuntimeError(f"failed to search user: {e}")

if __name__ == "__main__":
    print_warning('This library does not allow direct execution,\n    please try importing it in the following way or consult the documentation that will open below.')
    time.sleep(0.099)
    webbrowser.open_new_tab(url='https://pypi.org/project/dbtcpy')
