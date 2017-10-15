#!/usr/bin/python3

import os
import shutil
import subprocess as sub
import tarfile
import tempfile

from urllib.request import urlopen

import click

from acdsc.settings import steam_settings

url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz'


def has_steamcmd(path):
    steamcmd = os.path.join(path, 'steamcmd.sh')
    return os.path.exists(path) and os.path.exists(steamcmd)


def install_steamcmd(path):
    click.secho(
        'ERROR: steamcmd not found from {}!'.format(path),
        fg='red')
    click.confirm(
        'Do you wish to attempt installation from {}?'.format(url),
        abort=True)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    click.echo('..downloading {}'.format(url))
    response = urlopen(url)
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    with temp_file as fh:
        fh.write(response.read())
    click.echo('..extracting to {}'.format(path))
    tar = tarfile.open(temp_file.name)
    tar.extractall(path)
    tar.close()
    os.unlink(temp_file.name)
    click.secho('SteamCMD succesfully installed!', fg='green')


def assert_working_steamcmd(steamcmd):
    cp = sub.run('{} +quit'.format(steamcmd),
                 stdout=sub.PIPE,
                 stderr=sub.PIPE,
                 shell=True)
    cp.check_returncode()


def update_acds(steamcmd):
    click.secho('Updating Assetto Corsa Dedicated Server', fg='green')
    cmd = ('{steamcmd} +login {username} {password} '
           '+@sSteamCmdForcePlatformType windows +app_update {appid} '
           '+quit').format(steamcmd=steamcmd,
                           username=steam_settings['username'],
                           password=steam_settings['password'],
                           appid=steam_settings['appid'])
    sub.call(cmd, shell=True)
