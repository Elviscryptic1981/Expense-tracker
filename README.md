# Personal Finance Tracker CLI

## Introduction
The Personal Finance Tracker CLI is a command-line application designed to help users manage their personal finances. Users can add income, record expenses, and view financial reports. This project leverages SQLAlchemy ORM for database management and Alembic for database migrations.

## Features
- Add users
- Record transactions (income and expenses)
- View a list of users
- View transactions for a specific user

## Project Structure

personal_finance_tracker/ │ ├── Pipfile ├── Pipfile.lock ├── README.md └── lib/ ├── models/ │ ├── init.py │ └── model_1.py ├── cli.py ├── debug.py └── helpers.py


## Installation

### Prerequisites
- Python 3.6+
- Pipenv

### Steps
1. **Clone the repository**:
   ```bash
   git clone <git@github.com:Elviscryptic1981/Expense-tracker.git>
   cd Expense-tracker

### Install dependencies:
pipenv install

### Activate the virtual environment:
pipenv shell

### Set up the database:
alembic upgrade head

## Usage
### Run the CLI application:

python lib/cli.py

## Commands
### Add a user:
python lib/cli.py add_user "John Doe"

### Add a transaction:
python lib/cli.py add_transaction 1 100.0 "Groceries"

### List users:
python lib/cli.py list_users

### List transactions for a user:
python lib/cli.py list_transactions 1

License
This project is licensed under the MIT License.

## Acknowledgements
SQLAlchemy
Alembic
Click
### Contact
For any questions or suggestions, please contact [Elvis Kimani] at [Elviskimani99@gmail.com].
