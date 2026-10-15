"""All the content is plain Python lists: no database."""

SONGS = [
    {"id": 1, "title": "Kabisado", "artist": "IV of Spades", "cover": "covers/kabisado.jpeg"},
    {"id": 2, "title": "Sino", "artist": "Unique Salonga", "cover": "covers/sino.jpeg"},
    {"id": 3, "title": "Circles", "artist": "Post Malone", "cover": "covers/circles.jpeg"},
    {"id": 4, "title": "Blinding Lights", "artist": "The Weeknd", "cover": "covers/The_Weeknd_-_blinding_lights.jpeg"},
    {"id": 5, "title": "I knew it, i knew you", "artist": "Taylor Swift", "cover": "covers/i knew it i knew you.jpeg"},
    {"id": 6, "title": "Magbalik", "artist": "Callalily", "cover": "covers/magbalik.jpeg"},
    {"id": 7, "title": "Chasing cars", "artist": "Snow", "cover": "covers/chasing cars.jpeg"},
    {"id": 8, "title": "Saksi and langit", "artist": "December Avenue", "cover": "covers/saksi.jpeg"},
    {"id": 9, "title": "Fireworks", "artist": "Katy perry", "cover": "covers/fireworks.jpeg "},
    {"id": 10, "title": "Juno", "artist": "Sabrina Carpenter", "cover": "covers/juno.jpeg"},
    {"id": 11, "title": "Money Trees", "artist": "Kendrick Lamar & Jay Rock", "cover": "covers/money tree.jpeg"},
    {"id": 12, "title": "NOKIA", "artist": "Drake", "cover": "covers/nokia.jpeg"},
     {"id": 13, "title": "Bituin ng Mindanao", "artist": "Ugat ng Lahi", "cover": "covers/rene.jpeg"},
]

# Which songs appear in each list (by song id).
LIKED_IDS = [1, 2, 3, 4, 5, 6]
RECENT_IDS = [10, 4, 9, 2, 7, 12]
TRENDING_IDS = [4, 3, 5, 10, 9, 7]

PLAYLISTS = [
    {
        "id": number,
        "name": f"Playlist #{number}",
        "song_ids": [((number * 2 + offset) % len(SONGS)) + 1 for offset in range(4)],
    }
    for number in range(1, 6)
]


def songs_by_ids(ids):
    by_id = {song["id"]: song for song in SONGS}
    return [by_id[i] for i in ids]
