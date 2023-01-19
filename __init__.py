import sqlite3
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config["DEBUG"] = True

UPLOAD_FOLDER = r'static\files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mydb = sqlite3.connect("dataset.db")

mcr = mydb.cursor()

for x in mcr:
    print(x)
@app.route('/')
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def uploadFiles():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # uploaded_file.save(file_path)
        parseCSV(uploaded_file)
    return redirect(url_for('index.html'))


def parseCSV(filePath):
    col_names = ['CustomerId', 'EmailId', 'CustomerName', 'CreditScore', 'Location', 'Gender', 'Age',
                 'NoOfTransactions', 'Balance', 'NoOfProducts', 'HasCrCard', 'IsActMember', 'TotalTransactAmt',
                 'EstdSalary', 'Exited', 'TransactDate']
    df = pd.read_csv(filePath, names=col_names, header=None)
    for i, row in df.iterrows():
        sql = "INSERT INTO addresses (CustomerId, EmailId, CustomerName, CreditScore, Location, Gender, Age, NoOfTransactions, Balance, NoOfProducts, HasCrCard, IsActMember, TotalTransactAmt, EstdSalary, Exited, TransactDate) VALUES (%d, %s, %s, %f, %s, %s, %f, %f, %f, %f, %f, %f, %f, %f, %f, %s)"
        value = (
            row['CustomerId'], row['EmailId'], row['CustomerName'], row['CreditScore'], row['Location'], row['Gender'],
            row['Age'], row['NoOfTransactions'], row['Balance'], row['NoOfProducts'], row['HasCrCard'],
            row['IsActMember'],
            row['TotalTransactAmt'], row['EstdSalary'], row['Exited'], row['TransactDate'])
        mcr.execute(sql, value)
        mydb.commit()
        print(i, row['CustomerId'], row['EmailId'], row['CustomerName'], row['CreditScore'], row['Location'],
              row['Gender'], row['Age'], row['NoOfTransactions'], row['Balance'], row['NoOfProducts'], row['HasCrCard'],
              row['IsActMember'], row['TotalTransactAmt'], row['EstdSalary'], row['Exited'], row['TransactDate'])


if __name__ == "__main__":
    app.run(port=5000)
