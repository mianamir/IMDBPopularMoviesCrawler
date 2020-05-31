__author__ = "Amir Savvy"
__email__ = "mianamirlahore@gmail.com"

from data_collection_helpers import (urls, popular_movies)
from data_analysis import helpers

# Get urls from IMDB popular movies site
urls_list = ['/title/tt7286456/',
        '/title/tt6199572/',
        '/title/tt3152592/',
        '/title/tt6723592/']
# urls_list = urls.get_popular_movies_urls()

# Get IMDB popular movies list
# popular_movies_list = popular_movies.popular_movies_data(urls_list)


popular_movies_list = [
    {
        "current_position": 4,
        "popularity": "+10",
        "budget": 0,
        "genre_of_the_movie": "Crime, Drama",
        "number_of_user_reviews": 10147,
        "number_of_critic_reviews": 680
    },
    {
        "current_position": 5,
        "popularity": "-3",
        "budget": 0,
        "genre_of_the_movie": "Biography, Crime",
        "number_of_user_reviews": 236,
        "number_of_critic_reviews": 68
    },
    {
        "current_position": 2,
        "popularity": "+3",
        "budget": 0,
        "genre_of_the_movie": "Animation, Adventure",
        "number_of_user_reviews": 334,
        "number_of_critic_reviews": 65
    },
    {
        "current_position": 3,
        "popularity": "+16",
        "budget": 0,
        "genre_of_the_movie": "Sci-Fi, Thriller",
        "number_of_user_reviews": 0,
        "number_of_critic_reviews": 1
    }
]

# Get list of movies that have improved in popularity
helpers.movies_improved_in_popularity(popular_movies_list)

# Get previous week’s position of each movie list


# Get the highest rated genre with respect to position
# helpers.highest_rated_genre(popular_movies_list)



