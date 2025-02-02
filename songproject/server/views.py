from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Song, SongUserRating, SongRating
from .serializers import SongSerializer, SongUserRatingSerializer
from rest_framework.pagination import PageNumberPagination

class SongPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = SongPagination

class SongRetrieveView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'title'


@api_view(['POST'])
def rate_song(request):
    if not request.data.get('song_id') or not request.data.get('rating'):
        return Response({"error": "song_id and rating are required."}, status=status.HTTP_400_BAD_REQUEST)

    song = Song.objects.filter(song_id=request.data['song_id']).first()
    if not song:
        return Response({"error": "Song not found."}, status=status.HTTP_404_NOT_FOUND)

    rating = request.data.get('rating')

    # Considering each rating as new
    SongUserRating.objects.create(song=song, rating=rating)

    total_ratings = SongUserRating.objects.filter(song=song)
    total_ratings_count = total_ratings.count()

    if total_ratings_count > 0:
        total_rating_value = sum([rating.rating for rating in total_ratings])
        average_rating = total_rating_value / total_ratings_count
    else:
        average_rating = 0

    song_rating, created = SongRating.objects.get_or_create(song=song)
    song_rating.rating = average_rating
    song_rating.save()

    return Response({"message": "Song rated successfully."}, status=status.HTTP_200_OK)