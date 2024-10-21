# TODO Найдите количество книг, которое можно разместить на дискете

obem = 1.44
co_stronic = 100
co_strok = 50
co_simv = 25
v1simvole = 4

kniga_bait = co_stronic * co_strok * co_simv * v1simvole
kniga_mb = (kniga_bait) / (1024*1024)

col = round((obem / kniga_mb))
print("Количество книг, помещающихся на дискету:", col)
