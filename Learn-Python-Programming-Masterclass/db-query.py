import psycopg2

# Open database connection
# connect to the database with the credientials
try:
    connection = psycopg2.connect(
        host = "thewu.com",  # host on which the database is running
        port = "9005",
        database = "test",  # name of the database to connect to
        user = "test",  # username to connect with
        password = "wuuuuu")  # password associated with your username
except:
    print('Can not access database')

# create a cursor object
cursor = connection.cursor()

# execute query with cursor
query = "SELECT fiscal_year, expense_type, SUM (amount) " \
        "FROM accounting_expense_item " \
        "where fiscal_year='FY_2017_2018'  " \
        "GROUP BY fiscal_year,expense_type"
cursor.execute(query)

# retrieve results of query
resultset = cursor.fetchall()

# show retrieved data
for record in resultset:
    print(record)
