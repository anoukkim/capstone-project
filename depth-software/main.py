import sys
from PyQt5.QtWidgets import QApplication
from camera_app import CameraApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    camera_app = CameraApp()
    camera_app.show()
    sys.exit(app.exec_())
