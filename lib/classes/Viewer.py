from classes.Review import Review


class Viewer:

    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self._username

    def set_username(self, username):
        if type(username) == str and 6 <= len(username) <= 16:
            self._username = username

    username = property(get_username, set_username)

    def reviews(self):
        return [review for review in Review.all if review.viewer == self and isinstance(review, Review)]

    def reviewed_movies(self):
        return [review.movie for review in self.reviews()]

    def movie_reviewed(self, movie):
        return movie in self.reviewed_movies()

    def rate_movie(self, movie, rating):
        Review(self, movie, rating)
