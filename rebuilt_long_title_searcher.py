import requests
import bs4
from book_details_scraper_isolated import book_details

def title_search_long(totalpages):
    book_found = False
    book_choice = input("Search for a book title: ")

    similar_dictionary = dict()
    similar_dictionary_counter = 1


    page = 1
    while not book_found and page <= totalpages:
        if page == 1:
            print(f"Searching page {page}...")
            url = f"https://books.toscrape.com/catalogue/category/books_1/index.html"
        else:
            url = f"https://books.toscrape.com/catalogue/category/books_1/page-{page}.html"
            print(f"Searching page {page}...")
        page_destination = requests.get(url)

        page_soup = bs4.BeautifulSoup(page_destination.text, "lxml")
        page_component = page_soup.select(".product_pod")

        for book in page_component:
            if book_choice == book.select("a")[1]["title"]:
                print("Book found! -- ",book.select('a')[1]['title'])
                book_to_view = book.select('a')[1]['title']
                #------------------------------------------------------------------------------
                #This bit is to determine the URL of the details for the book itself.

                book_url = book.select('a')[0]['href']
                url_pruned = False
                while url_pruned == False:
                    if book_url[:3] == '../':
                        book_url = book_url[3:]
                    else:
                        url_pruned = True
                book_url = f"https://books.toscrape.com/catalogue/{book_url}"
                #-------------------------------------------------------------------------------
                book_found = True

            else:
                book_choice_split = book_choice.split(" ")
                for word in book_choice_split:
                    if len(word) > 3 and word in book.select("a")[1]["title"]:
                        similar_dictionary[(similar_dictionary_counter)] = [(book.select("a")[1]["title"]),(book.select('a')[0]['href'])]
                        similar_dictionary_counter += 1

        page += 1

    if book_found == True:
        return book_url, book_found
    elif len(similar_dictionary) > 0:
        return similar_dictionary, book_found
    else:
        return "No Matches or similar content",book_found




def output_processer(title_search_output):
    # A few lines to define the unpack the variables from the 'title_search_output' input
    unknown_input = title_search_output[0]
    book_found = title_search_output[1]  # The boolean 'book_found' is the second item returned from the title_search function

    if type(unknown_input) == str and book_found == True:
        book_url = unknown_input
        similar_dictionary = dict()
    elif type(unknown_input) == str and book_found == False:
        book_url = ''
        similar_dictionary = dict()
    elif type(unknown_input) == dict:
        similar_dictionary = unknown_input
        book_url = ''
    else:
        print("Unidentified input into function")

    #---------------------------------------------------

    if len(similar_dictionary) > 0:
        print("--------------------------------")
        print("No match found, did you mean...")
        for item in similar_dictionary:
            print(f"{item}. {similar_dictionary.get(item)[0]}")
        book_choice_bool = False
        while book_choice_bool == False:
            alt_book_number = input(f"Enter the book number for more details (1-{len(similar_dictionary)}), or press 'Enter' to go back: ")
            alt_book_number = int(alt_book_number)
            if alt_book_number in range(1, len(similar_dictionary)):

                print(f"Obtaining details for '{similar_dictionary.get(alt_book_number)[0]}'.")

                #This URL pruning feature can probably be integrated into the 'book_details' function, as it has been repeated more than once throughout this script
                book_url = similar_dictionary.get(alt_book_number)[1]
                url_pruned = False
                while url_pruned == False:
                    if book_url[:3] == '../':
                        book_url = book_url[3:]
                    else:
                        url_pruned = True
                book_url = f"https://books.toscrape.com/catalogue/{book_url}"
                book_details(book_url)
                #---------------------------------------------------------------------------------------------------------------------------------------------------
                book_choice_bool = True
            elif alt_book_number == '':
                print("Returning...")
                book_choice_bool = True
            else:
                print("Invalid input")
    elif len(similar_dictionary) == 0 and book_found == False:
        print("No matches or similar items found.")
    elif book_found == True:
        acceptable_input = False
        while acceptable_input == False:
            proceed_to_book = input("Would you like to view the details for this book? ('Yes/ No'): ")
            if proceed_to_book == "Yes":
                acceptable_input = True
                # Time to webscrape the page using the function in book-details-scraper-isolated.
                book_details(book_url)
            elif proceed_to_book == "No":
                acceptable_input = True
                print("Returning to homepage...")
            else:
                print("Invalid input!")
