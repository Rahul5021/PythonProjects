import pg8000

conn = pg8000.connect(database="to_do", user="postgres", password="159357", host="localhost", port="5432")

if conn:
    print("hi")