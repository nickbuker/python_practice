def longest_possible(play):
    print songs
    times = []
    for song in songs:
        times.append((make_seconds(song['playback']), song['title']))

    timer = 0
    best_song = False
    for tup in times:
        if tup[0] > timer and tup[0] <= play:
            timer = tup[0]
            best_song = tup[1]
    return best_song


def make_seconds(play_time):
    return (int(play_time[0:2]) * 60) + int(play_time[3::])
