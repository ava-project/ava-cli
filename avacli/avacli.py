"""
Main file of AVA CLI.
"""

import click
import requests

from .version import __version__


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__)
def cli():
    """
    CLI to allow a user to control AVA.
    """
    pass


@cli.command()
@click.option('--email', '-e', nargs=1, help='email',
              prompt='Please enter your email')
@click.option('--password', '-p', prompt=True, hide_input=True,
              confirmation_prompt=True, help='password')
def login(email, password):
    """
    Log in to AVA Cloud.
    """

    payload = {
        'action': 'authenticate',
        'payload': {
            'email': email,
            'password': password
        }
    }
    r = requests.post('http://localhost:3000', json=payload)
    # click.echo('Debug : ' + username)


@cli.command()
def logout():
    """
    Log ouf of AVA Cloud.
    """

    payload = {
        'action': 'logout'
    }
    r = requests.post('http://localhost:3000', json=payload)


@cli.command()
@click.argument('keyword', required=False)
def list(keyword=''):
    """
    List all plugin available.
    """

    payload = {
        'action': 'list-plugins',
        'payload': {
            'keyword': keyword
        }
    }
    r = requests.post('http://localhost:3000', json=payload)


@cli.command()
@click.argument('id', type=int)
def info(id):
    """
    Get information about a plugin.
    """

    payload = {
        'action': 'info-plugin',
        'payload': {
            'id': id
        }
    }
    r = requests.post('http://localhost:3000', json=payload)


@cli.command()
@click.argument('id', type=int)
def install(id):
    """
    Install a plugin.
    """

    payload = {
        "action": "install-plugin",
        "payload": {
            "id": id
        }
    }
    r = requests.post('http://localhost:3000', json=payload)


@cli.command()
@click.argument('id', type=int)
def remove(id):
    """
    Remove an installed plugin.
    """

    payload = {
        "action": "remove-plugin",
        "payload": {
            "id": id
        }
    }
    r = requests.post('http://localhost:3000', json=payload)


@cli.command()
def update():
    """
    Update all plugins.
    """

    click.echo('Debug')
