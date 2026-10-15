# Spotibai (simple, no database)

A small Django web app with clickable pages, based on a Figma wireframe. No database, admin, login system or JavaScript.

## Run it

```bash
pip install -r requirements.txt
python manage.py runserver
```

Open http://127.0.0.1:8000/login/ and click **Log in**.

## Pages

- `/login/` login screen (opens Home)
- `/` home
- `/play/<id>/` song page with previous and next icons
- `/account/` account
- `/liked/`, `/recent/`, `/trending/` song lists
- `/playlists/` and `/playlists/<id>/` playlists

## Where things are

- `music/data.py` the songs, playlists and which songs each list shows
- `music/views.py` one short view per page
- `music/templates/music/base.html` the shared page: head, sidebar, header, footer. Every other page extends it and only fills in its own content
- `music/templates/music/song_card.html` the song card that pages include
- `music/static/music/style.css` all styling; the color palette is the variables at the top
