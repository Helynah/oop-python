# Hellen M Wanyana
"""Subscribercmodule"""
from abc import ABC, abstractmethod


class Subscriber(ABC):
    """Subscriber class"""

    @abstractmethod
    def breaking_news(self, news_category, news_title):
        """Receives breaking news and reacts depending on the category"""


class BusinessNewsSubscriber(Subscriber):
    """Receives Business beaking news"""

    def breaking_news(self, news_category, news_title):
        """Reacts to only business news"""
        if news_category == "business":
            print(f"SUBSCRIBER: {news_category.title()} Breaking: {news_title}")


class PoliticsNewsSubscriber(Subscriber):
    """Receives Political breaking news"""

    def breaking_news(self, news_category, news_title):
        """Reacts to only political news"""
        if news_category == "politics":
            print(f"SUBSCRIBER: {news_category.title()} Breaking: {news_title}")


class KeyWordSubscriber(Subscriber):
    """Receives breaking news with a keyword input by subscriber"""

    def __init__(self, key_word):
        """Initialize the keyWord"""
        self.key_word = key_word

    def breaking_news(self, news_category, news_title):
        """Receive breaking news and filter based on the specified keyword and category."""
        if news_category.lower() == "politics" and self.key_word in news_title.lower():
            print(f"SUBSCRIBER: Filter [{self.key_word}]: {news_title}")
