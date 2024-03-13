# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    d = defaultdict()
    with open(f) as rating_file:
        for line in rating_file: 
            ratings_list = []
            l = line.strip().split("|")
            movie_title = l[0]
            if movie_title in d:
                d[movie_title].append(l[1])
            else:
                ratings_list.append(l[1])
                d[movie_title] = ratings_list
    return d


# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    d = defaultdict()
    with open(f) as genre_file:
        for line in genre_file:
            l = line.strip().split("|")
            genre = l[0]
            movie = l[2]
            d[movie] = genre
    return d
# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    genre_dict = defaultdict()
       
    for key, value in d.items():
        if value not in genre_dict:
            genre_dict[value] = [key]
        else:
            genre_dict[value].append(key) 
    return genre_dict

     
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    average_rating = defaultdict()
    for key, value in d.items():
        count = 0.0
        for i in value:
            count += float(i)
        avg = count/(len(value))
        average_rating[key] = round(avg, 2)
    return average_rating
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating, 
    #         in ranked order from highest to lowest average rating
    # WRITE YOUR CODE BELOW
    top_n = defaultdict()

    for i in range(n):
        max = 0
        for key, value in d.items():    
            if d[key] > max and key not in top_n:
                max = d[key]
                id = key
        if id not in top_n:
            top_n[id] = max

    return top_n
        
    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    filter_d = defaultdict()

    for key in d:
        if d[key] >= thres_rating:
            filter_d[key] = d[key]
    return filter_d
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    genre_movies = defaultdict()
    popular_in_genre = defaultdict()
    for i in range(n):
        for key in genre_to_movies:
            if key == genre:
                genre_movies[key] = genre_to_movies[key] # Returns dictionary of Comedy movies: {Comedy: ["Movie1", "Movie2..."]}
                list = genre_movies[genre]
                for movie in list:
                    if movie in movie_to_average_rating:
                        popular_in_genre[movie] = movie_to_average_rating[movie]
                        popular_in_genre = get_popular_movies(popular_in_genre, n)
    return popular_in_genre


    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    genre_movies = defaultdict()
    for key in genre_to_movies:
        if key == genre:
            moviesList = genre_to_movies[genre]
            sum = 0.0
            for movie in moviesList:
                if movie in movie_to_average_rating:
                    genre_movies[movie] = movie_to_average_rating[movie]
                    sum += float(genre_movies[movie])
            average = sum/len(genre_movies)
    return average

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    list = []
    genre_popularity = defaultdict()
    for i in range(n):
        for key in genre_to_movies:
            if key not in list:
                list.append(key)
        for genre in list:
            average = get_genre_rating(genre, genre_to_movies, movie_to_average_rating)
            genre_popularity[genre] = average
    return genre_popularity

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rating)
    # WRITE YOUR CODE BELOW
    user_ratings = defaultdict()
    with open(f) as movie_ratings:
        for line in movie_ratings:
            list_of_movies_rated = []
            list = line.strip().split("|")
            user_id = list[2]
            rating = list[1]
            movie = list[0]
            if user_id in line:
                if user_id not in user_ratings:
                    user_ratings[user_id] = [(movie, rating)]
                elif user_id in user_ratings:
                    list_of_movies_rated = user_ratings[user_id]
                    list_of_movies_rated.append((movie, rating))
    return user_ratings
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    genre_to_rating = defaultdict()
    
    for user in user_to_movies:
        if float(user) == user_id:
            list_of_movies_rated = user_to_movies[user] 
            for item in list_of_movies_rated:
                movie = item[0]  
                rating = float(item[1])
                if movie in movie_to_genre:
                    movie_genre = movie_to_genre[movie]
                    if movie_genre not in genre_to_rating:
                        genre_to_rating[movie_genre] = [rating]
                    else:
                        # There is multiple of same genre
                        genre_to_rating[movie_genre].append(rating)
        else:
            break
    max = 0.0
    top_genre = ''
    for genre in genre_to_rating:
        rating = float(sum(genre_to_rating[genre]))/(len(genre_to_rating[genre]))
        if rating > max:
            max = rating
            top_genre = genre
    return top_genre

    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    top_3 = defaultdict()
    not_rated = defaultdict()
    for user in user_to_movies:
        if float(user) == user_id:
            top_genre = get_user_genre(user_id, user_to_movies, movie_to_genre)
            list_of_movies_rated = user_to_movies[user]
            list_of_movies = []
            for tuple in list_of_movies_rated:
                theMovie = tuple[0] 
                list_of_movies.append(theMovie)
            for movie in movie_to_genre:
                if movie_to_genre[movie] == top_genre:
                    if movie not in list_of_movies:
                        for movies in movie_to_average_rating:
                            if movie == movies:
                                rating = movie_to_average_rating[movies]
                                not_rated[movie] = rating
        else:
            break              
    top_3 = get_popular_movies(not_rated, 3)
    return top_3
    

# -------- main function for your testing -----
def main():
    a = read_movie_genre("genreMovieSample.txt")
    b = create_genre_dict(a)

    d = read_ratings_data("movieRatingSample.txt")
    e = calculate_average_rating(d)
    f = get_popular_movies(e, n=10)

    g = get_popular_in_genre("Action", b, e)
    print(g)
    p = get_genre_rating("Action", b, e)
    filter_movies(f, thres_rating=3)

    genre_popularity(b, e)

    z = read_user_ratings("movieRatingSample.txt")

    pp = get_user_genre(18, z, a)

    zz = recommend_movies(1, z, a, e)
    print(zz)
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py
main()

    