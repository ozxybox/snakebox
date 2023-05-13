import sys

from cat   import CommandCat
from ls    import CommandLs
from mkdir import CommandMkdir
from mv    import CommandMv

g_commands = {}

g_commands["cat"]    = CommandCat()
g_commands["ls"]     = CommandLs()
g_commands["mkdir"]  = CommandMkdir()
g_commands["mv"]     = CommandMv()

def main():
    cmd = g_commands[sys.argv[1]]
    cmd.parse_args(sys.argv[2:])
    cmd.run(sys.stdin, sys.stdout, sys.stderr)

if __name__ == '__main__':
    main()
