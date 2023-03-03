class Review:

    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        Review.add_to_reviews(self)

    @classmethod
    def add_to_reviews(cls, review):
        cls.all.append(review)

    def get_rating(self):
        return self._rating 
    
    def set_rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5:
            self._rating = rating

    rating = property(get_rating, set_rating)

    def get_viewer(self):
        return self._viewer

    def set_viewer(self, viewer):
        from classes.Viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer

    viewer = property(get_viewer, set_viewer)

    def get_movie(self):
        return self._movie

    def set_movie(self, movie):
        from classes.Movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie

    movie = property(get_movie, set_movie)


