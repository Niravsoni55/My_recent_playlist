# Recently Played Songs In-Memory Store

This Python project implements Create an in-memory store for recently played songs that can accommodate N songs per user, with a fixed initial capacity. This store must have the capability to store a list of song-user pairs, with each song linked to a user. It should also be able to fetch recently played songs based on the user and eliminate the least recently played songs when the store becomes full.

## Project Structure

The project has the following directory structure:

my_recent_songs/
recently_played.py

tests/
test_recently_played.py


- `my_recent_songs/` directory contains the implementation of the RecentlyPlayed class in the `recently_played.py` file.
- `tests/` directory contains the test code in the `test_recently_played.py` file.

## Installation and Execution

1. Clone the repository: 

    https://github.com/Niravsoni55/My_recent_playlist

2. Change into the project directory: 

    cd My_recent_Songs

3. Install the required dependencies:
  ```
    pip install -r requirements.txt
  ```

4. Run the tests:
  ```
    python -m pytest
  ```
  - This will execute the `test_recently_played.py` file and verify the functionality of the RecentlyPlayed class


Note: You can use the RecentlyPlayed class in your own code by importing it:

```python
from my_recent_songs.recently_played import RecentlyPlayed

#Create an instance of RecentlyPlayed and use its methods
```
 

