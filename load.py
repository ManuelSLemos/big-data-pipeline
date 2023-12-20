from sqlalchemy import create_engine

username = 'root'
password = 'root'
host = 'mysql' # container_name / service
port = '3306'
database = 'rick'

engine = create_engine(f'mysql://{username}:{password}@{host}:{port}/{database}')

conn = engine.connect()

# query = 'SELECT * FROM estudiantes'
# conn.execute(query)

conn.close()