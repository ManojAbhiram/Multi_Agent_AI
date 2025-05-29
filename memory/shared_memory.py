import sqlite3
import uuid
from datetime import datetime

class SharedMemory:
    def __init__(self, db_name="shared_memory.db"):
        self.conn = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id TEXT PRIMARY KEY,
                source TEXT,
                type TEXT,
                timestamp TEXT,
                intent TEXT,
                extracted_values TEXT,
                thread_id TEXT
            )
        ''')
        self.conn.commit()

    def store(self, source, type_, intent, extracted_values, thread_id):
        self.conn.execute(
            '''INSERT INTO memory (id, source, type, timestamp, intent, extracted_values, thread_id)
               VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (
                str(uuid.uuid4()),
                source,
                type_,
                datetime.now().isoformat(),
                intent,
                json.dumps(extracted_values),
                thread_id
            )
        )
        self.conn.commit()
