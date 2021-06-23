# DjangoWallet (REST API)
The test task is to make a simple REST service (Django REST framework).

Personal financial management service must have the following functions:
- The user stores data about his wallet: arbitrary name and balance in rubles.
- A history of transactions is kept within the wallet.
- One user may have several wallets.

The service API must provide the user:
- Create, edit and delete wallets.
- Create and delete transactions. User can't directly edit the wallet balance.
Each transaction has a date, a value and an arbitrary comment from the user.
- View the wallets list.
- View the transactions list both within one wallet and all at once.
