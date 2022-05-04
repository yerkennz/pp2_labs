import psycopg2
from config import config

def create_table():
	commands = (
		"""
		CREATE TABLE telephone(
			Users_name VARCHAR (20) UNIQUE NOT NULL,
			Tell_num VARCHAR (20) UNIQUE NOT NULL
		);
		"""	
	)
	con = None
	try: 
		params = config()
		con = psycopg2.connect(**params)
		cur = con.cursor()
		cur.execute(commands)
		cur.close()
		con.commit()
	except Exception as e:
		print(str(e))
	if con is not None:
		con.close()

create_table()