import cProfile
from gui import SortGUI

g = SortGUI()
cProfile.run('g.run()', sort = 'time')

