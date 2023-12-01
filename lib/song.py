class Song:
    all = []
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    def __init__(self,name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_song_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artist(self.artist)
        
    @classmethod
    def add_to_song_count(cls):
        cls.count += 1
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        Song.add_to_genre_count(genre)
    @classmethod
    def add_to_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        Song.add_to_artist_count(artist)
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1   

# hotel_lobby = Song("Hotel Lobby", "Migos", "Rap")
# mo_bamba = Song("Mo Bamba", "Shack Wes", "Rap")
# country_road = Song("Country Road", "Katy Perry", "Pop")
# billy_jean = Song("Billy Jean", "Michael Jackson", "Pop")
# print(f"SongCount: {Song.count}, Artists: {Song.artists}, Genres: {Song.genres} GenreCount: {Song.genre_count} Artist_Count: {Song.artist_count}")