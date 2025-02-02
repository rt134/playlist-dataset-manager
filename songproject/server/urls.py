from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.SongListView.as_view(), name='song_list'),
    path('songs/<str:title>/', views.SongRetrieveView.as_view(), name='song_retrieve'),
    path('rate_song/', views.rate_song, name='rate_song'),
]
