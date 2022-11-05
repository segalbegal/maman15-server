from data.data_holder import DataHolder
import sqlite3

DB_FILE = 'server.db'

class SqliteDataHolder(DataHolder):
    def __init__(self) -> None:
        self.conn: sqlite3.Connection = sqlite3.connect(DB_FILE, check_same_thread=False)
        self.conn.text_factory = bytes

        self._init_db()

    def _get_data(self, query: str, parameters: tuple=()) -> list:
        cur = self.conn.cursor()
        cur.execute(query, parameters)
        data = cur.fetchall()
        cur.close()

        return data

    def _execute_query(self, query: str, parameters: tuple=()) -> None:
        cur = self.conn.cursor()
        cur.execute(query, parameters)
        self.conn.commit()
        cur.close()

    def _init_db(self) -> None:
        self.conn.executescript('PRAGMA foreign_keys = ON;')
        self._init_table('CLIENTS')
        self._init_table('FILES')

    def _init_table(self, table_name: str) -> None:
        query = f"SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?;"
        data = self._get_data(query, (table_name,))

        if len(data) == 0:
            self._create_table(table_name)

    def _create_table(self, table_name: str) -> None:
        file_name = f'./db_queries/{table_name}.sql'
        with open(file_name) as f:
            query = f.read()

        self.conn.executescript(query)

    def fetch_all_data(self) -> tuple:
        clients = self._get_data('SELECT * FROM CLIENTS')
        clients_dict = {
            client[0]: {
                'id': client[0],
                'name': client[1].decode('utf-8'),
                'public-key': client[2],
                'aes-key': client[3],
                'last-seen': client[4].decode('utf-8')
            } for client in clients}

        files = self._get_data('SELECT * FROM FILES')
        files_list = [
            {
                'id': file[0],
                'file-name': file[1].decode('utf-8'),
                'file-path': file[2].decode('utf-8'),
                'verified': file[3] == 1,
            } for file in files]

        return clients_dict, files_list

    def update_last_seen(self, id: bytes) -> None:
        query = f'UPDATE CLIENTS SET LastSeen = datetime() WHERE ID = ?;'
        self._execute_query(query, (id,))

    def user_exists(self, name: str) -> bool:
        query = f'SELECT * FROM CLIENTS WHERE NAME = ?;'
        data = self._get_data(query, (name,))

        return len(data) > 0

    def insert_user(self, details: dict) -> None:
        parameters = (details['id'], details['name'])
        query = f'INSERT INTO CLIENTS (ID, Name, LastSeen) VALUES (?, ?, datetime());'
        self._execute_query(query, parameters)

    def update_user_cred(self, details: dict) -> None:
        parameters = details['public-key'], details['aes-key'], details['id']
        query = 'UPDATE CLIENTS SET PUBLICKEY = ?, AESKEY = ? WHERE ID = ?'
        self._execute_query(query, parameters)

    def insert_file(self, details: dict) -> None:
        parameters = (details['id'], details['file-name'], details['file-path'], details['verified'])
        query = 'INSERT INTO FILES (ID, FileName, PathName, Verified) VALUES (?, ?, ?, ?);'
        self._execute_query(query, parameters)

    def update_file_verification(self, details: dict) -> None:
        query = 'UPDATE FILES SET VERIFIED = True WHERE ID = ? AND FILENAME = ?'
        parameters = (details['id'], details['file-name'])
        self._execute_query(query, parameters)

    def get_user_name(self, details: dict) -> str:
        query = 'SELECT NAME FROM CLIENTS WHERE ID = ?'
        data = self._get_data(query, (details['id'],))
        return data[0][0]

    def get_user_aes(self, details: dict) -> bytes:
        query = 'SELECT AESKEY FROM CLIENTS WHERE ID = ?'
        data = self._get_data(query, (details['id'],))

        return data[0][0]
