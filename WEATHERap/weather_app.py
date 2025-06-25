import sys
import requests
import geocoder
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

API_KEY = "7da38f220ada56522cbd671ae1fb6bf9"


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.weather_label = QLabel("Weather: ", self)
        layout.addWidget(self.weather_label)

        self.temperature_label = QLabel("Temperature: ", self)
        layout.addWidget(self.temperature_label)

        self.refresh_button = QPushButton("Refresh", self)
        layout.addWidget(self.refresh_button)
        self.refresh_button.clicked.connect(self.get_weather_data)

        self.get_weather_data()

    def get_location(self):
        g = geocoder.ip('me')  # Fetch location based on IP address
        return g.latlng  # Return latitude and longitude as a list

    def get_weather_data(self):
        location = self.get_location()
        if location:
            latitude, longitude = location
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"

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