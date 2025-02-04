from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    search_term = request.GET.get("searchMovie")
    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()
    context = {
        "searchTerm": search_term,
        "movies": movies,
    }
    return render(
        request,
        "home.html",
        context,
    )


def about(request):
    return HttpResponse("<h1>Welcome to About Page</h1>")


def signup(request):
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, "detail.html", {"movie": movie, "reviews": reviews})


@login_required
def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "GET":
        return render(
            request,
            "createreview.html",
            {
                "form": ReviewForm(),
                "movie": movie,
            },
        )
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect("detail", newReview.movie_id)
        except ValueError:
            return render(
                request,
                "createrview.html",
                {"form": ReviewForm(), "error": "bad data passed in"},
            )


@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == "GET":
        form = ReviewForm(instance=review)
        return render(request, "updatereview.html", {"review": review, "form": form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect("detail", review.movie.id)
        except ValueError:
            return render(
                request,
                "updatereview.html",
                {"review": review, "form": form, "error": "Bad data in form"},
            )
            
@login_required            
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect("detail", review.movie.id)
