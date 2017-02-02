"""
Main file of AVA CLI.
"""

import sys
import click
import requests

from .version import __version__


url = 'http://localhost:8080'


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__)
def cli():
    """
    CLI to allow a user to control AVA.
    """
    pass


@cli.command()
def login():
    """
    Log in to AVA Cloud.
    """

    username = click.prompt('Please enter your username')
    password = click.prompt('Password', hide_input=True)
    payload = {
        'username': username,
        'password': password
    }
    try:
        r = requests.post(url + '/user/login', data=payload)
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
    click.echo(r.text)
    click.echo('Logged In.')


@cli.command()
def logout():
    """
    Log ouf of AVA Cloud.
    """

    try:
        r = requests.delete(url + '/user/logout')
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
    click.echo(r.text)
    click.echo('Logged Out.')


@cli.command()
@click.argument('keyword', required=False)
def list(keyword=''):
    """
    List all plugin available.
    """

    try:
        r = requests.get(url + '/plugins')
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        click.echo('Error: Problem happenned', err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo('Error: Unable to end the request with the server',
                   err=True)
        sys.exit(1)
    click.echo(r.text)


@cli.command()
@click.argument('id', type=int)
def info(id):
    """
    Get information about a plugin.
    """

    try:
        r = requests.get(url + '/plugins/' + id)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 404:
            click.echo('Error: Plugin not found', err=True)
        else:
            click.echo('Error: Problem happenned', err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo('Error: Unable to end the request with the server',
                   err=True)
        sys.exit(1)
    click.echo(r.text)


@cli.command()
@click.argument('id', type=int)
def install(id):
    """
    Install a plugin.
    """

    try:
        r = requests.get(url + '/plugins/' + id + '/download')
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 400:
            click.echo('Error: Plugin already installed', err=True)
        elif r.status_code == 401:
            click.echo('Error: You\'re not logged in', err=True)
        elif r.status_code == 404:
            click.echo('Error: Plugin doesn\'t exist', err=True)
        else:
            click.echo('Error: Problem happenned', err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo('Error: Unable to end the request with the server',
                   err=True)
        sys.exit(1)
    click.echo(r.text)
    click.echo('Plugin installed')


@cli.command()
@click.argument('id', type=int)
def remove(id):
    """
    Remove an installed plugin.
    """

    try:
        r = requests.delete(url + '/plugins/' + id)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 400:
            click.echo('Error: Plugin already removed', err=True)
        elif r.status_code == 401:
            click.echo('Error: You\'re not logged in', err=True)
        elif r.status_code == 404:
            click.echo('Error: Plugin not found', err=True)
        else:
            click.echo('Error: Problem happenned', err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo('Error: Unable to end the request with the server',
                   err=True)
        sys.exit(1)
    click.echo(r.text)
    click.echo('Plugin removed')


@cli.command()
@click.argument('id', type=int)
def enable(id):
    """
    Enable an installed plugin.
    """

    try:
        r = requests.patch(url + '/plugins/' + id + '/enable')
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 400:
            click.echo('Error: Plugin already enabled', err=True)
        elif r.status_code == 401:
            click.echo('Error: You\'re not logged in', err=True)
        elif r.status_code == 404:
            click.echo('Error: Plugin not downloaded', err=True)
        else:
            click.echo('Error: Problem happenned', err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo('Error: Unable to end the request with the server',
                   err=True)
        sys.exit(1)
    click.echo(r.text)
    click.echo('Plugin enabled')


@cli.command()
@click.argument('id', type=int)
def disable(id):
    """
    Disable an installed plugin.
    """

    try:
        r = requests.patch(url + '/plugins/' + id + '/disable')
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 400:
            click.echo('Error: Plugin already disabled', err=True)
        elif r.status_code == 401:
            click.echo('Error: You\'re not logged in', err=True)
        elif r.status_code == 404:
            click.echo('Error: Plugin not downloaded', err=True)
        else:
            click.echo('Error: Problem happenned', err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo('Error: Unable to end the request with the server',
                   err=True)
        sys.exit(1)
    click.echo(r.text)
    click.echo('Plugin disabled')


@cli.command()
@click.argument('id', type=int)
def play(id):
    """
    Enable daemon listening.
    """

    try:
        r = requests.patch(url + '/playback/play')
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        click.echo('Error: Problem happenned', err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo('Error: Unable to end the request with the server',
                   err=True)
        sys.exit(1)
    click.echo(r.text)
    click.echo('Listening enabled')


@cli.command()
@click.argument('id', type=int)
def pause(id):
    """
    Disable daemon listening.
    """

    try:
        r = requests.patch(url + '/playback/pause')
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        click.echo('Error: Problem happenned', err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo('Error: Unable to end the request with the server',
                   err=True)
        sys.exit(1)
    click.echo(r.text)
    click.echo('Listening disabled')


@cli.command()
def update():
    """
    Update all plugins.
    """

    click.echo('Debug')
