from django.urls import path
from .views import MainIndex, MainShow, MainFilm, Mfilm, Maintech, MainPost, main_delete_post, main_view

app_name = "main"

urlpatterns = [
    path('', MainIndex, name="index"),
    path('Tvshows', MainShow, name="show"),
    path('film', MainFilm, name="film"),
    path('technology', Maintech, name='tech'),
    path('more-films', Mfilm, name="mfilm"),
    path('add-content', MainPost, name="content"),
    path('delete-post/<int:id>/', main_delete_post, name='delete-post'),
    path('view/<int:id>/', main_view, name='view')
]
