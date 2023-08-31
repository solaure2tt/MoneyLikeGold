# MoneyLikeGold
================================================================================

## Description
This application is to manage the money present in a banking account. It allow to create an account, do transactions an view balance.

## How to use the application

create the database

cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p



in one terminal type:

MLG_MYSQL_USER=mlg_dev MLG_MYSQL_PWD=mlg_dev_pwd MLG_MYSQL_HOST=localhost MLG_MYSQL_DB=mlg_dev_db MLG_TYPE_STORAGE=db MLG_API_HOST=0.0.0.0 MLG_API_PORT=5000 python3 -m api.v1.app


In another terminal you can test the application by calling the good API

### Create a user

curl -X POST http://0.0.0.0:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"email": "YOUR_EMAIL", "YOUR_PASSWORD": "lor", "last_name": "YOUR_NAME"}'
example: 
curl -X POST http://0.0.0.0:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"email": "lor@yahoo.fr", "password": "lor", "last_name": "Laure"}'


{"__class__":"User","created_at":"2023-08-27T12:29:33.439521","email":"lor@yahoo.fr","id":"e4965fba-3013-4650-a803-4720fc5cb887","last_name":"Laure","password":"lor","updated_at":"2023-08-27T12:29:33.439533"}


### View a specific user

curl -X GET http://0.0.0.0:5000/api/v1/users/USER_ID
example:
curl -X GET http://0.0.0.0:5000/api/v1/users/e4965fba-3013-4650-a803-4720fc5cb887 


### Update a user

curl -X PUT http://0.0.0.0:5000/api/v1/users/USER_ID -H "Content-Type: application/json" -d '{"field": value, …, “field”: value}'
example: 
curl -X PUT http://0.0.0.0:5000/api/v1/users/e4965fba-3013-4650-a803-4720fc5cb887 -H "Content-Type: application/json" -d '{"first_name": “Alain”}'


### List all users

curl -X GET http://0.0.0.0:5000/api/v1/users




### Delete a user

curl -X DELETE http://0.0.0.0:5000/api/v1/users/USER_ID


### Create an account

curl -X POST http://0.0.0.0:5000/api/v1/accounts/ -H "Content-Type: application/json" -d '{"account_number": "VALUE", "user_id": "USER_ID"}'

example:
curl -X POST http://0.0.0.0:5000/api/v1/accounts/ -H "Content-Type: application/json" -d '{"account_number": "8888-7777-6666-5555", "user_id": "e4965fba-3013-4650-a803-4720fc5cb887"}'2

{"__class__":"Account","account_number":"3332-4455-5599","created_at":"2023-08-27T12:33:43.815225","id":"6595efa3-3d47-4695-b040-658898f0f0d9","updated_at":"2023-08-27T12:33:43.815237","user_id":"e4965fba-3013-4650-a803-4720fc5cb887"}


### View a specific account

curl -X GET http://0.0.0.0:5000/api/v1/accounts/ACCOUNT_ID

example:
curl -X GET http://0.0.0.0:5000/api/v1/accounts/6595efa3-3d47-4695-b040-658898f0f0d9


### Update an account

curl -X PUT http://0.0.0.0:5000/api/v1/accounts/ACCOUNT_ID -H "Content-Type: application/json" -d '{"amount_account": 1000}'

Example:
curl -X PUT http://0.0.0.0:5000/api/v1/accounts/6595efa3-3d47-4695-b040-658898f0f0d9 -H "Content-Type: application/json" -d '{"amount_account": 1000}'

{"__class__":"Account","account_number":"3332-4455-5599","amount_account":1000,"created_at":"2023-08-27T12:33:44","id":"6595efa3-3d47-4695-b040-658898f0f0d9","updated_at":"2023-08-27T12:33:44","user_id":"e4965fba-3013-4650-a803-4720fc5cb887"}



### List all accounts

curl -X GET http://0.0.0.0:5000/api/v1/accounts/


### Delete account

curl -X DELETE http://0.0.0.0:5000/api/v1h/accounts/ACCOUNT_ID


#### Create a transaction
withdraw
curl -X POST http://0.0.0.0:5000/api/v1/transactions/ -H "Content-Type: application/json" -d '{"amount_transaction": 280, "transaction_type": 0, "account1_id": "ACCOUNT_ID", "user_id": "USER_ID"}'

Example:
curl -X POST http://0.0.0.0:5000/api/v1/transactions/ -H "Content-Type: application/json" -d '{"amount_transaction": 280, "transaction_type": 0, "account1_id": "6595efa3-3d47-4695-b040-658898f0f0d9", "user_id": "e4965fba-3013-4650-a803-4720fc5cb887"}'


#### Deposit

curl -X POST http://0.0.0.0:5000/api/v1/transactions/ -H "Content-Type: application/json" -d '{"amount_transaction": AMOUNT_TRANSACTION, "transaction_type": 1, "account1_id": "ACCOUNT_ID", "user_id": "USER_ID"}'

Example:
curl -X POST http://0.0.0.0:5000/api/v1/transactions/ -H "Content-Type: application/json" -d '{"amount_transaction": 400, "transaction_type": 1, "account1_id": "6595efa3-3d47-4695-b040-658898f0f0d9", "user_id": "e4965fba-3013-4650-a803-4720fc5cb887"}'

{"__class__":"Transaction","account_id":"6595efa3-3d47-4695-b040-658898f0f0d9","amount_transaction":400,"created_at":"2023-08-27T14:02:06.840475","id":"caaed28d-b3a8-4bbf-88ae-fb908233ed22","transaction_type":1,"updated_at":"2023-08-27T14:02:06.840488","user_id":"e4965fba-3013-4650-a803-4720fc5cb887"}


####Transfer


curl -X POST http://0.0.0.0:5000/api/v1/transactions/ -H "Content-Type: application/json" -d '{"amount_transaction": AMOUNT_TRANSACTION, "transaction_type": 2, "account1_id": "FIRST_ACCOUNT_ID", "account2_id": "SECOND_ACCOUNT_ID", "user_id": "USER_ID"}'

Example:
curl -X POST http://0.0.0.0:5000/api/v1/transactions/ -H "Content-Type: application/json" -d '{"amount_transaction": 250, "transaction_type": 2, "account1_id": "6595efa3-3d47-4695-b040-658898f0f0d9", "account2_id": "c3371231-ab62-449a-962f-76612c701141", "user_id": "e4965fba-3013-4650-a803-4720fc5cb887"}'


### View a transaction

curl -X GET http://0.0.0.0:5000/api/v1/transactions/TRANSACTION_ID


### List all transactions

curl -X GET http://0.0.0.0:5000/api/v1/transactions/


### Delete a transaction

curl -X DELETE http://0.0.0.0:5000/api/v1/transactions/TRANSACTION_ID




### List all transactions in a specific account

curl -X GET http://0.0.0.0:5000/api/v1/account/ACCOUNT_ID/transactions

Example:
curl -X GET http://0.0.0.0:5000/api/v1/account/c3371231-ab62-449a-962f-76612c701141/transactions



### List all transactions for a specific user

curl -X GET http://0.0.0.0:5000/api/v1/user/USER_ID/transactions

Example:
curl -X GET http://0.0.0.0:5000/api/v1/user/e4965fba-3013-4650-a803-4720fc5cb887/transactions


### View the balance of a specific account

curl -X GET http://0.0.0.0:5000/api/v1/account_balance/ACCOUNT_ID

Example:
curl -X GET http://0.0.0.0:5000/api/v1/account_balance/6595efa3-3d47-4695-b040-658898f0f0d9



