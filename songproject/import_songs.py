import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'songproject.settings')
django.setup()


import json
from server.models import Song, SongRating


def import_songs():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(script_dir, 'data', 'playlist.json')

    with open(json_file, 'r') as file:
        data = json.load(file)

    for i in range(len(data['id'])):
        song_id = data['id'][str(i)]
        title = data['title'][str(i)]
        
        if Song.objects.filter(song_id=song_id).exists():
            print(f"Song with ID {song_id} already exists. Skipping import.")
            continue

        rating_id = data.get('rating_id', {}).get(str(i), None)
        rating_value = data.get('rating', {}).get(str(i), 0)
        if rating_id:
            song_rating = SongRating.objects.get(id=rating_id)
        else:
            song_rating = SongRating.objects.create(rating=rating_value)

        song = Song(
            song_id=song_id,
            title=title,
            danceability=data.get('danceability', {}).get(str(i), 0),
            energy=data.get('energy', {}).get(str(i), 0),
            key=data.get('key', {}).get(str(i), 0),
            loudness=data.get('loudness', {}).get(str(i), 0),
            mode=data.get('mode', {}).get(str(i), 0),
            acousticness=data.get('acousticness', {}).get(str(i), 0),
            instrumentalness=data.get('instrumentalness', {}).get(str(i), 0),
            liveness=data.get('liveness', {}).get(str(i), 0),
            valence=data.get('valence', {}).get(str(i), 0),
            tempo=data.get('tempo', {}).get(str(i), 0),
            duration_ms=data.get('duration_ms', {}).get(str(i), 0),
            time_signature=data.get('time_signature', {}).get(str(i), 0),
            num_bars=data.get('num_bars', {}).get(str(i), 0),
            num_sections=data.get('num_sections', {}).get(str(i), 0),
            num_segments=data.get('num_segments', {}).get(str(i), 0),
            song_class=data.get('class', {}).get(str(i), 0),
            rating=song_rating
        )

        song.save()

    print('Successfully imported songs data into the database')

if __name__ == '__main__':
    import_songs()
