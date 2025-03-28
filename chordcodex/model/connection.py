import psycopg2
from psycopg2.extras import RealDictCursor

class DBConnection:
    """Context manager for PostgreSQL connections using env vars."""
    def __init__(self, **config):
        self.config = config
    
    def __enter__(self):
        self.conn = psycopg2.connect(
            **self.config,
            cursor_factory=RealDictCursor
        )
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.cursor.close()
        self.conn.close()