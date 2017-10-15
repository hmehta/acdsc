#!/usr/bin/python3

import os

import click

# Validators TODO:
# NAME cannot start with number
# *_PORT - check for collisions


# stub validators
def is_car():
    pass


def is_car_skin():
    pass


def is_car_list():
    pass


def is_track():
    pass


def is_track_subversion():
    pass


def max_clients():
    pass


def is_tyre_list():
    pass


class SteamPath(click.Path):

    def convert(self, value, param, ctx):
        return super(SteamPath, self).convert(
            os.path.join(ctx.params['steam_path'], value), param, ctx)
