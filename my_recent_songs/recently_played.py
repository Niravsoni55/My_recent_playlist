from collections import deque
from typing import Dict, List, Tuple

class RecentlyPlayed:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.song_user_pairs: Dict[str, deque] = {}


    def add_song(self, user: str, song: str) -> None:
        if user not in self.song_user_pairs:
            self.song_user_pairs[user] = deque([], maxlen=self.capacity)
        self.song_user_pairs[user].append(song)

    def get_recently_played(self, user: str) -> List[str]:
        if user not in self.song_user_pairs:
            return []
        return list(self.song_user_pairs[user])

