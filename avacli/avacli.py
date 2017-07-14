"""
Main file of AVA CLI.
"""

import sys
import click
import requests

from .version import __version__


url = 'http://localhost:8001'


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
    Login to AVA Cloud.
    """

    email = click.prompt('Please enter your email')
    password = click.prompt('Password', hide_input=True)
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


@cli.command()
def logout():
    """
    Logout of AVA Cloud.
    """

    try:
        r = requests.get(url + '/logout')
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 400:
            click.echo('Error: Bad credentials', err=True)
        elif r.status_code == 401:
            click.echo('Error: You are not logged in', err=True)
        else:
            click.echo('Error: Problem happenned', err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo('Error: Unable to end the request with the server',
                   err=True)
        sys.exit(1)
    click.echo('Logged Out.')


@cli.command()
def me():
    """
    Retrieve user information from AVA Cloud.
    """

    try:
        r = requests.get(url + '/me')
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
    click.echo('Username: ' + r.json()['username'])
    click.echo('Email: ' + r.json()['email'])
    click.echo('First Name: ' + r.json()['first_name'])
    click.echo('Last Name: ' + r.json()['last_name'])


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
    plugins = r.json()
    click.echo('Plugin List:')
    for plugin in plugins:
        click.echo('#########################')
        click.echo('Name: ' + plugin['name'])
        click.echo('ID: ' + str(plugin['id']))
        click.echo('Version: ' + plugin['version'])
        click.echo('Description: ' + plugin['description'])


@cli.command()
@click.argument('plugin_name', type=str)
def info(plugin_name):
    """
    Get information about a plugin.
    """

    try:
        r = requests.get(url + '/plugins/' + plugin_name)
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
    plugin = r.json()
    click.echo('Name: ' + plugin['name'])
    click.echo('Version: ' + plugin['version'])
    click.echo('Description: ' + plugin['description'])


@cli.command()
@click.argument('plugin_name', type=str)
@click.argument('author', type=str)
def download(plugin_name, author):
    """
    Dowload a plugin.
    """

    try:
        r = requests.get(url + '/plugins/' + author + '/' +
                         plugin_name + '/download')
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 400:
            click.echo('Error: Plugin already Downloaded', err=True)
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
    click.echo('Plugin downloaded')


@cli.command()
@click.argument('plugin_name', type=str)
def install(plugin_name):
    """
    Install a plugin.
    """

    try:
        r = requests.get(url + '/plugins/' + plugin_name + '/install')
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
@click.argument('plugin_name', type=str)
def remove(plugin_name):
    """
    Remove an installed plugin.
    """

    try:
        r = requests.delete(url + '/plugins/' + plugin_name)
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
@click.argument('plugin_name', type=str)
def enable(plugin_name):
    """
    Enable an installed plugin.
    """

    try:
        r = requests.patch(url + '/plugins/' + plugin_name + '/enable')
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
@click.argument('plugin_name', type=str)
def disable(plugin_name):
    """
    Disable an installed plugin.
    """

    try:
        r = requests.patch(url + '/plugins/' + plugin_name + '/disable')
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
def play():
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
def pause():
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
@click.argument('plugin_name', type=str)
def update(plugin_name):
    """
    Update all plugins.
    """

    try:
        r = requests.patch(url + '/plugins/' + plugin_name)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 400:
            click.echo('Plugin already up to date', err=True)
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
    click.echo('Plugin updated')
