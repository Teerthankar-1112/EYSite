DROP TABLE IF EXISTS data;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CustomerId TEXT NOT NULL,
    EmailId TEXT NOT NULL,
    CustomerName TEXT NOT NULL,
    CreditScore TEXT NOT NULL,
    Location TEXT NOT NULL,
    Gender TEXT NOT NULL,
    Age TEXT NOT NULL,
    NoOfTransactions TEXT NOT NULL,
    Balance TEXT NOT NULL,
    NoOfProducts TEXT NOT NULL,
    HasCrCard TEXT NOT NULL,
    IsActMember TEXT NOT NULL,
    TotalTransactAmt TEXT NOT NULL,
    EstdSalary TEXT NOT NULL,
    Exited TEXT NOT NULL,
    TransactDate TEXT NOT NULL,
);
