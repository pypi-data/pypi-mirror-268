import click
import os

from meerkat import email as send_email, ping as send_ping, sms as send_sms, slack as send_slack
from meerkat.api import get_user_token

@click.group()
def meerkat():
    pass

@meerkat.command()
def ping():
    """Trigger ping sound to play from your local machine"""
    send_ping()

@meerkat.command()
@click.argument('message', type=str)
def email(message):
    """Send an email to your MeerkatIO email address with MESSAGE content"""
    send_email(message=message)

@meerkat.command()
@click.argument('message', type=str)
def sms(message):
    """Send an SMS to your MeerkatIO email address with MESSAGE content"""
    send_sms(message=message)

@meerkat.command()
@click.argument('message', type=str)
def slack(message):
    """Send a Slack direct message to your MeerkatIO email address with MESSAGE content"""
    send_slack(message=message)

@meerkat.command()
def login():
    """Login to MeerkatIO Platform and setup local environment"""
    email = click.prompt("Enter Email")
    password = click.prompt("Enter Password", hide_input=True)
    token = get_user_token(email, password)

    if not token:
        click.echo("Invalid email or password.")
        return

    #save token to user HOME and set OS env
    with open(os.path.expanduser("~") + "/.meerkat", "w") as file:
        file.write(token)
    os.environ["MEERKAT_TOKEN"] = token

    click.echo(f"\nMeerkatIO initialized successfully!")

if __name__ == "__main__":
    meerkat()