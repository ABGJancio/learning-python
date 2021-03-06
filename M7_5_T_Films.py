"""World of films at hand."""


class Films:
    """This is a class for films."""

    def __init__(self, title, release_year, genre, times_played):
        """
        Construct for Films class.

        Parameters:
            title (str)         : title of the movie
            release_year (int)  : yaer of movie release
            genre (str)         : definition of the genre of the movie
            times_played (int)  : how many times movir was played
        """
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.times_played = times_played

        # Variables
        self.times_played = 0

    def play(self, step=1):
        """Increase the number of plays of a given title by step."""
        self.times_played += step

    def __str__(self):
        """Inform about title and year of movie release."""
        return f"{self.title} ({self.release_year})"

    def film_library(self):
        """Create the list of movies."""
        # for _ in range
        pass


class Serials(Films):
    """This is a subclass for serials."""

    def __init__(self, title, release_year, genre, episode_no, season_no, times_played):
        """
        Construct for Serials class.

        Parameters:
            title (str)         : title of the serial
            release_year (int)  : yaer of serial season release
            genre (str)         : definition of the genre of the serial
            episode_no (int)    : episode number of the series  
            season_no (int)     : season number of the series
            times_played (int)  : how many times serial was played

        """
        super().__init__(title, release_year, genre, times_played)
        self.episode_no = episode_no
        self.season_no = season_no

    def __str__(self):
        """Inform about number of season and number of episode of the series title."""
        if self.season_no >= 1 and self.season_no <= 9:
            s_no = 'S0'+str(self.season_no)
        else:
            s_no = 'S'+str(self.season_no)
        if self.episode_no >= 1 and self.episode_no <= 9:
            e_no = 'E0'+str(self.episode_no)
        else:
            e_no = 'E'+str(self.episode_no)
        se_no = s_no + e_no
        return f"{self.title} {se_no}"


film1 = Films('Mission: Impossible', 1996, 'Action', 113752)
serial1 = Serials('The 100', 1984, 'Sci-Fi', 3, 1, 68652)
film_library = [film1, serial1]
print(film_library)

print(film1)
print(serial1)
