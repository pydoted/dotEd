# -*- coding: utf-8 -*-

# Copyright (c) 2016 Victor Nea, Morvan Lassauzay, Matthieu Dien, Marwan Ghanem
# This file is part of dotEd.
#
# dotEd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dotEd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dotEd.  If not, see <http://www.gnu.org/licenses/>.

import sys

from PyQt5.QtWidgets import QApplication

from doted.major_1.minor_1.app.Doted import Doted


def main(args=None):
    '''Entry point.

    Argument(s):
    args (List[str]): Arguments in command line (default None)
    '''
    app = QApplication(sys.argv)

    # Initialisation
    doted = Doted()
    doted.run()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
