movies = []


def menu():

    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_by = input("what properity of the movies is it?")
            looking_for = input("What are you looking for?")
            movie = find_movie(looking_for, lambda x: x[find_by])
            print(movie or 'No Movies Found')
        else:
            print("unknown command, please try again...")
        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")


def add_movie():
    name = input("Enter the movie name: ")
    hero = input("Enter the hero name: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'name': name,
        'hero': hero,
        'year': year
    })
    print("Movie added sucessfully.")


def show_movies():
        for movie in movies:
            show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name : {movie['name']}")
    print(f"Hero : {movie['hero']}")
    print(f"Year : {movie['year']}")


def find_movie(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return  found

menu()