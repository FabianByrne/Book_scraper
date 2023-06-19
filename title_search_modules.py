
from totalpage_calculator import totalpage_calculator

from rebuilt_long_title_searcher import title_search_long

from rebuilt_long_title_searcher import output_processer



def title_search_modules():
    #1. Run totalpage_calculator to find the total number of pages to scrape through

    totalpages = totalpage_calculator()

    #2. Run the title_search_long to scour all pages within the index for a certain book, or similar alternatives.
    #2 a. If the output of title_search_long is a string, it should be the book url produced upon finding the book successfully.
    #2 b. If the output of title_search long is a list, it should be the 'similar_list' produced upon finding similar titles, but not the one requested.

    title_search_long_output = title_search_long(totalpages)

    output_processer(title_search_long_output)