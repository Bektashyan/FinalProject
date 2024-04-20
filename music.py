from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///playlist.db', echo=True)


Base = declarative_base()


class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    name = Column(String)


    tracks = relationship('Track', back_populates='playlist')

class Track(Base):
    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)
    duration = Column(Integer)


    playlist_id = Column(Integer, ForeignKey('playlists.id'))
    playlist = relationship('Playlist', back_populates='tracks')


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

playlist1 = Playlist(name='My Playlist')
session.add(playlist1)
session.commit()

track1 = Track(title='Song 1', artist='Artist 1', duration=180, playlist=playlist1)
track2 = Track(title='Song 2', artist='Artist 2', duration=240, playlist=playlist1)
session.add_all([track1, track2])
session.commit()


playlist = session.query(Playlist).filter_by(name='My Playlist').first()
print("Playlist:", playlist.name)
print("Tracks:")
for track in playlist.tracks:
    print(track.title, "-", track.artist)

track1.duration = 200
session.commit()

session.delete(track2)
session.commit()

session.close()
