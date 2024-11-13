# TODO Найдите количество книг, которое можно разместить на дискете

v_book = 1.44
list_in_book = 100
strok_in_book = 50
simbol_in_strok = 25
ves_simbola = 4 / (1024**2) # перевел в Мб
odinak_knig = v_book / (ves_simbola * simbol_in_strok * strok_in_book * list_in_book)
print("Количество книг, помещающихся на дискету:", int(round(odinak_knig, 0)))
