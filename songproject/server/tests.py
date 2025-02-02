from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Song, SongUserRating, SongRating

class SongViewsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.song = Song.objects.create(title="TestSong", song_id="12345")
        self.song_rating = SongRating.objects.create(song=self.song, rating=4)
        print("Created song")
    
    def test_song_list_view(self):
        url = reverse('song_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
    
    def test_song_retrieve_view(self):
        url = reverse('song_retrieve', kwargs={'title': self.song.title})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.song.title)

    def test_rate_song_view_success(self):
        url = reverse('rate_song')
        data = {
            'song_id': '12345',
            'rating': 4
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Song rated successfully.")
        
        song_user_rating = SongUserRating.objects.filter(song=self.song, rating=4).first()
        self.assertIsNotNone(song_user_rating)
        self.song_rating.refresh_from_db()
        self.assertEqual(self.song_rating.rating, 4)

    def test_rate_song_view_missing_fields(self):
        url = reverse('rate_song')
        data = {'song_id': '12345'} 
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "song_id and rating are required.")
    
    def test_rate_song_view_song_not_found(self):
        url = reverse('rate_song')
        data = {
            'song_id': '99999',
            'rating': 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
