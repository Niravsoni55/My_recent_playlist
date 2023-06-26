from my_recent_songs.recently_played import RecentlyPlayed

def test_recently_played():
    rp = RecentlyPlayed(3)

    rp.add_song('user1', 'S1')
    rp.add_song('user1', 'S2')
    rp.add_song('user1', 'S3')
    assert rp.get_recently_played('user1') == ['S1', 'S2', 'S3']

    rp.add_song('user1', 'S4')
    assert rp.get_recently_played('user1') == ['S2', 'S3', 'S4']

    rp.add_song('user1', 'S2')
    assert rp.get_recently_played('user1') == ['S3', 'S4', 'S2']

    rp.add_song('user1', 'S1')
    assert rp.get_recently_played('user1') == ['S4', 'S2', 'S1']

    rp.add_song('user2', 'S1')
    assert rp.get_recently_played('user1') == ['S4', 'S2', 'S1']
    assert rp.get_recently_played('user2') == ['S1']