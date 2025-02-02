from django.db import models

class SongRating(models.Model):
    rating = models.FloatField(default=0)

    def __str__(self):
        return f"Rating: {self.rating}"

class Song(models.Model):
    song_id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    danceability = models.FloatField(default=0)
    energy = models.FloatField(default=0)
    key = models.IntegerField(default=0)
    loudness = models.FloatField(default=0)
    mode = models.IntegerField(default=0)
    acousticness = models.FloatField(default=0)
    instrumentalness = models.FloatField(default=0)
    liveness = models.FloatField(default=0)
    valence = models.FloatField(default=0)
    tempo = models.FloatField(default=0)
    duration_ms = models.IntegerField(default=0)
    time_signature = models.IntegerField(default=0)
    num_bars = models.IntegerField(default=0)
    num_sections = models.IntegerField(default=0)
    num_segments = models.IntegerField(default=0)
    song_class = models.IntegerField(default=0)
    rating = models.ForeignKey(SongRating, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Song: {self.title}"

class SongUserRating(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return f"Rating for {self.song.title}: {self.rating}"
