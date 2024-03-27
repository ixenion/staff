import psycopg2

hostname = 'localhost'
database = 'psyco'
username = 'arix'
pwd = '0000'
port_id = 5432

conn = None
cur = None

try:
    # 'conn' needed to beclosed.
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)
    
    # In order to perform any sql transactions
    # we will need to open a 'cursor'.
    # A 'cursor' is a something that can help you to perform
    # any of sql operations.
    # It kind of stores a values that will returned from sql operations.
    # 'cur' needed to be closed.
    cur = conn.cursor()
    

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

