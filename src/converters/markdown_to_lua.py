#
# -----------------------------------------------------------------------------
# ----- Libraries
# -----------------------------------------------------------------------------
from lib import readWrite as rw                                          # :: utility read and write


# == Disabled Libraries

# -----------------------------------------------------------------------------
# ----- Classes
# -----------------------------------------------------------------------------
class MarkdownToLua():
    def __init__(self, controller):
        self.controller = controller

    def start(self):
        lines = rw.read('data/input/test.md')
        lines = self.adapt_luaTable(lines)
        rw.write('data/output/test.lua', lines)

    def adapt_path(path):
        pass

    def adapt_luaTable(self, lines):
        for ii in range(len(lines)):
            if lines[ii] == "# Content":
                del lines[0:ii]
                break
        return lines

# -----------------------------------------------------------------------------
# ----- Free Functions
# -----------------------------------------------------------------------------

