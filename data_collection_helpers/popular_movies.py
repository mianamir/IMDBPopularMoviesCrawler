import json

import requests
from bs4 import BeautifulSoup


def popular_movies_data(urls):
    """
    Will crawl IMDB popular movies each page
    :param urls:
    :return: json of IMDB popular movies
    """
    popular_movies_list = list()
    for url in urls:
        URL = 'https://www.imdb.com{}'.format(url)
        single_page = requests.get(URL)
        soup = BeautifulSoup(single_page.content, 'html.parser')

        title_block_div = soup.find('div', class_='title_block')
        title_block_a_tags = title_block_div.find_all('a')
        try:
            genre_of_the_movie = "{}, {}".format(title_block_a_tags[2].text,
                                                 title_block_a_tags[3].text)
        except (LookupError, ValueError, IndexError):
            genre_of_the_movie = "Not Available"
        except Exception:
            genre_of_the_movie = "Not Available"

        title_review_bar_div = soup.find('div', class_='titleReviewBar')
        title_review_bar_a_tags = title_review_bar_div.find_all('a')
        current_position_div = \
            title_review_bar_div.find_all(class_='titleReviewBarItem')[-1]
        current_position_text = \
            current_position_div.find(class_='subText').text
        current_position_sub_text = current_position_div.find(class_='subText')

        position_image_up = None
        position_image_down = None
        current_position = None
        number_of_user_reviews = None
        number_of_critic_reviews = None
        popularity = None

        if not position_image_down and \
                current_position_sub_text.find(
                    class_='popularityImageUp') and \
                'popularityImageUp' in \
                current_position_sub_text.find(
                    class_='popularityImageUp')['class']:
            position_image_up = "+"
        if not position_image_up and \
                current_position_sub_text.find(class_='popularityImageDown') \
                and 'popularityImageDown' in \
                current_position_sub_text.find(
                    class_='popularityImageDown')['class']:
            position_image_down = "-"

        if ' ' not in current_position_text.replace('\n', '').strip():
            current_position = \
                int(current_position_text.replace('\n', '').strip())
            popularity = ""
        else:
            try:
                current_position = \
                    int(current_position_text.replace('\n', '').strip()[0])
            except (LookupError, ValueError, IndexError):
                current_position = 0
            except Exception:
                current_position = 0
            try:
                popularity = \
                    current_position_text.replace('\n', '').strip()[-3:-1]
            except (LookupError, ValueError, IndexError):
                popularity = ""
            except Exception:
                popularity = ""
            if position_image_up:
                popularity = position_image_up + '' + str(popularity).strip()
            if position_image_down:
                popularity = position_image_down + '' + str(popularity).strip()
            try:
                if len(title_review_bar_a_tags):
                    number_of_user_reviews = \
                        int(str(title_review_bar_a_tags[3].text[:-4]).
                            replace(',', ''))
                else:
                    number_of_user_reviews = 0
            except (LookupError, ValueError,IndexError):
                number_of_user_reviews = 0
            except Exception:
                number_of_user_reviews = 0
            try:
                if len(title_review_bar_a_tags):
                    number_of_critic_reviews = \
                        int(title_review_bar_a_tags[4].text[:-7])
                else:
                    number_of_critic_reviews = 0
            except (LookupError, ValueError,IndexError):
                if len(title_review_bar_div.find_all('a')):
                    number_of_critic_reviews = \
                        int(title_review_bar_div.find_all('a')[-1].text[0])
                else:
                    number_of_critic_reviews = 0
            except Exception:
                number_of_critic_reviews = 0
        popular_movies_list.append(
            {
                'current_position': current_position,
                'popularity': popularity,
                'budget': 0,
                'genre_of_the_movie': genre_of_the_movie,
                'number_of_user_reviews': number_of_user_reviews,
                'number_of_critic_reviews': number_of_critic_reviews

            }
        )
    try:
        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(popular_movies_list, f, ensure_ascii=False, indent=4)
        print("->>>>>>>> Data Scrapped Successfully ->>>>>>>>>>>>>")
    except FileNotFoundError:
        print("Error: file not found")
    return popular_movies_list

