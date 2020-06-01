def movies_improved_in_popularity(data):
    """
    Will give list of movies that have improved in popularity
    :param args:
    :return: list of movies that have improved in popularity
    """
    response = list()
    for movie in data:
        if movie['popularity']:
            if '+' in movie['popularity']:
                response.append(movie)
    print("Movies improved in popularity list: ")
    print(response)


def highest_rated_genre(data):
    """
    Get the highest rated genre with respect to positions
    :param data:
    :return: highest rated genre dict
    """
    SIZE = float(len(data))
    avg_data = list()
    for single in data:
        avg_data.append(
            {
                "current_position": single['current_position']/SIZE,
                "popularity": single['popularity'],
                "budget": single['budget'],
                "genre_of_the_movie": single['genre_of_the_movie'],
                "number_of_user_reviews": single['number_of_user_reviews'],
                "number_of_critic_reviews": single['number_of_critic_reviews']
            }
        )
    highest_rated_movie = max(avg_data,
                              key=lambda movie: movie['current_position'])
    print("Highest rated genre: ")
    print(highest_rated_movie)


def list_previous_week_position_of_each_movie(data):
    """
    Will give list of previous week position of each movie
    :param data:
    :return: list of previous week position of each movie
    """
    response = list()
    for movie in data:
        try:
            if '+' in movie['popularity']:
                popularity = int(str(movie['popularity']).replace('+', ''))
                movie['current_position'] = popularity + int(
                    movie['current_position'])
                response.append(
                    {
                        'genre_of_the_movie': movie['genre_of_the_movie'],
                        'previous_week_position': movie['current_position']

                    }
                )
        except TypeError:
            pass

        try:
            if '-' in movie['popularity']:
                popularity = int(str(movie['popularity']).replace('-', ''))
                movie['current_position'] = popularity - int(
                    movie['current_position'])
                response.append(
                    {
                        'genre_of_the_movie': movie['genre_of_the_movie'],
                        'previous_week_position': movie['current_position']

                    }
                )
        except TypeError:
            pass
    print("List of previous week position of each movie: ")
    print(response)

