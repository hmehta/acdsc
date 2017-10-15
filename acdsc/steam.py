#!/usr/bin/python3

import os
import subprocess as sub
import tarfile
import tempfile

from urllib.request import urlopen

import click


url = 'http://repo.steampowered.com/steam/archive/precise/steam_latest.tar.gz'


def has_acds(steam_path, server_path):
    steamapps = os.path.join(steam_path, 'steamapps')
    return (os.path.exists(steam_path) and
            os.path.exists(steamapps) and
            os.path.exists(server_path))


def has_steam():
    cp = sub.run(
        'command -v steam', stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
    return cp.returncode == os.EX_OK


# TODO: Steam requires make, gpg, ca-certificates and 32bit libgcc1
# Steam
def install_steam():
    click.secho('ERROR: steam not found!', fg='red')
    click.confirm(
        'Do you wish to attempt installation from {}?'.format(url),
        abort=True)
    click.echo('..downloading {}'.format(url))
    response = urlopen(url)
    temp_dir = tempfile.TemporaryDirectory()
    steam_dir = os.path.join(temp_dir.name, 'steam')
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    with temp_file as fh:
        fh.write(response.read())
    click.echo('..extracting to {}'.format(steam_dir))
    tar = tarfile.open(temp_file.name)
    tar.extractall(temp_dir.name)
    tar.close()
    os.unlink(temp_file.name)
    click.echo('..running sudo make install')
    sub.call('sudo make install', cwd=steam_dir, shell=True)
    temp_dir.cleanup()
    click.secho('Steam succesfully installed!', fg='green')
