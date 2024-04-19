"""         ████████▄  ▀█████████▄    ▄▄▄▄███▄▄▄▄      ▄███████▄ ▄██   ▄  
            ███   ▀███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███   ██▄
            ███    ███   ███    ███ ███   ███   ███   ███    ███ ███▄▄▄███
            ███    ███  ▄███▄▄▄██▀  ███   ███   ███   ███    ███ ▀▀▀▀▀▀███
            ███    ███ ▀▀███▀▀▀██▄  ███   ███   ███ ▀█████████▀  ▄██   ███
            ███    ███   ███    ██▄ ███   ███   ███   ███        ███   ███
            ███   ▄███   ███    ███ ███   ███   ███   ███        ███   ███
            ████████▀  ▄█████████▀   ▀█   ███   █▀   ▄████▀       ▀█████▀   """          
#       𝑂𝑝𝑒𝑛 𝑆𝑜𝑢𝑟𝑐𝑒 𝑙𝑖𝑏𝑟𝑎𝑟𝑦 𝑡𝑜 𝑖𝑛𝑡𝑒𝑟𝑎𝑐𝑡 𝑤𝑖𝑡𝘩 𝑎 𝑆𝑄𝐿𝑖𝑡𝑒 𝑑𝑎𝑡𝑎𝑏𝑎𝑠𝑒, 𝑝𝑟𝑜𝑣𝑖𝑑𝑖𝑛𝑔 𝑚𝑒𝑡𝘩𝑜𝑑𝑠 𝑓𝑜𝑟
#           𝑎𝑑𝑑𝑖𝑛𝑔, 𝑑𝑒𝑙𝑒𝑡𝑖𝑛𝑔, 𝑒𝑑𝑖𝑡𝑖𝑛𝑔, 𝑎𝑛𝑑 𝑠𝑒𝑎𝑟𝑐𝘩𝑖𝑛𝑔 𝑢𝑠𝑒𝑟 𝑑𝑎𝑡𝑎 𝑖𝑛 𝑡𝘩𝑒 𝑑𝑎𝑡𝑎𝑏𝑎𝑠𝑒.


import                            webbrowser
import                            subprocess
import                            importlib
import                            sqlite3
import                            time
import                            sys
import                            os

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def print_error(message):
    """Print an error message."""
    print(f"[\033[91m-\033[0m] {message}")

def print_success(message):
    """Print a success message."""
    print(f"[\033[92m+\033[0m] {message}")

def print_warning(message):
    """Print a warning message."""
    print(f"[\033[93m!\033[0m] {message}")

def package(package):
    """Execute command to download any dependencies."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package}"])

def install(package):
    """Install all needed dependencies."""
    try:
        importlib.util.find_spec(package)
    except ImportError:
        print(f"{package} is not installed. Installing...")
        package(package)

class dbmpy:
    """A class for interacting with a SQLite database."""
    
    def __init__(self, db_name):
        """Initialize the Dbtcpy class."""
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
            self._create_database()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to connect to database: {e}")

    def _disconnect(self):
        """Close the connection to the SQLite database."""
        try:
            if self.conn:
                self.conn.close()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to disconnect from database: {e}")

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
            raise RuntimeError(f"Failed to create database: {e}")

    def add(self, user_data):
        """Add a new user to the database."""
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
            raise RuntimeError(f"Failed to add user: {e}")

    def delete(self, user_id):
        """Delete a user from the database."""
        try:
            self.cursor.execute(
                """
                DELETE FROM users WHERE id=?
            """,
                (user_id,),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to delete user: {e}")

    def edit(self, user_id, new_data):
        """Edit user data in the database."""
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
            raise RuntimeError(f"Failed to edit user: {e}")

    def show(self, user_id):
        """Retrieve user data from the database."""
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
            raise RuntimeError(f"Failed to show user: {e}")

    def search(self, **kwargs):
        """Search for users in the database based on specified criteria."""
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
            raise RuntimeError(f"Failed to search user: {e}")

if __name__ == "__main__":
    print_warning('This library does not allow direct execution,\n    please try importing it in the following way or consult the documentation that will open below.')
    time.sleep(0.099)
    webbrowser.open_new_tab(url='https://pypi.org/project/dbmpy')