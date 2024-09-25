import sqlite3

# Create a connection to a SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('J:/AlgoSetup/data/trading_data.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create a simple table to store trading logs
cur.execute('''
CREATE TABLE IF NOT EXISTS trade_logs (
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    trade_type TEXT,
    profit REAL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Insert a sample trade record
cur.execute('''
INSERT INTO trade_logs (symbol, trade_type, profit) VALUES (?, ?, ?)
''', ('EURUSD', 'BUY', 1.5))

# Commit the transaction
conn.commit()

# Fetch the data to verify insertion
cur.execute('SELECT * FROM trade_logs')
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
