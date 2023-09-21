import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

class StarRating(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.stars = 0
        self.max_stars = 5
        self.star_buttons = []

        layout = QHBoxLayout()

        for i in range(self.max_stars):
            star_button = QPushButton("★", self)
            star_button.clicked.connect(self.onStarClicked)
            self.star_buttons.append(star_button)
            layout.addWidget(star_button)

        self.setLayout(layout)

    def onStarClicked(self):
        sender = self.sender()
        self.stars = self.star_buttons.index(sender) + 1
        self.updateStars()

    def updateStars(self):
        for i, star_button in enumerate(self.star_buttons):
            if i < self.stars:
                star_button.setStyleSheet("color: yellow;")
            else:
                star_button.setStyleSheet("color: gray;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Ocenianie Gwiazdkowe')
    layout = QVBoxLayout()

    rating_widget = StarRating()
    layout.addWidget(rating_widget)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())
