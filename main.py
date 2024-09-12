from json import load
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


with open("config.json", "r", encoding="utf-8") as config_file:
    config = load(config_file)
    windows_count = config.get("window_count")
    text = config.get("text")
    print(config)


class RandomWindow(QMainWindow):
    def __init__(self, window_text, height, width):
        super().__init__()
        self.text_edit = QTextEdit()
        self.text_edit.setText(window_text)
        font = self.text_edit.font()
        font.setPointSize(24)  # Increase the font size to 24 points
        self.text_edit.setFont(font)
        self.setCentralWidget(self.text_edit)
        self.setWindowTitle(window_text)
        self.setGeometry(random.randint(0, width), random.randint(0, height), 300, 200)

def main(num_windows):
    app = QApplication(sys.argv)  # Create a single QApplication instance
    screens = QApplication.screens()
    primary_screen = screens[0]
    sr = primary_screen.size()  # sr --- screen resolution

    window_width = sr.width()
    window_height = sr.height()

    windows = []  # Store the window instances in a list

    if num_windows:
        for i in range(num_windows):
            window = RandomWindow(text, height=window_height, width=window_width)
            window.show()
            windows.append(window)  # Add the window instance to the list

    elif not num_windows:
        while True:
            window = RandomWindow(text, height=window_height, width=window_width)
            window.show()
            windows.append(window)  # Add the window instance to the list

    else:
        print("Invalid argument!")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(windows_count)
