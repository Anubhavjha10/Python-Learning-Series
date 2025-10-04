import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.result_widgets = [self.temperature_label, self.emoji_label, self.description_label]
        self.animation_group = QParallelAnimationGroup(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(300, 300, 400, 550)
        self.setWindowIcon(QIcon('weather_icon.png'))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        vbox = QVBoxLayout()
        vbox.setSpacing(15)
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addStretch()
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addStretch()

        self.setLayout(vbox)

        for widget in self.findChildren(QLabel):
            widget.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setWordWrap(True)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                  stop: 0 #e0f2ff, stop: 1 #b0dfff);
            }
            QLabel, QPushButton, QLineEdit {
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel#city_label {
                font-size: 28px;
                color: #005073;
            }
            QLineEdit#city_input {
                font-size: 24px;
                padding: 10px;
                border: 2px solid #a2d2ff;
                border-radius: 15px;
                background-color: #f0faff;
            }
            QLineEdit#city_input:focus {
                border: 2px solid #0077c2;
            }
            QPushButton#get_weather_button {
                font-size: 22px;
                font-weight: bold;
                color: white;
                background-color: #0077c2;
                padding: 12px;
                margin-top: 5px;
                border: none;
                border-radius: 15px;
            }
            QPushButton#get_weather_button:hover {
                background-color: #005d99;
            }
            QPushButton#get_weather_button:pressed {
                background-color: #00446b;
            }
            QLabel#temperature_label {
                font-size: 80px;
                font-weight: bold;
                color: #1a237e;
            }
            /* --- Yahaan Badlav Kiya Gaya Hai --- */
            QLabel#emoji_label {
                font-size: 110px;
                /* Yeh line alag-alag OS ke liye best emoji font select karegi */
                font-family: 'Segoe UI Emoji', 'Apple Color Emoji', 'Noto Color Emoji', sans-serif;
            }
            QLabel#description_label {
                font-size: 35px;
                color: #4682b4;
            }
        """)

        for widget in self.result_widgets:
            opacity_effect = QGraphicsOpacityEffect(widget)
            widget.setGraphicsEffect(opacity_effect)
            opacity_effect.setOpacity(0.0)

        self.get_weather_button.clicked.connect(self.run_weather_fetch)
        self.city_input.returnPressed.connect(self.run_weather_fetch)

    def run_weather_fetch(self):
        for widget in self.result_widgets:
            widget.graphicsEffect().setOpacity(0.0)
        self.get_weather()

    def get_weather(self):
        api_key = "a72fbd01245a2da0defd62af7af9c28b"
        city = self.city_input.text()

        if not city:
            self.display_error("Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            self.display_weather(data)
        except requests.exceptions.HTTPError as http_err:
            status_code = http_err.response.status_code
            if status_code == 404:
                self.display_error(f"'{city}'\nCity Not Found")
            else:
                self.display_error(f"HTTP Error: {status_code}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\nPlease check your internet")
        except requests.exceptions.Timeout:
            self.display_error("Request Timed Out")
        except requests.exceptions.RequestException:
            self.display_error("An error occurred")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 25px; color: #d9534f; font-weight: bold;")
        self.temperature_label.setText(message)
        self.fade_in(self.temperature_label)

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("")

        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"].title()

        self.temperature_label.setText(f"{temperature_c:.1f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

        self.fade_in_all_results()

    def fade_in(self, widget):
        self.animation_group.clear()
        anim = QPropertyAnimation(widget.graphicsEffect(), b"opacity")
        anim.setDuration(600)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation_group.addAnimation(anim)
        self.animation_group.start()

    def fade_in_all_results(self):
        self.animation_group.clear()
        for widget in self.result_widgets:
            anim = QPropertyAnimation(widget.graphicsEffect(), b"opacity")
            anim.setDuration(600)
            anim.setStartValue(0.0)
            anim.setEndValue(1.0)
            anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.animation_group.addAnimation(anim)
        self.animation_group.start()

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 781:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "🧐"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

