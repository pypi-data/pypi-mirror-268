from monterey.tools.dialogs import Dialog
from monterey.tools.frontend import Frontend
from monterey.tools.inputs import Input
from monterey.tools.live_table import LiveTable
from monterey.tools.loaders import Loader
from monterey.tools.logger import Logger
from monterey.tools.preconditions import Preconditions
from monterey.tools.progress_bar import ProgressBar
from monterey.tools.text import Text

#==============================================================================

class Tools:
    def __init__ (self):
        self.text = Text()
        self.tools.frontend = Frontend()
        self.tools.dialog = Dialog()
        self.tools.inputs = Input()
        self.tools.live_table = LiveTable()
        self.tools.loader = Loader
        self.tools.logger = Logger
        self.tools.preconditions = Preconditions
        self.tools.progress_bar = ProgressBar

#==============================================================================
