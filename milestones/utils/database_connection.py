"""

example of context manager with error handling

Here's a few great or interesting resources:

Python with Context Managers, another Jeff Knupp post. It gets a bit advanced at the end, but it's really good up to halfway through. Read half and then continue after completing more of the course!
Introduction to Context Managers in Python, a nice read to review context managers as we've looked at in this section. Worth a look!
SQLite AUTOINCREMENT : Why You Should Avoid Using It, we didn't talk about AUTOINCREMENT in SQLite, but it is a frequent question amongst my students. Here's why AUTOINCREMENT can be a bad choice in SQLite.


Type Hinting : https://docs.python.org/3/library/typing.html
"""

import sqlite3


class DatabaseConnection:

    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
