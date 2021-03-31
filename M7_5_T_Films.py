"""World of films at hand."""

import random
import datetime


class AttrDisplay:
    """
    Provide an inheritable display overload method.

    Can be mixed into any class, and will work on any instance.
    """

    def __getattr__(self, attr):
        """Delegate attributes."""
        return getattr(self, attr)

    def gatherAttrs(self):
        """Make the list of all attributes."""
        attrs = []
        for key in self.__dict__:
            attrs.append(f'{key}={getattr(self, key)}')
        return ', '.join(attrs)

    def __repr__(self):
        """
        Show instances with their class names and a name:value pair.

        It applays for each attribute stored on the instance itself 
        (but not attrs inherited from its classes).
        """
        return f'[{self.__class__.__name__}: {self.gatherAttrs()}]'


class Films(AttrDisplay):
    """This is a class for films."""

    def __init__(self, title, release_year, genre, times_played):
        """
        Construct for Films class.

        Parameters:
            title (str)         : title of the movie
            release_year (int)  : yaer of movie release
            genre (str)         : definition of the genre of the movie
            times_played (int)  : how many times movie was played
        """
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.times_played = times_played

        # Variables
        # self.times_played = 0

    def play(self, step=1):
        """Increase the number of plays of a given title by step."""
        self.times_played += step

    def __str__(self):
        """Inform about title and year of movie release."""
        return f'{self.title} ({self.release_year})'

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
        return f'{self.title}' f' S{self.season_no:02d}'+f'E{self.episode_no:02d}'





def get_movies():
    """."""
    movies = sorted([movie for movie in films_library if movie.__class__ ==
                     Films], key=lambda by_title: by_title.__dict__['title'])
    return movies


def get_series():
    """."""
    series = sorted([serie for serie in films_library if serie.__class__ ==
                     Serials], key=lambda by_year: by_year.__dict__['release_year'])
    return series


def search():
    """."""
    picture = input('Podaj tytuł: ')
    picture_attrs = [
        item for item in films_library if item.__dict__['title'] == picture][0]
    print(AttrDisplay.__repr__(picture_attrs))
    return


def generate_views():
    """."""
    rand_pic = random.choice(films_library)
    rand_pic.__dict__['times_played'] += random.randint(1, 100)
    return AttrDisplay.__repr__(rand_pic)


def accelerate_views(times):
    """."""
    for i in range(times-1):
        generate_views()
    return


def top_titles(content_type):
    """."""
    top_pictures = sorted([picture for picture in films_library if picture.__class__ ==
                           content_type], key=lambda by_year: by_year.__dict__['times_played'])
    print(
        f'Nr 1. {top_pictures[-1]},\nNr 2. {top_pictures[-2]},\nNr 3. {top_pictures[-3]}')
    return


if __name__ == '__main__':
    print('\nBiblioteka filmów')

    film1 = Films('The Green Mile', 1999, 'Drama', 976398)
    film2 = Films('Mission: Impossible', 1996, 'Action', 113752)
    film3 = Films('News of the World', 2020, 'Drama/Western', 13441)
    film4 = Films('Schindler\'s List', 1993, 'Drama', 357428)
    film5 = Films('Django', 2012, 'Wetern', 476035)

    serial1 = Serials('The 100', 1984, 'Sci-Fi', 3, 1, 68652)
    serial2 = Serials('Proven Innocent', 2019, 'Drama', 12, 1, 168)
    serial3 = Serials('New Amsterdam', 2021, 'Drama', 4, 3, 35)
    serial4 = Serials('Game of Thrones', 2011, 'Fantasy', 9, 1, 359856)
    serial5 = Serials('Twin Peaks', 1991, 'Thriller', 19, 2, 105068)

    films_library = [film1, film2, film3, film4, film5,
                     serial1, serial2, serial3, serial4, serial5]

    generate_views()

    print(f'\nNajpopularniejsze filmy i seriale dnia {datetime.date.today()}:')
    top_titles(Serials)