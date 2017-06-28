import sys
import click
import requests

from click.testing import CliRunner


url = 'http://localhost:8001'


def test_login():
    @click.command()
    @click.option('--email', prompt=True)
    @click.option('--password', prompt=True)
    def login(email, password):
        payload = {
            'email': email,
            'password': password
        }
        try:
            r = requests.post(url + '/login', data=payload)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if r.status_code == 400:
                click.echo('Error: Bad credentials', err=True)
            else:
                click.echo('Error: Problem happenned', err=True)
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            click.echo('Error: Unable to end the request with the server',
                       err=True)
            sys.exit(1)
        click.echo('Logged In.')

    runner = CliRunner()
    result = runner.invoke(login, input='test@test.com\navarocks\n')
    assert not result.exception
    assert result.output == 'Email: test@test.com\nPassword: avarocks\n' \
        'Logged In.\n'


def test_me():
    @click.command()
    def me():
        try:
            r = requests.get(url + '/me')
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if r.status_code == 400:
                click.echo('Error: Bad credentials', err=True)
            elif r.status_code == 401:
                click.echo('Error: Not logged in', err=True)
            else:
                click.echo('Error: Problem happenned', err=True)
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            click.echo('Error: Unable to end the request with the server',
                       err=True)
            sys.exit(1)
        click.echo('Username: ' + r.json()['username'])
        click.echo('Email: ' + r.json()['email'])
        click.echo('First Name: ' + r.json()['first_name'])
        click.echo('Last Name: ' + r.json()['last_name'])

    runner = CliRunner()
    result = runner.invoke(me)
    assert not result.exception
    assert result.output == 'Username: test\nEmail: test@test.com\n' \
        'First Name: \nLast Name: \n'


def test_logout():
    @click.command()
    def logout():
        try:
            r = requests.get(url + '/logout')
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if r.status_code == 400:
                click.echo('Error: Bad credentials', err=True)
            elif r.status_code == 401:
                click.echo('Error: Not logged in', err=True)
            else:
                click.echo('Error: Problem happenned', err=True)
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            click.echo('Error: Unable to end the request with the server',
                       err=True)
            sys.exit(1)
        click.echo('Logged Out.')

    runner = CliRunner()
    result = runner.invoke(logout)
    assert not result.exception
    assert result.output == 'Logged Out.\n'
