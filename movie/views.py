from django.shortcuts import redirect, render, get_object_or_404
from movie.forms import ReviewForm

from movie.models import Movie, Review

# Create your views here.

def home(request):
    searchItem = request.GET.get('searchItem')
    if searchItem:
        movie = Movie.objects.filter(title__icontains=searchItem)
    else:
        movie = Movie.objects.all()
    return render(request, 'home.html', {'searchItem' : searchItem, 'movies' : movie})


def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'details.html', {'movie' : movie, 'reviews' : reviews})


def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'reviewform.html', {'form' : ReviewForm, 'movie' : movie})
        
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('details', newReview.movie.id)
        except ValueError:
            return render(request, 'reviewform.html', {'form' : ReviewForm(), 'movie' : movie, 'error' : 'Bad Data Given'})