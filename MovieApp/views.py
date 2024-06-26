from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from MovieApp.models import Genre, SubGenre, Movie
from MovieApp.forms import SignUpForm, SignInForm, UserReviewForm
from django.db.models import Q

# Create your views here.

class GenreListView(View):
    def get(self, request, *args, **kwargs):
        genres = Genre.objects.all().order_by('genre_name')
        return render(request, 'MovieApp/index.html',{'genres':genres})


class GenreDetailView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("gd")
        g = Genre.objects.get(id=id)
        sub = SubGenre.objects.filter(parent_genre_id = id)
        genres = Genre.objects.order_by('genre_name')

        sub_with_movies = []
        for subgenre in sub:
            # Retrieve movies for the subgenre ordered by release date in reverse chronological order
            movies = subgenre.movies.order_by('-release_date')
            sub_with_movies.append({'subgenre': subgenre, 'movies':movies})

        return render(request, "MovieApp/genre_detail.html",{'g':g, 'sub_with_movies':sub_with_movies ,'genres':genres})
    
class MovieListView(ListView):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.order_by('title') # Fetch all movies
        paginator = Paginator(movies, per_page=24)  # Show 24 movies per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        genres = Genre.objects.order_by('genre_name') # Fetch all genres
        return render(request, 'MovieApp/movie_list.html', {'movies': movies, 'genres': genres, 'page_obj': page_obj})
    
class MovieDetailView(View):
    def get(self, request, *args, **kwargs):
        movie_id = kwargs.get('md')
        movie = Movie.objects.get(id=movie_id)
        movie_genres = movie.genres.all() # Fetch all genres available in the database
        genres = Genre.objects.order_by('genre_name') # Fetch all genres

         # Instantiate the form
        form = UserReviewForm()

        return render(request, 'MovieApp/movie_detail.html', {'movie':movie, 'movie_genres':movie_genres, 'genres':genres, 'form':form})
    
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'MovieApp/signup.html'
    success_url = reverse_lazy('signin')
    success_message = 'Registered Successfully !'
    def get_success_message(self, cleaned_data):
        return self.success_message
    

class SignInView(View):
    def get (self, request, *args, **kwargs):
        signinform = SignInForm() # Instantiate the SignUpForm
        return render(request, 'MovieApp/signin.html',{'signinform':signinform})
    
    def post (self, request, *args, **kwargs):
        signinform = SignInForm(request.POST)
        if signinform.is_valid():
            username = signinform.cleaned_data.get('username')
            password = signinform.cleaned_data.get('password')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
                return redirect('signin')  # Redirect back to the login page with an error message
        # If the form is invalid or authentication fails, re-render the login page with the form and validation errors
        return render(request, 'MovieApp/signin.html', {'signinform': signinform})
    
class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")
    

class SearchView(View):
    def get(self, request):
        query = request.GET.get('query')
        if query:
            movie = Movie.objects.filter(title__icontains=query).first()
            genre = Genre.objects.filter(genre_name__icontains=query).first()
            if movie:
                return JsonResponse({'status': 'redirect', 'url': reverse('movie_detail', args=[movie.id])})
            elif genre:
                return JsonResponse({'status': 'redirect', 'url': reverse('genre_detail', args=[genre.id])})
            else:
                return JsonResponse({'status': 'error', 'message': 'No results found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Query cannot be empty'})
        

class UserReviewCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserReviewForm()
        return render(request, 'movie_detail.html', {'form': form})
     
    def post(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        form = UserReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movie_detail', md=movie_id)
        return redirect('movie_detail', md=movie_id)