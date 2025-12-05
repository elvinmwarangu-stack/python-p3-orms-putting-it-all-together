import sqlite3

# Use in-memory DB for testing; or use "dogs.db" for persistent storage
CONN = sqlite3.connect(":memory:")  
CURSOR = CONN.cursor()
