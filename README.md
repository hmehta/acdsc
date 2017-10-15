# acdsc - Assetto Corsa Dedicated Server Control

A simple CLI tool for configuring and managing Assetto Corsa Dedicated Server

## Example usage

```bash
## Settings
# print out current server settings
acdsc server show

# set setting values
acdsc server set [--with-defaults] --name "my ac server #001" --time-of-day-mult "2" ...

## Sessions
# print out current sessions
acdsc server session-list

# add a session
acdsc server add-session

# remove a session
acdsc server del-session

## Weather
# display currently configured weathers
acdsc server weather-list

# add a weather
acdsc server add-weather

# remove a weather
acdsc server del-weather

## Entry list
# set driver details in entry list
acdsc set-entry --car 0 --drivername "foobar" --ballast 50 ...

# generate anonymous entries to entry list
acdsc gen-entries car1 car2 car3

## Server management
# run AC Dedicated Server
acdsc start -f|-b

# check status (and logs [TODO])
acdsc status

# stop AC Dedicated Server
acdsc stop

# update AC Dedicated Server (you can also use --autoupdate -flag with start)
acdsc update
```
