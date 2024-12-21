import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup, QSizePolicy, QWidget, QStackedWidget
from ultralytics import YOLO
from capture_window import CaptureWindow
from depth_window import DepthWindow
import numpy as np

model = YOLO('models/yolov8n-seg.pt')


class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)
        self.auto_mode = False

    def initUI(self):
        self.setWindowTitle('Camera Application')
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.camera_page = QWidget()
        self.camera_layout = QVBoxLayout(self.camera_page)
        self.radio_button_layout = QHBoxLayout()
        self.radio_auto = QRadioButton('Auto Mode')
        self.radio_manual = QRadioButton('Manual Mode')
        self.radio_manual.setChecked(True)
        self.radio_button_group = QButtonGroup()
        self.radio_button_group.addButton(self.radio_manual)
        self.radio_button_group.addButton(self.radio_auto)
        self.radio_button_layout.addWidget(self.radio_auto)
        self.radio_button_layout.addWidget(self.radio_manual)
        self.radio_manual.toggled.connect(self.switch_mode)
        self.camera_layout.addLayout(self.radio_button_layout)

        self.video_display = QLabel()
        self.video_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.video_display.setScaledContents(True)
        self.camera_layout.addWidget(self.video_display)

        self.capture_button = QPushButton('Capture Photo')
        self.capture_button.clicked.connect(self.capture_photo)
        self.camera_layout.addWidget(self.capture_button)

        self.central_widget.addWidget(self.camera_page)
        self.capture_window = CaptureWindow(self.central_widget)
        self.central_widget.addWidget(self.capture_window)
        self.depth_window = DepthWindow(self.central_widget)
        self.central_widget.addWidget(self.depth_window)

        self.resize(800, 600)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            results = model(frame)
            annotated_frame = frame.copy()
            for result in results:
                for box in result.boxes.xyxy:
                    x1, y1, x2, y2 = map(int, box[:4])
                    cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            rgb_image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            qt_image = QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888)
            self.video_display.setPixmap(QPixmap.fromImage(qt_image))

    def capture_photo(self):
        ret, frame = self.cap.read()
        if ret:
            self.capture_window.display_image(frame)
            self.central_widget.setCurrentIndex(1)

    def switch_mode(self):
        self.auto_mode = self.radio_auto.isChecked()

    def closeEvent(self, event):
        self.cap.release()
