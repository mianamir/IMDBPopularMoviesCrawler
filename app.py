__author__ = "Amir Savvy"
__email__ = "mianamirlahore@gmail.com"

from data_collection_helpers import (urls, popular_movies)
from data_analysis import helpers

# Get urls from IMDB popular movies site
urls_list = urls.get_popular_movies_urls()

# Get IMDB popular movies list
popular_movies_list = popular_movies.popular_movies_data(urls_list)

# Get list of movies that have improved in popularity
helpers.movies_improved_in_popularity(popular_movies_list)

# Get previous week’s position of each movie list
helpers.list_previous_week_position_of_each_movie(popular_movies_list)

# Get the highest rated genre with respect to position
helpers.highest_rated_genre(popular_movies_list)



