from sqlalchemy import create_engine
from sqlalchemy import text

username = 'root'
password = 'root'
host = 'mysql' # container_name / service
port = '3306'
database = 'rick'

engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}')

conn = engine.connect()

characters_table = '''CREATE TABLE IF NOT EXISTS characters ( 
    id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), 
    status VARCHAR(255), species VARCHAR(255), 
    kind VARCHAR(255), 
    gender VARCHAR(255), 
    origin VARCHAR(255), 
    location VARCHAR(255));'''

# Create Table
conn.execute(text(characters_table))