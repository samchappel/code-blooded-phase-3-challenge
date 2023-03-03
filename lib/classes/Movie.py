from classes.Review import Review


class Movie:

    all = []

    def __init__(self, title):
        self.title = title
        self.__class__.all.append(self)

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
        movies_with_ratings = [movie for movie in cls.all if movie.reviews()]
        if not movies_with_ratings:
            return None
        highest_rated_movie = movies_with_ratings[0]
        for movie in movies_with_ratings:
            if movie.average_rating() > highest_rated_movie.average_rating():
                highest_rated_movie = movie
        if highest_rated_movie not in cls.all:
            cls.all.append(highest_rated_movie)
        return highest_rated_movie
