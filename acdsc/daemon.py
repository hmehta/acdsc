#!/usr/bin/python3

import atexit
import os
import signal
import subprocess as sub
import sys
import time


class Daemon(object):

    def __init__(self, pidfile):
        self.pidfile = pidfile

    def daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError as err:
            sys.stderr.write('fork #1 failed: {0}\n'.format(err))
            sys.exit(1)

        # decouple from parent environment
        os.chdir('/')
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError as err:
            sys.stderr.write('fork #2 failed: {0}\n'.format(err))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(os.devnull, 'r')
        so = open(os.devnull, 'a+')
        se = open(os.devnull, 'a+')

        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        atexit.register(self.delpid)

        pid = str(os.getpid())
        with open(self.pidfile, 'w+') as f:
            f.write(pid + '\n')

    def delpid(self):
        os.remove(self.pidfile)

    def getpid(self):
        with open(self.pidfile, 'r') as pf:
            return int(pf.read().strip())

    def start(self):
        # Check for a pidfile to see if the daemon already runs
        try:
            pid = self.getpid()
        except IOError:
            pid = None

        if pid:
            message = 'pidfile {0} already exist. Daemon already running?\n'
            sys.stderr.write(message.format(self.pidfile))
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        # Get the pid from the pidfile
        try:
            pid = self.getpid()
        except IOError:
            pid = None

        if not pid:
            message = 'pidfile {0} does not exist.  Daemon not running?\n'
            sys.stderr.write(message.format(self.pidfile))
            return  # not an error in a restart

        # Try killing the daemon process
        try:
            while 1:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            e = str(err.args)
            if e.find('No such process') > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
                else:
                    print (str(err.args))
                    sys.exit(1)

    def restart(self):
        self.stop()
        self.start()

    def run(self):
        pass


class ACDaemon(Daemon):

    def __init__(self, config):
        super().__init__(config['pidfile'])
        self.cwd = config['server-path']

    def run(self):
        # TODO: logs?
        sub.run('./acServer', cwd=self.cwd, shell=True)
