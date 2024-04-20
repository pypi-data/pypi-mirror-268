"""
ipython.py - Sopel IPython Console Module
Copyright © 2014, Elad Alfassa <elad@fedoraproject.org>
Copyright © 2022, dgw, technobabbl.es
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
from __future__ import unicode_literals, absolute_import, print_function, division

import sys

from sopel import plugin

from IPython.terminal.embed import InteractiveShellEmbed


@plugin.commands('console')
@plugin.require_admin('Only admins can start the interactive console')
def interactive_shell(bot, trigger):
    """Starts an interactive IPython console"""
    if bot.memory.get('ipython_console', None):
        bot.say('Console already running')
        return
    if not sys.__stdout__.isatty():
        bot.say('A tty is required to start the console')
        return
    if bot._daemon:
        bot.say("Can't start console when running as a daemon")
        return

    # Backup stderr/stdout wrappers
    old_stdout = sys.stdout
    old_stderr = sys.stderr

    # IPython wants actual stderr and stdout
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    bot.memory['ipython_console'] = InteractiveShellEmbed(
        banner1='Sopel interactive shell (embedded IPython)',
        banner2='`bot` and `trigger` are available; type `exit` to quit',
        exit_msg='Interactive shell closed',
    )

    bot.say('Starting console')
    bot.memory['ipython_console']()  # blocks until console is closed (Ctrl-D etc.)
    del bot.memory['ipython_console']

    # Restore stderr/stdout wrappers
    sys.stdout = old_stdout
    sys.stderr = old_stderr
