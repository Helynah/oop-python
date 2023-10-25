#Hellen M Wanyana
"""Breaking News module"""
from abc import ABC, abstractmethod


class Publisher(ABC):
    """Publisher class, Declares a set of methods for managing subscribers."""

    @abstractmethod
    def attach(self, subscriber):
        """Attach a subscriber to the publisher."""

    @abstractmethod
    def detach(self, subscriber):
        """Detach a subscriber from the publisher."""


class NewYorkTimesBreakingNews(Publisher):
    """NewYorkTimesBreakingNews class extends Publisher"""

    def __init__(self):
        """Init the Publisher."""
        self._subscriber = []

    def attach(self, subscriber):
        """Attach a new subscriber"""
        self._subscriber.append(subscriber)

    def detach(self, subscriber):
        "Detach/remove a subscriber"
        self._subscriber.remove(subscriber)

    def publish_news_item(self, news_category, news_title):
        """Publishes the news item/headline for each category"""
        print(f"NYT: Breaking News: {news_title} [category = {news_category}]")
        self.notify(news_category, news_title)

    def notify(self, news_category, news_title):
        """Notifies subscribers of the breaking news they subscribed to"""
        print("NYT: Notifying subscribers...")
        for subscriber in self._subscriber:
            subscriber.breaking_news(news_category, news_title)
