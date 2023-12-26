from django.urls import path

from movie.views import create_review, details

urlpatterns = [
    path('<int:movie_id>', details, name='details'),
    path('review/<int:movie_id>/create/', create_review, name='create_review')
]
