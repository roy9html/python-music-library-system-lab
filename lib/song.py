class Song:
    """Represents a song and maintains class-level statistics across all songs."""

    # Total number of Song instances created.
    count = 0
    # Unique genres seen across all songs.
    genres = []
    # Unique artists seen across all songs.
    artists = []
    # Mapping of genre -> number of songs in that genre.
    genre_count = {}
    # Mapping of artist -> number of songs by that artist.
    artist_count = {}
    # Alias kept for the spec name `artists_count`.
    artists_count = artist_count

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level stats whenever a new song is instantiated.
        self.__class__.add_song_to_count()
        self.__class__.add_to_genres(self.genre)
        self.__class__.add_to_artists(self.artist)
        self.__class__.add_to_genre_count(self.genre)
        self.__class__.add_to_artists_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Append `genre` to the genres list if not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Append `artist` to the artists list if not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the song count for `genre`, creating the key if missing."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increment the song count for `artist`, creating the key if missing."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
        cls.artists_count = cls.artist_count
