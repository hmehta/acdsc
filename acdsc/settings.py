#!/usr/bin/python3

from collections import OrderedDict

import click

from acdsc.validators import (
    is_car_list, is_track, is_track_subversion, max_clients, is_car,
    is_car_skin, is_tyre_list)


# NOTE: Assetto Corsa Dedicated Server requires non-anonymous user
steam_settings = {
    'username': 'acdscontrol',
    'password': 'Kekkonen69',
    'appid': 302550
}

server_settings = OrderedDict([
    ('NAME', {
        'default': 'acdsc default',
        'description': 'name of the server',
        'validator': click.STRING
    }),
    ('CARS', {
        'default': 'abarth500_s1;ferrari_458',
        'description': 'models of the cars allowed in the server (as in '
                       'content/cars -directory)',
        'validator': is_car_list
    }),
    ('TRACK', {
        'default': 'vallelunga',
        'description': 'track on the server (as in content/tracks -directory)',
        'validator': is_track
    }),
    ('CONFIG_TRACK', {
        'default': 'extended_circuit',
        'description': 'subversion of the track (as in content/tracks/TRACK/ '
                       '-directory)',
        'validator': is_track_subversion
    }),
    ('SUN_ANGLE', {
        'default': '-8',
        'description': 'angle of the position of the sun',
        'validator': click.INT
    }),
    ('MAX_CLIENTS', {
        'default': '15',
        'description': 'max number of clients (must be <= track\'s number of '
                       'pits)',
        'validator': max_clients
    }),
    ('RACE_OVER_TIME', {
        'default': '20',
        'description': 'time remaining in seconds to finish the race from the '
                       'moment the first one passes on the finish line',
        'validator': click.IntRange(1)
    }),
    ('ALLOWED_TYRES_OUT', {
        'default': '-1',
        'description': 'number of tyres allowed outside of track before '
                       'penalty (-1 disabled)',
        'validator': click.IntRange(-1, 4)
    }),
    ('UDP_PORT', {
        'default': '9600',
        'description': 'UDP port number',
        'validator': click.IntRange(1024, 49151)
    }),
    ('TCP_PORT', {
        'default': '9600',
        'description': 'TCP port number',
        'validator': click.IntRange(1024, 49151)
    }),
    ('HTTP_PORT', {
        'default': '8081',
        'description': 'Lobby port number (both UDP and TCP)',
        'validator': click.IntRange(1024, 49151)
    }),
    ('PASSWORD', {
        'default': 'something',
        'description': 'server password',
        'validator': click.STRING
    }),
    ('LOOP_MODE', {
        'default': '1',
        'description': 'the server restarts from the first track, to disable '
                       'this set it to 0',
        'validator': click.IntRange(0, 1)
    }),
    ('REGISTER_TO_LOBBY', {
        'default': '1',
        'description': 'this must not be touched',
        'validator': click.IntRange(1, 1)
    }),
    ('PICKUP_MODE_ENABLED', {
        'default': '1',
        'description': 'if 0 the server start in booking mode (do not use it).'
                       ' Warning: in pickup mode you have to list only a '
                       'circuit under TRACK and you need to list a least one '
                       'car in the entry_list',
        'validator': click.IntRange(0, 1)
    }),
    ('SLEEP_TIME', {
        'default': '1',
        'description': 'this must not be touched',
        'validator': click.IntRange(1, 1)
    }),
    ('VOTING_QUORUM', {
        'default': '75',
        'description': 'percentage of vote that is required for the SESSION '
                       'vote to pass',
        'validator': click.IntRange(1, 100)
    }),
    ('VOTE_DURATION', {
        'default': '20',
        'description': 'time in seconds for the vote duration',
        'validator': click.IntRange(1)
    }),
    ('BLACKLIST_MODE', {
        'default': '0',
        'description': 'ban player -> 0 = normal kick, rejoin possible, '
                       '1 = until server restart, 2 kick  player and add him '
                       'to blacklist',
        'validator': click.IntRange(0, 2)
    }),
    ('TC_ALLOWED', {
        'default': '1',
        'description': '0 -> no car can use TC, '
                       '1 -> only car provided with TC can use it; '
                       '2-> any car can use TC',
        'validator': click.IntRange(0, 2)
    }),
    ('ABS_ALLOWED', {
        'default': '1',
        'description': '0 -> no car can use ABS, '
                       '1 -> only car provided with ABS can use it; '
                       '2-> any car can use ABS',
        'validator': click.IntRange(0, 2)
    }),
    ('STABILITY_ALLOWED', {
        'default': '0',
        'description': 'Stability assist 0 -> OFF; 1 -> ON',
        'validator': click.IntRange(0, 1)
    }),
    ('AUTOCLUTCH_ALLOWED', {
        'default': '1',
        'description': 'Autoclutch assist 0 -> OFF; 1 -> ON',
        'validator': click.IntRange(0, 1)
    }),
    ('DAMAGE_MULTIPLIER', {
        'default': '0',
        'description': 'Damage from 0 (no damage) to 100 (full damage)',
        'validator': click.IntRange(0, 100)
    }),
    ('FUEL_RATE', {
        'default': '100',
        'description': 'Fuel usage from 0 (no fuel usage) to XXX (100 is the '
                       'realistic one)',
        'validator': click.IntRange(0)
    }),
    ('TYRE_WEAR_RATE', {
        'default': '100',
        'description': 'Tyre wear from 0 (no tyre wear) to XXX (100 is the '
                       'realistic one)',
        'validator': click.IntRange(0)
    }),
    ('CLIENT_SEND_INTERVAL_HZ', {
        'default': '15',
        'description': 'refresh rate of packet sending by the server. '
                       '10Hz = ~100ms. Higher number = higher MP quality = '
                       'higher bandwidth resources needed. Really high values '
                       'can create connection issues',
        'validator': click.IntRange(1)
    }),
    ('TYRE_BLANKETS_ALLOWED', {
        'default': '1',
        'description': 'at the start of the session or after the pitstop the '
                       'tyre will have the the optimal temperature',
        'validator': click.IntRange(0, 1)
    }),
    ('ADMIN_PASSWORD', {
        'default': 'kunos',
        'description': 'it\'s the password needed to be recognized as server '
                       'administrator: you can join the server using it to be '
                       'recognized automatically. Write on the game\'s chat '
                       '/help to see the command list',
        'validator': click.STRING
    }),
    ('QUALIFY_MAX_WAIT_PERC', {
        'default': '120',
        'description': 'this is the factor to calculate the remaining time in '
                       'a qualify session after the session is ended: '
                       '120 means that 120% of the session fastest lap '
                       'remains to end the current lap.',
        'validator': click.IntRange(1)
    }),
    ('WELCOME_MESSAGE', {
        'default': '',
        'description': 'path of a file who contains the server welome message',
        'validator': click.Path(exists=True, dir_okay=False, file_okay=True)
    }),
    ('START_RULE', {
        'default': '0',
        'description': 'false start penalty: 0 is car locked until start; '
                       '1 is teleport   ; 2 is drivethru (if race has 3 or '
                       'less laps then the Teleport penalty is enabled)',
        'validator': click.IntRange(0, 2)
    }),
    ('NUM_THREADS', {
        'default': '4',
        'description': 'number of server threads',
        'validator': click.IntRange(1)
    }),
    ('FORCE_VIRTUAL_MIRROR', {
        'default': '1',
        'description': '1 virtual mirror will be enabled for every client, '
                       '0 for mirror as optional',
        'validator': click.IntRange(0, 1)
    }),
    ('LEGAL_TYRES', {
        'default': 'V;E;HR;ST',
        'description': 'list of the tyre\'s shortnames that will be allowed '
                       'in the server.',
        'validator': is_tyre_list
    }),
    ('MAX_BALLAST_KG', {
        'default': '50',
        'description': 'the max total of ballast that can be added through '
                       'the admin command',
        'validator': click.IntRange(0)
    }),
    ('UDP_PLUGIN_LOCAL_PORT', {
        'default': '0',
        'description': 'see plugin example',
        'validator': click.IntRange(0, 49151)
    }),
    ('UDP_PLUGIN_ADDRESS', {
        'default': '',
        'description': 'see plugin example',
        'validator': click.STRING
    }),
    ('AUTH_PLUGIN_ADDRESS', {
        'default': '',
        'description': 'see plugin example',
        'validator': click.STRING
    }),
    ('RACE_GAS_PENALTY_DISABLED', {
        'default': '0',
        'description': '0 any cut will be penalized with the gas cut message; '
                       '1 no penalization will be forced, but cuts will be '
                       'saved in the race result json.',
        'validator': click.IntRange(0, 1)
    }),
    ('RESULT_SCREEN_TIME', {
        'default': '10',
        'description': 'seconds of result screen between racing sessions.',
        'validator': click.IntRange(1)
    }),
    ('RACE_EXTRA_LAP', {
        'default': '0',
        'description': 'if it\'s a timed race, with 1 the race will not end '
                       'when the time is over and the leader crosses the '
                       'line, but the latter will be forced to drive another '
                       'extra lap.',
        'validator': click.IntRange(0, 1)
    }),
    ('LOCKED_ENTRY_LIST', {
        'default': '0',
        'description': 'same as in booking mode, only players already '
                       'included in the entry list can join the server '
                       '(password not needed).',
        'validator': click.IntRange(0, 1)
    }),
    ('RACE_PIT_WINDOW_START', {
        'default': '25',
        'description': 'Pit window open at lap/minute (depends on the race '
                       'mode)',
        'validator': click.IntRange(1)
    }),
    ('RACE_PIT_WINDOW_END', {
        'default': '35',
        'description': 'Pit window closes at lap/minute (depends on the race '
                       'mode)',
        'validator': click.IntRange(1)
    }),
    ('REVERSED_GRID_RACE_POSITIONS', {
        'default': '8',
        'description': '0 = no additional race, 1toX = only those position '
                       'will be reversed for the next race, -1 = all the '
                       'position will be reversed (Retired players will be '
                       'on the last positions)',
        'validator': click.IntRange(0)
    }),
    ('TIME_OF_DAY_MULT', {
        'default': '1',
        'description': 'multiplier for the time of day',
        'validator': click.IntRange(1)
    })
])

session_settings = OrderedDict([
    ('BOOK',
     OrderedDict([
         ('NAME', {
            'default': 'Booking',
            'description': 'booking session - add this section only if your '
                           'server is in booking mode',
            'validator': click.STRING
            }),
         ('TIME', {
            'default': '5',
            'description': 'session length in minutes',
            'validator': click.IntRange(0)
            })])),
    ('PRACTICE',
     OrderedDict([
         ('NAME', {
            'default': 'Free Practice',
            'description': 'practice session',
            'validator': click.STRING
            }),
         ('TIME', {
            'default': '0',
            'description': 'session length in minutes',
            'validator': click.IntRange(0)
            }),
         ('IS_OPEN', {
            'default': '1',
            'description': '0 = no join, 1 = free join',
            'validator': click.IntRange(0, 1)
            })])),
    ('QUALIFY',
     OrderedDict([
         ('NAME', {
            'default': 'Qualify',
            'description': 'qualify session',
            'validator': click.STRING
            }),
         ('TIME', {
            'default': '5',
            'description': 'session length in minutes',
            'validator': click.IntRange(0)
            }),
         ('IS_OPEN', {
            'default': '1',
            'description': '0 = no join, 1 = free join',
            'validator': click.IntRange(0, 1)
            })])),
    ('RACE',
     OrderedDict([
         ('NAME', {
            'default': 'Race',
            'description': 'race session',
            'validator': click.STRING
            }),
         ('TIME', {
            'default': '0',
            'description': 'length of the timed races only if laps = 0',
            'validator': click.IntRange(0)
            }),
         ('IS_OPEN', {
            'default': '2',
            'description': '0 = no join, 1 = free join, '
                           '2 = free join until 20 seconds to the green light',
            'validator': click.IntRange(0, 2)
            }),
         ('LAPS', {
            'default': '5',
            'description': 'length of the lap races',
            'validator': click.IntRange(0)
            }),
         ('WAIT_TIME', {
            'default': '60',
            'description': 'seconds before the start of the session',
            'validator': click.IntRange(1)
            })]))
])

# NOTE: content/weather is not populated for dedicated server, these must be
# manually maintained :(
weather_types = ('1_heavy_fog', '2_light_fog', '3_clear', '4_mid_clear',
                 '5_light_clouds', '6_mid_clouds', '7_heavy_clouds')
weather_settings = OrderedDict([
    ('GRAPHICS', {
        'default': '3_clear',
        'description': 'weather type (as in content/weather -directory)',
        'validator': click.Choice(weather_types)
        }),
    ('BASE_TEMPERATURE_AMBIENT', {
        'default': '18',
        'description': 'temperature of the ambient',
        'validator': click.IntRange(-50, 60)
        }),
    ('VARIATION_AMBIENT', {
        'default': '2',
        'description': 'variation of the ambient temperature',
        'validator': click.INT
        }),
    ('BASE_TEMPERATURE_ROAD', {
        'default': '6',
        'description': 'relative road temperature: this value will be added '
                       'to the final ambient temp.',
        'validator': click.INT
        }),
    ('VARIATION_ROAD', {
        'default': '1',
        'description': 'variation of the road temperature',
        'validator': click.INT
        }),
    ('WIND_BASE_SPEED_MIN', {
        'default': '3',
        'description': 'min wind speed of the session',
        'validator': click.INT
        }),
    ('WIND_BASE_SPEED_MAX', {
        'default': '15',
        'description': 'max wind speed of the session',
        'validator': click.INT
        }),
    ('WIND_BASE_DIRECTION', {
        'default': '30',
        'description': 'base direction of the wind (0=North, 90=East, ...)',
        'validator': click.IntRange(0, 360)
        })
])

entry_list_settings = OrderedDict([
    ('DRIVERNAME', {
        'default': '',
        'description': 'Driver name',
        'validator': click.STRING
    }),
    ('GUID', {
        'default': '',
        'description': 'Steam GUID',
        'validator': click.STRING  # TODO: GUID validator (no duplicates)
    }),
    ('MODEL', {
        'default': 'bmw_m3_e30',
        'description': 'Car model',
        'validator': is_car
    }),
    ('TEAM', {
        'default': '',
        'description': 'Team name',
        'validator': click.STRING
    }),
    ('BALLAST', {
        'default': 0,
        'description': 'Additional weight (ballast) in kg',
        'validator': click.INT
    }),
    ('SKIN', {
        'default': '',
        'description': 'Car skin',
        'validator': is_car_skin
    }),
    ('SPECTATOR_MODE', {
        'default': 0,
        'description': 'Should always be 0',
        'validator': click.IntRange(0, 0)
    })
])
