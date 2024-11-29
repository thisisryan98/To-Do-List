movies= {}

def return_lobby():
    """Return user to lobby"""
    print("\n")
    print("Type (Add) to add movies.")
    print("Type (View) to view movies.")
    print("Type (Remove) to remove movies.")
    choice = input("\nWhat would you like to do? ").strip().lower()
    if choice == 'add':
        add_movie()
    elif choice == 'view':
        print_list()
    elif choice == 'remove':
        remove_movies()
    else:
        print("\nSorry, that is not an option. Please re-enter your response.")
        return_lobby()

def add_movie(): 
    """Add Movie to Dictionary"""
    polling_active = True
    while polling_active:
        title = input("\nWhat is the title of the movie you want to add? ")
        director = input("\nWho is the director of the movie? ")
        genre = input("\nWhat is the genre of the movie? ")
        year = input("\nWhat year was the movie released? ")
        
        movies[title] = {
            'director': director,
            'genre': genre,
            'year': year,
        }
        print("\nYour movie has been added to the list.")
        add_another = input("\nWould you like to add another movie to the library?\n(yes/no): ").strip().lower()
        if add_another != 'yes':
            polling_active = False
    return_lobby()

def print_list():
    """Print List"""
    print("\n---Favorite Movies---")
    for title, details in movies.items():
        print(f"\nTitle: {title}")
        print(f"Director: {details['director']}")
        print(f"Genre: {details['genre']}")
        print(f"Release Year: {details['year']}")
    
    back_lobby = input("\nWould you like to return to the lobby?\n(yes/no): ").strip().lower()
    if back_lobby == 'yes':
        return_lobby()
    else:
        print("\nToo bad. You go to lobby.")
        return_lobby()

def remove_movies():
    """remove movie from dictionary"""
    if not movies:
        print("\nThere are no movies to remove.")
        return_lobby()
    
    title = input("\nEnter the title of the movie you want to remove: ")
    
    if title in movies:
        del movies[title]
        print(f"\n'{title}' has been removed from library.")
    else:
        print(f"\nSorry, '{title}' is not in the library.")
        
    remove_another = input("\nWould you like to remove another movie?\n(yes/no)").strip().lower()
    if remove_another == 'yes':
        remove_movies()
    else:
        return_lobby()
    
return_lobby()