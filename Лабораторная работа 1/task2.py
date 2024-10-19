# TODO Найдите количество книг, которое можно разместить на дискете

drive_memory = 1.44 #Мбайт, объем дискеты

drive_memory_bytes = drive_memory * 1024 * 1024 # перевод Мбайты в байты

pages = 100 #Количество страниц в книге

rows_on_page = 50 #Число строк на странице

symbols_in_row = 25 #Количество символов в строке

memory_for_symbol = 4 #Для хранения кода одного символа нужно 4 байта

memory_for_book = memory_for_symbol * symbols_in_row * rows_on_page * pages

quantity_book_on_drive = round(drive_memory_bytes/memory_for_book)



print("Количество книг, помещающихся на дискету:", quantity_book_on_drive)
