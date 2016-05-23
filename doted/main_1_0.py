# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from major_1.minor_0.app.Doted import Doted


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Initialisation
    doted = Doted()
    doted.run()
    
    sys.exit(app.exec_())
