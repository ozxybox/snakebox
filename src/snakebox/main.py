import sys

from snakebox.cat   import CommandCat
from snakebox.ls    import CommandLs
from snakebox.mkdir import CommandMkdir
from snakebox.mv    import CommandMv

g_commands = {}

g_commands["cat"]    = CommandCat()
g_commands["ls"]     = CommandLs()
g_commands["mkdir"]  = CommandMkdir()
g_commands["mv"]     = CommandMv()

def main():
    cmd = g_commands[sys.argv[1]]
    cmd.parse_args(sys.argv[2:])
    cmd.run(sys.stdin, sys.stdout, sys.stderr)
