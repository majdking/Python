class MediaError(Exception):
    """Custom exception for media-related errors."""
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj
    
class Movie:
    """Parent class representing a movie."""
    def __init__(self, title, year, director, duration):
        if title.strip() == '':
            raise ValueError('Title cannot be empty')
        self.title = title
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        self.year = year
        if director.strip() == '':
            raise ValueError('Director cannot be empty')
        self.director = director
        if duration < 1:
            raise ValueError('Duration must be positive')
        self.duration = duration

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    def __init__(self):
        self.items = []

    def add(self, media_item):
        if not isinstance(media_item, Movie) and not isinstance(media_item, TVSeries):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)

    def __str__(self):
        if not self.items:
            return "Media Catalogue (empty)"
        movies = self.get_movies()
        series = self.get_tv_series()
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        if movies:
            result += '=== MOVIES ===\n'
            for i,item in enumerate(movies, start=1):
                result += f'{i}. {item}\n'
        if series:
            result += '=== TV SERIES ===\n'
            for i,item in enumerate(series, start=1):
                result += f'{i}. {item}\n'       
        return result

    def get_movies(self):
        return [item for item in self.items if type(item) == Movie]

    def get_tv_series(self):
        return [item for item in self.items if type(item) == TVSeries]




class TVSeries(Movie):
    """Child class representing an entire TV series."""
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)
        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        self.seasons = seasons
        self.total_episodes = total_episodes
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'


try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    # movie2 = Movie('Dances with Wolves', 1990, 'Kevin Costner', 224)
    catalogue = MediaCatalogue()
    catalogue.add(movie1)
    #catalogue.add(movie2)
    series1 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 4, 5, 62)
    catalogue.add(series1)
    series2 = TVSeries('The Sopranos', 1999, 'David Chase', 55, 6, 86)
    catalogue.add(series2)
    print(catalogue)
    print(catalogue.get_movies())

#     movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
#     movie2 = Movie('Dances with Wolves', 1990, 'Kevin Costner', 224)
#     movie3 = Movie('Annie Hall', 1977, 'Woody Allen', 93)
#     MediaCatalogue1 = MediaCatalogue()
#     MediaCatalogue1.add(movie1)
#     MediaCatalogue1.add(movie2)
#     MediaCatalogue1.add(movie3)
except ValueError as e:
    print(f'Validation Error: {e}')
except MediaError as e:
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj}: {type(e.obj)}')
    
# else:
#     # print(movie1)
#     print(MediaCatalogue1)

print(movie1.__doc__)
print(series1.__doc__)