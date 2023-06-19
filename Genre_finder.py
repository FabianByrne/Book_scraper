import bs4
import requests

def genre_finder():

    home_page = requests.get("https://books.toscrape.com/catalogue/category/books_1/index.html")

    soup = bs4.BeautifulSoup(home_page.text,"lxml")

    topic_list = soup.select(".nav.nav-list")


    names = topic_list[0]

    genre_dict = dict()
    range_counter = 0
    loop_condition = False

    while loop_condition == False:
        try:
            names.select('a')[range_counter]
        except IndexError:
            break
        genre_name = (names.select('a')[range_counter]).getText().strip() # the strip part is necessary to remove the blocks of whitespace, which would mainfest as '\n' on the genre names e.g: "\nTravel\n" for Travel.
        genre_href = (names.select("a")[range_counter]['href'])
        genre_dict[(range_counter +1)] = [(genre_name),(genre_href)] # The +1 on 'range counter +1' is so the key starts at 1 rather than 0, which looks better for a menu.
        range_counter +=1
    #print(genre_dict)

    print("Genre list:")

    for x in genre_dict:
        print(f"{x}.{genre_dict.get(x)[0]}")

    genre_choice = input(f"Please choose a genre (1-{len(genre_dict)}): ")
    genre_choice = int(genre_choice)

    print(f"You have chosen '{genre_dict.get(genre_choice)[0]}'")

    # This finds the URL for a chosen genre.

    hyperlink = (genre_dict.get(int(genre_choice))[1])
    if hyperlink[:3] == ("../"):
        hyperlink = hyperlink[3:]
    else:
        pass

    full_hyperlink = (f"https://books.toscrape.com/catalogue/category/{hyperlink}")

    return full_hyperlink