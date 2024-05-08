from django.urls import path
from MovieApp import views

urlpatterns = [
    path('',views.GenreListView.as_view(), name = 'home'),
    path('genre/<int:gd>',views.GenreDetailView.as_view(),name = 'genre_detail'),
    path('movies/',views.MovieListView.as_view(), name = 'movie_lst'),
    path('movie/<int:md>',views.MovieDetailView.as_view(),name = 'movie_detail'),
    path('signup/',views.SignUpView.as_view(), name = 'signup'),
    path('signin/',views.SignInView.as_view(), name = 'signin'),
    path('signout/',views.SignOutView.as_view(), name = 'signout'),
    path('search/', views.SearchView.as_view(), name='search'),
]