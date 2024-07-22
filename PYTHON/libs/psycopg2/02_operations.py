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


    ##############
    # OPERATIONS #
    ##############
    
    # drop table (see 'insert multiple values')
    cur.execute('DROP TABLE IF EXISTS employee')

    # create table
    create_table = ''' CREATE TABLE IF NOT EXISTS employee (
                            id      int PRIMARY KEY,
                            name    varchar(40) NOT NULL,
                            salary  int,
                            dept_id varchar(30)) '''
    cur.execute(create_table)
    
    # insert values into the table
    # '%s' is to avoid sql injection.
    insert_data_to_the_db = ''' INSERT INTO employee
                                (id, name, salary, dept_id)
                                VALUES (%s, %s, %s, %s) '''
    insert_value = (1, 'James', 12000, 'D1')
    # cur.execute(insert_data_to_the_db, insert_value)

    # insert multiple values
    # id=1 will raise an error,
    # so to avoid it - drop the table.
    insert_values = [ (1, 'Mike', 13000, 'D1'), (2, 'Nick', 15000, 'D1'), (3, 'Rohn', 14000, 'D2') ]
    for inser_value in insert_values:
        cur.execute(insert_data_to_the_db, inser_value)

    # fetch data from the table
    cur.execute('SELECT * FROM employee')
    # to see the result (all records)
    for record in cur.fetchall():
        print(record[1], record[2])
    # But if there are hundreeds of columns
    # it vould be tricky to get right column.
    # So to solve this, we can return in a dictionary format.
    import psycopg2.extras
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # It wiil tell to the cursor return data in ofrm of a dictionary.
    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        print(record['name'], record['salary'])

    # update table data
    update_table = 'UPDATE employee SET salary = salary + (salary * 0.5)'
    cur.execute(update_table)

    # delete particular employee
    delete_employee = 'DELETE FROM employee WHERE name = %s'
    delete_record = ('Mike',)
    cur.execute(delete_employee, delete_record)

    # Save (send) any transactions (operations) we've made to the DB.
    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

