import cx_Oracle

try:
    connection = cx_Oracle.connect("admin/password@localhost:1522/orcl")
    cur = connection.cursor()
    print("Successfully connected to orcl database!")

except:
    print("Database connection failed: ")

