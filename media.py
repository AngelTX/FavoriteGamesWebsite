import webbrowser

class Game():
    """This class provides a way to store game related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, game_title, poster_image,
                 trailer_youtube):
        """Initiates a movie Object with the specified arguments"""
        self.title = game_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens game trailer in the webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
