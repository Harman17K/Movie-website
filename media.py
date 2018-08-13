import webbrowser
# above file is imported.


class Movie():
    # A class name Movie is made.
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # A function is made which stores title-
        # ,stoyline,poster URL, trailer URL.
        # self is essential to use while making-
        # a function in python.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Again a function is made which will-
        # help to play trailer.
        webbrowser.open(self.trailer_youtube_url)
        # webbrowser.open helps us to open any-
        # link which is provided to it.
