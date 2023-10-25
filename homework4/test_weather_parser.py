"""Test Weather module"""

import unittest
import json
import sys
from typing import IO
from weather_parser import WeatherParser


def test_weather_parser(filename: IO[str]) -> json:
    """Loads duplicate data from a JSON file"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(0)


class WeatherParserTestCase(unittest.TestCase):
    """Tests all functions in the WeatherParser class"""

    def setUp(self) -> None:
        """Sets up the test fixture"""
        self.weather_data = test_weather_parser("test_data.json")
        self.weather = WeatherParser(self.weather_data)

    def test_get_feels_like_f(self) -> None:
        """Is the FeelsLikeF the same as that in the json file?"""
        self.assertEqual(self.weather.get_feels_like_f(), "56")

    def test_get_cloud_cover(self) -> None:
        """Is the cloudcover the same as that in the json file?"""
        self.assertEqual(self.weather.get_cloud_cover(), "100")

    def test_get_weather_description(self) -> None:
        """Is the weatherDesc the same as that in the json file?"""
        self.assertEqual(self.weather.get_weather_description(), "Light rain, mist")

    def test_get_sunrise(self) -> None:
        """TIs the sunrise the same as that in the json file"""
        self.assertEqual(self.weather.get_sunrise(), "07:04 AM")

    def test_get_sunset(self) -> None:
        """Is the sunset the same as that in the json file?"""
        self.assertEqual(self.weather.get_sunset(), "05:53 PM")


if __name__ == "__main__":
    unittest.main()
