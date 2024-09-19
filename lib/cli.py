import click
from models import SessionLocal, engine, Base, User, Transaction

Base.metadata.create_all(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def add_user(name):
    db = SessionLocal()
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    click.echo(f"User {name} added with ID {user.id}")

@cli.command()
@click.argument('user_id')
@click.argument('amount', type=float)
@click.argument('description')
def add_transaction(user_id, amount, description):
    db = SessionLocal()
    transaction = Transaction(amount=amount, description=description, user_id=user_id)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    click.echo(f"Transaction added with ID {transaction.id}")

@cli.command()
def list_users():
    db = SessionLocal()
    users = db.query(User).all()
    for user in users:
        click.echo(f"ID: {user.id}, Name: {user.name}")

@cli.command()
@click.argument('user_id')
def list_transactions(user_id):
    db = SessionLocal()
    transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    for transaction in transactions:
        click.echo(f"ID: {transaction.id}, Amount: {transaction.amount}, Description: {transaction.description}")

if __name__ == "__main__":
    cli()
