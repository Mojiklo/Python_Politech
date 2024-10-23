# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_characters = 25
symbol_weight = 4

book_bait = number_of_pages * number_of_lines * number_of_characters * symbol_weight
book_mb = (book_bait) / (1024*1024)

cound_books = round(volume / book_mb)
print("Количество книг, помещающихся на дискету:", cound_books)
