from Genre_finder import genre_finder
from All_from_genre import all_from_genre
from book_details_scraper_isolated import book_details
from Ratings_filter import ratings_filter


def homepage():

    print("Welcome to the web scraper!")
    shutdown = False
    while shutdown == False:
        print("*******************************************")
        print("--------------- Homepage ------------------")
        print("-------------------------------------------")
        print("Welcome to the web scraper! Choose a Feature: ")
        print("")
        print("1. Search directly for a book by title")
        print("2. Browse by genre")
        print("3. Search by rating")
        print("4. End program")
        print("")
        print("------------------------------------------")


        user_input = input("Choose an option (1-4): ")

        user_input = str(user_input)


        if user_input == '1':
            from title_search_modules import title_search_modules
            title_search_modules()
        elif user_input == '2':
            output_url = genre_finder()
            book_to_view = all_from_genre(output_url)
            book_details(book_to_view)
        elif user_input == '3':
            ratings_filter()
        elif user_input == '4':
            print("Shutting down...")
            shutdown = True
        else:
            print("Invalid input!")


homepage()