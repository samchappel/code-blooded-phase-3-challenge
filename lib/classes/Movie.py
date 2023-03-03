from classes.Review import Review


class Movie:

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self._title 

    def set_title(self, title):
        if isinstance(title, str) and 1 <= len(title):
            self._title = title

    title = property(get_title, set_title)

    def reviews(self):
        return [review for review in Review.all if review.movie == self and isinstance(review, Review)]

    def reviewers(self):
        return list({review.viewer for review in self.reviews()})

    def average_rating(self):
        ratings = [review.rating for review in self.reviews()]
        if len(ratings) == 0:
            return 0
        return sum(ratings) / len(ratings)

    @classmethod
    def highest_rated(cls):
        pass
