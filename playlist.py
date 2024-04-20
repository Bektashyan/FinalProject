class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Category: {self.name}"


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.playlists = []

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def __str__(self):
        return f"User: {self.username}, Password: {self.password}"


class Playlist(Category):
    def __init__(self, name):
        super().__init__(name)
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def __str__(self):
        return f"Playlist: {self.name}, Tracks: {len(self.tracks)}"


class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"Track: {self.title} by {self.artist}, Duration: {self.duration} seconds"


# Example usage:
if __name__ == "__main__":
    user1 = User("JohnDoe", "john@example.com")

    # Create a playlist
    playlist1 = user1.create_playlist("My Playlist")

    # Create tracks
    track1 = Track("Song 1", "Artist 1", 180)
    track2 = Track("Song 2", "Artist 2", 240)

    # Add tracks to the playlist
    playlist1.add_track(track1)
    playlist1.add_track(track2)

    # Print user info
    print(user1)

    # Print playlist info
    print(playlist1)

    # Print tracks in the playlist
    for track in playlist1.tracks:
        print(track)
