import fresh_tomatoes
import media
# above files are imported

Toy_story = media.Movie("Toy Story", "A story of a boy whose toys are shit",
                        "https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY606_.jpg",  # NOQA
                        "https://youtu.be/KYz2wyBy3kc")
# Instances are created and their name,storyline-
# , poster URL, trailer links are also given.
# media.Movie calls the class Movie and stores-
# all details in it when required.

Avatar = media.Movie("Avatar", "a marine on alien planet",
                     "https://images-na.ssl-images-amazon.com/images/I/61OUGpUfAyL._SY679_.jpg",  # NOQA
                     "https://youtu.be/5PSNL1qE6VY")

Veere_di_Wedding = media.Movie("Veere di wedding", "A story of friendship of a girl gang",  # NOQA
                               "http://st1.bollywoodlife.com/wp-content/uploads/2017/10/veere-di-wedding.jpg",  # NOQA
                               "https://youtu.be/IZODr96ZRCc")

Dhoom2 = media.Movie("Dhoom 2", "good story",
                     "https://c1.staticflickr.com/7/6202/6086017004_df9f620cfa_b.jpg",  # NOQA
                     "https://youtu.be/sWE458JxSZA")

Race3 = media.Movie("Race 3", "Race for money movie",
                    "https://pbs.twimg.com/media/Dclk41SUwAAljtO.jpg",
                    "https://youtu.be/xBht9TG7ySw")

Parmanu = media.Movie("Parmanu", "Indian nuclear bomb history",
                      "https://data1.ibtimes.co.in/cache-img-0-450/en/full/684955/1522898211_john-abraham.jpg",  # NOQA
                      "https://youtu.be/XQFb12N0Arc")

American_made = media.Movie("American made", "A drug mafia movie",
                            "https://media-cache.cinematerial.com/p/500x/rk6gpxgz/american-made-dvd-cover.jpg",  # NOQA
                            "https://youtu.be/AEBIJRAkujM")

Deadpool = media.Movie("Deadpool", "Action Movie",
                       "https://images-na.ssl-images-amazon.com/images/I/91qmrdkBViL._SY606_.jpg",  # NOQA
                       "https://youtu.be/FyKWUTwSYAs")

Avengers_Infinity_wars = media.Movie("Avengers: Infinity wars", "A marvel movie",  # NOQA
                                     "http://media.comicbook.com/2018/03/avengers-infinity-war-poster-all-iron-man-version-1096449.jpeg",  # NOQA
                                     "https://youtu.be/6ZfuNTqbHE8")

movies = [Toy_story, Avatar, Veere_di_Wedding,
          Dhoom2, Race3, Parmanu,
          American_made, Deadpool, Avengers_Infinity_wars]
# The names of all movies are stores in the list.

fresh_tomatoes.open_movies_page(movies)

# fresh_tomatoes.open_movies_page help to open the list/array-
# of movies in the form of website using HTML/CSS.
