# Music Library System

A small Python library that models songs for a music streaming service and
maintains aggregate statistics about the catalog. Built as a lab exercise on
class attributes and class methods.

## Features

- Create `Song` objects with a `name`, `artist`, and `genre`.
- Automatically tracks, across every instance:
  - Total number of songs created (`Song.count`).
  - All unique genres (`Song.genres`).
  - All unique artists (`Song.artists`).
  - Number of songs per genre (`Song.genre_count`).
  - Number of songs per artist (`Song.artist_count`, also exposed as `Song.artists_count`).

## Project Structure

```
.
├── lib/
│   ├── song.py              # Song class implementation
│   └── testing/
│       ├── conftest.py
│       └── song_test.py     # Pytest suite
├── Pipfile / Pipfile.lock   # Python dependencies (pipenv)
├── pytest.ini
└── README.md
```

## Installation

This project uses [pipenv](https://pipenv.pypa.io/) and Python 3.8+.

```bash
pipenv install
pipenv shell
```

## Usage

```python
from lib.song import Song

Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Sara Smile", "Hall and Oates", "Pop")

Song.count           # -> 3
Song.genres          # -> ['Rap', 'Pop']
Song.artists         # -> ['Jay Z', 'Beyonce', 'Hall and Oates']
Song.genre_count     # -> {'Rap': 1, 'Pop': 2}
Song.artist_count    # -> {'Jay Z': 1, 'Beyonce': 1, 'Hall and Oates': 1}
```

Each new `Song` instance triggers the following class methods automatically
from `__init__`:

| Method                   | Effect                                                    |
|--------------------------|-----------------------------------------------------------|
| `add_song_to_count`      | Increments `count` by 1.                                  |
| `add_to_genres`          | Appends `genre` to `genres` if not already present.       |
| `add_to_artists`         | Appends `artist` to `artists` if not already present.     |
| `add_to_genre_count`     | Increments `genre_count[genre]` (creates key if missing). |
| `add_to_artists_count`   | Increments `artist_count[artist]` (creates key if missing). |

## Running Tests

```bash
pytest
```

Expected output:

```
6 passed
```

## Screenshot

<!-- Add a screenshot of the passing test run or a usage demo here, e.g.: -->
<!-- ![Tests passing](docs/tests-passing.png) -->

## License

See [LICENSE.md](LICENSE.md).
