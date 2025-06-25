import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

API_KEY = "7da38f220ada56522cbd671ae1fb6bf9"


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 200)

        self.weather_label = QLabel("Weather: ", self)
        self.weather_label.move(20, 50)

        self.temperature_label = QLabel("Temperature: ", self)
        self.temperature_label.move(20, 80)

        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.move(150, 120)
        self.refresh_button.clicked.connect(self.get_weather_data)

        self.get_weather_data()

    def get_weather_data(self):
        city = "London"  # You can implement location services to get user's location dynamically
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()
            weather = data["weather"][0]["description"].capitalize()
            temperature = data["main"]["temp"]
            self.weather_label.setText(f"Weather: {weather}")
            self.temperature_label.setText(f"Temperature: {temperature}°C")
        except requests.exceptions.RequestException:
            self.weather_label.setText("Weather data not available.")
            self.temperature_label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
