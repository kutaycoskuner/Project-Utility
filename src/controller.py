#
# -----------------------------------------------------------------------------
# ----- Libraries
# -----------------------------------------------------------------------------
from src.converters import markdown_to_lua as mdToLua                          # :: for implementing delay


# ==== Disabled Library

# -----------------------------------------------------------------------------
# ----- Classes
# -----------------------------------------------------------------------------
class Args:
    def __init__(self):
        self.args = None
        self.crt_Args()


class Controller:
    def __init__(self):
        self.mdToLua = mdToLua.MarkdownToLua(self)

    def start(self):
        # print('i am working')
        self.mdToLua.start()

# -----------------------------------------------------------------------------
# ----- Start
# ----------------------------------------------------------------------------- 
def main():
    controller = Controller()
    controller.start()