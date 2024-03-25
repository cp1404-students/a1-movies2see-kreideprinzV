"""
Name: Hein Htet Aung
Date started:
GitHub URL (of this assignment): https://github.com/cp1404-students/a1-movies2see-kreideprinzV
Remember to NEVER make this assignment repo public
"""

import csv

# Constants
MOVIES_FILE = "movies.csv"
WATCHED = "w"
UNWATCHED = "u"


def load_movies():
    """Load movies from CSV file into a list of lists."""
    movies = []
    with open(MOVIES_FILE, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            movies.append(row)
    return movies

def save_movies(movies):
    """Saving movies to moive.csv file."""
    with open(MOVIES_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)

def sort_key(movie):
    """Sorting movies."""
    return (movie[2], movie[0])

def display_movies(movies):
    """Displaying formatted list of movies from csv."""
    print("Movies:")
    for index, movie in enumerate(sorted(movies, key=sort_key)):

        status = "*" if movie[3] == UNWATCHED else ""
        print(f"{index+1}. {movie[0]}, {movie[2]}, {movie[1]} {status}")
    unwatched_count = sum(1 for movie in movies if movie[3] == UNWATCHED)
    print(f"\n{unwatched_count} movies to watch.")


def add_movie(movies):
    """Adding a new movie to the list from csv."""
    title = input("Enter movie title: ")
    year = input("Enter movie year: ")
    category = input("Enter movie category: ")
    movies.append([title, category, year, UNWATCHED])
    print("Movie added successfully.")


def watch_movie(movies):
    """Mark a movie as watched."""
    unwatched_movies = [index+1 for index, movie in enumerate(movies) if movie[3] == UNWATCHED]
    if not unwatched_movies:
        print("No more movies to watch!")
        return
    print("Choose a movie to mark as watched:")
    for index in unwatched_movies:
        print(f"{index}. {movies[index-1][0]}")
    choice = int(input("Enter your choice: "))
    if choice in unwatched_movies:
        movies[choice-1][3] = WATCHED
        print(f"{movies[choice-1][0]} marked as watched.")
    else:
        print("Invalid choice.")
2
def main():

    movies = load_movies()

    print("Welcome to Movie List Program by Hein Htet Aung!")


    while True:
        print("\nMenu:")
        print("(D) List movies")
        print("(W) Mark movie as watched")
        print("(A) Add movie")
        print("(Q) Quit")
        choice = input("Enter your choice: ").upper()

        if choice == "D":
            display_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            watch_movie(movies)
        elif choice == "Q":
            save_movies(movies)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
