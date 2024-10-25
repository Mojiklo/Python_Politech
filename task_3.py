# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_characters = 25
symbol_weight = 4

book_byte = number_of_pages * number_of_lines * number_of_characters * symbol_weight
book_mb = book_byte / (1024*1024)

count_books = int(volume / book_mb)
print("Количество книг, помещающихся на дискету:", count_books)
