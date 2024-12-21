from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap
import cv2
from utils.depth_utils import generate_depth_image


class CaptureWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.image_label = QLabel()
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.image_label)

        self.model_button = QPushButton('Generate Depth Image')
        self.model_button.clicked.connect(self.generate_3d_model)
        self.layout.addWidget(self.model_button)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.back_to_camera)
        self.layout.addWidget(self.back_button)

    def display_image(self, image):
        self.captured_image = image
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        qt_image = QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(qt_image))

    def generate_3d_model(self):
        if self.captured_image is not None:
            depth_image = generate_depth_image(self.captured_image)
            self.parent().widget(2).display_image(depth_image)
            self.parent().setCurrentIndex(2)

    def back_to_camera(self):
        self.parent().setCurrentIndex(0)
