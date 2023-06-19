import requests
import bs4
from book_details_scraper_isolated import book_details
def ratings_filter():
    book_by_ratings_dict = dict()
    home_destination = requests.get("https://books.toscrape.com/catalogue/category/books_1/index.html")
    soup = bs4.BeautifulSoup(home_destination.text,"lxml")

    # Page calculator -----------------------------------------

    pages_num = soup.select(".current")

    if bool(pages_num) == True:
        pages_num_text = (pages_num[0].getText())
        pages_num_text = (str(pages_num_text))
        pages_num_text = pages_num_text.strip()
        pages_num_list = pages_num_text.split(" ")
        totalpages = pages_num_list[-1]
        totalpages = int(totalpages)
    else:
        totalpages = 1


    rating_loop = False

    while rating_loop == False:
        rating_choice = input("Choose a rating to sort by (1-5): ")
        if rating_choice == "1":
            rating_choice = ".star-rating.One"
            rating_loop = True
        elif rating_choice == "2":
            rating_choice = ".star-rating.Two"
            rating_loop = True
        elif rating_choice == "3":
            rating_choice = ".star-rating.Three"
            rating_loop = True
        elif rating_choice == "4":
            rating_choice = ".star-rating.Four"
            rating_loop = True
        elif rating_choice == "5":
            rating_choice = ".star-rating.Five"
            rating_loop = True
        else:
            print("Invalid input! Select a rating between 1 and 5")
            print(rating_choice)


    book_counter = 0

    for page in range(1,totalpages + 1):
        if page == 1:
            page_destination = requests.get(f"https://books.toscrape.com/catalogue/category/books_{page}/index.html")
        else:
            page_destination = requests.get(f"https://books.toscrape.com/catalogue/category/books_1/page-{page}.html")

        page_soup = bs4.BeautifulSoup(page_destination.text,"lxml")
        page_component = page_soup.select(".product_pod")



        for book in page_component:
        

        
            if len(book.select(rating_choice)) != 0:
                book_counter += 1
                book_title = (book.select("a")[1]["title"])
                book_url = book.select('a')[0]['href']
                url_pruned = False
                while url_pruned == False:
                    if book_url[:3] == '../':
                        book_url = book_url[3:]
                    else:
                        url_pruned = True
                book_url = f"https://books.toscrape.com/catalogue/{book_url}"
                book_by_ratings_dict[book_counter] = [(book_title), (book_url)]
                print(f"{book_counter}.{book_by_ratings_dict.get(book_counter)[0]}")

            else:
                pass

    print("")
    print(f"Finished! a total of {book_counter} books were found.")

    acceptable_input = False
    while acceptable_input == False:
        user_input = input(f"Choose a book (1-{len(book_by_ratings_dict)}), or press 'Enter' to return to the homepage: ")
        if user_input == '':
            pass
        else:
            user_input = int(user_input)
            print(f"Retrieving details for {user_input}")
            book_url = book_by_ratings_dict.get(user_input)[1]
            book_details(book_url)
