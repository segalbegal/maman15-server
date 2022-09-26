from data.data_holder import DataHolder
import sqlite3

DB_FILE = 'server.db'

class SqliteDataHolder(DataHolder):
    def __init__(self) -> None:
        self.conn: sqlite3.Connection = sqlite3.connect(DB_FILE, check_same_thread=False)
        self.conn.text_factory = bytes

    def update_last_seen(self, id) -> None:
        query = f'UPDATE CLIENTS SET LastSeen = datetime() WHERE ID = ?;'
        cur = self.conn.cursor()
        cur.execute(query, (id))
        self.conn.commit()
        cur.close()

    def user_exists(self, name: str) -> bool:
        query = f'SELECT * FROM CLIENTS WHERE NAME = ?;'
        cur = self.conn.cursor()
        cur.execute(query, (name))
        data = cur.fetchall()
        cur.close()

        return len(data) > 0

    def insert_user(self, details: dict) -> None:
        parameters = (details['id'], details['name'])
        query = f'INSERT INTO CLIENTS (ID, Name, LastSeen) VALUES (?, ?, datetime());'

        cur = self.conn.cursor()
        cur.execute(query, parameters)
        self.conn.commit()
        cur.close()

    def insert_file(self, details: dict) -> None:
        parameters = (details['id'], details['file-name'], details['file-path'], details['verified'])
        query = f'INSERT INTO FILES (ID, FileName, PathName, Verified) VALUES (?, ?, ?, ?);'

        cur = self.conn.cursor()
        cur.execute(query, parameters)
        self.conn.commit()
        cur.close()