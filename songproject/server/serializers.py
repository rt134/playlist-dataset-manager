from rest_framework import serializers
from .models import Song, SongRating, SongUserRating

class SongRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRating
        fields = ['id', 'rating']

class SongSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = [
            'song_id', 'title', 'danceability', 'energy', 'key', 'loudness', 'mode', 
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 
            'duration_ms', 'time_signature', 'num_bars', 'num_sections', 'num_segments', 
            'song_class', 'rating'
        ]

    def get_rating(self, obj):
        return getattr(obj.rating, 'rating', None)

class SongUserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongUserRating
        fields = ['song', 'rating']
