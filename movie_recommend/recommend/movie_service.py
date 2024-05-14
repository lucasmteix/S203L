from .models import Movie

class MovieService:
    def get_all_movies(self):
        """Retorna todos os filmes."""
        return Movie.objects.all()

    def get_movies_by_genre(self, genre_name):
        """Retorna filmes de um determinado gênero."""
        return Movie.objects.filter(genre__name=genre_name)