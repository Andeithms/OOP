class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show(self):
        print(f'{self.name}: {self.duration} min')


class Album:
    def __init__(self, title, group):
        self.title = title
        self.group = group
        self.track_list = []

    def get_tracks(self):
        print(f'Альбом {self.title} группы {self.group}:')
        for track in self.track_list:
            track.show()

    def add_track(self, track):
        self.track_list.append(track)

    def get_durations(self):
        album_duration = 0
        for track in self.track_list:
            album_duration += track.duration
        print(f'Длительность альбома {self.title}: {album_duration} min')


track_1_1 = Track('Damnation', 4)
track_1_2 = Track('Royal Beggars', 3)
track_1_3 = Track('Modern Misery', 5)

track_2_1 = Track('Ignit', 3)
track_2_2 = Track('Mental Health', 2)
track_2_3 = Track('Brixton', 3)

album_1 = Album('Holy hell', 'Architects')
album_2 = Album('Phoenix', 'Zebrahead')

album_1.add_track(track_1_1)
album_1.add_track(track_1_2)
album_1.add_track(track_1_3)
album_2.add_track(track_2_1)
album_2.add_track(track_2_2)
album_2.add_track(track_2_3)

album_1.get_durations()
album_2.get_durations()
album_2.get_tracks()
album_1.get_tracks()
