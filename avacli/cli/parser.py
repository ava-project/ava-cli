
from .commands import Commands

# print(commands.login)

class ArgsParser(object):

    def __init__(self, arguments):
        self.args = arguments
        self.func = None
        self.commands = Commands()

    def dispatch(self):
        cmd = getattr(self.commands, self.args['ARGS'][0], None)
        if callable(cmd):
            cmd()
        else:
            print('no')
