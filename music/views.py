from django.http import Http404
from django.shortcuts import render

from .data import LIKED_IDS, PLAYLISTS, RECENT_IDS, SONGS, TRENDING_IDS, songs_by_ids


def login_page(request):
    return render(request, "tunes/login.html")


def home(request):
    context = {
        "liked": songs_by_ids(LIKED_IDS),
        "playlists": PLAYLISTS[:6],
        "trending": songs_by_ids(TRENDING_IDS),
    }
    return render(request, "tunes/home.html", context)


def player(request, pk):
    position = next((i for i, song in enumerate(SONGS) if song["id"] == pk), None)
    if position is None:
        raise Http404("No such song")
    context = {
        "song": SONGS[position],
        "prev_song": SONGS[position - 1],  # index -1 wraps to the last song
        "next_song": SONGS[(position + 1) % len(SONGS)],
    }
    return render(request, "tunes/player.html", context)


def account(request):
    return render(request, "tunes/account.html")


def about(request):
    return render(request, "tunes/about.html")


def playlists(request):
    return render(request, "tunes/playlists.html", {"playlists": PLAYLISTS})


def playlist(request, pk):
    chosen = next((p for p in PLAYLISTS if p["id"] == pk), None)
    if chosen is None:
        raise Http404("No such playlist")
    return render(
        request,
        "tunes/songs.html",
        {"title": chosen["name"], "songs": songs_by_ids(chosen["song_ids"])},
    )


def liked(request):
    return render(request, "tunes/songs.html", {"title": "Liked Songs", "songs": songs_by_ids(LIKED_IDS)})


def recent(request):
    return render(request, "tunes/songs.html", {"title": "Recent Music", "songs": songs_by_ids(RECENT_IDS)})


def trending(request):
    return render(request, "tunes/songs.html", {"title": "Trending now", "songs": songs_by_ids(TRENDING_IDS)})
