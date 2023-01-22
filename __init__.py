import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO data (CustomerId, EmailId, CustomerName, CreditScore, Location, Gender, Age, NoOfTransactions, Balance, NoOfProducts, HasCrCard, IsActMember, TotalTransactAmt, EstdSalary, Exited, TransactDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Data', 'CSV File for dataframe')
            )


connection.commit()
connection.close()
