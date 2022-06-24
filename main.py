from PySide2.QtWidgets import QApplication

from form import *
import sys

aplicatie = QApplication(sys.argv)

main_form = Form()
main_form.show()

aplicatie.exec_()

