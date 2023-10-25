"""Weather parser module"""


class WeatherParser:
    """Weather parser class"""

    def __init__(self, weather_data):
        self.response = weather_data

    def get_feels_like_f(self):
        """returns the current feel of the temperature"""
        return self.response["current_condition"][0]["FeelsLikeF"]

    def get_cloud_cover(self):
        """gets the cloud cover"""
        return self.response["current_condition"][0]["cloudcover"]

    def get_weather_description(self):
        """ "describes the weather"""
        return self.response["current_condition"][0]["weatherDesc"][0]["value"]

    def get_sunset(self):
        """gets the sunset"""
        return self.response["weather"][0]["astronomy"][0]["sunset"]

    def get_sunrise(self):
        """gets the sunrise"""
        return self.response["weather"][0]["astronomy"][0]["sunrise"]
