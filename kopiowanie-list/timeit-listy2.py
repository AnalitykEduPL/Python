import timeit
import copy
import random

random_numbers = random.sample(range(7000000),1000000)

czas1=timeit.timeit(stmt="""random_numbers2=[item for item in random_numbers]""", globals=locals(), number = 100)
czas2=timeit.timeit(stmt="""random_numbers2=copy.deepcopy(random_numbers)""", globals=locals(), number = 100)
czas3=timeit.timeit(stmt="""random_numbers2=random_numbers[0:len(random_numbers)]""", globals=locals(),number = 100)
czas4=timeit.timeit(stmt="""random_numbers2=copy.copy(random_numbers)""", globals=locals(), number = 100)
czas5=timeit.timeit(stmt="""random_numbers2=random_numbers[:]""", globals=locals(), number = 100)
czas6=timeit.timeit(stmt="""random_numbers2=[*random_numbers]""", globals=locals(), number = 100)
czas7=timeit.timeit(stmt="""random_numbers2=random_numbers*1""", globals=locals(), number = 100)
czas8=timeit.timeit(stmt="""random_numbers2=[]; 
for item in random_numbers: random_numbers2.append(item)""", globals=locals(), number = 100)
czas9=timeit.timeit(stmt="""random_numbers2=list(random_numbers)""", globals=locals(), number = 100)
czas10=timeit.timeit(stmt="""random_numbers2=[]; random_numbers2.extend(random_numbers)""", globals=locals(), number = 100)
czas11=timeit.timeit(stmt="""random_numbers2=random_numbers.copy()""", globals=locals(), number = 100)



wyniki = [["List comprehension =>", czas1], ["copy.deepcopy() =>", czas2], ["[0:len(numbers)] =>", czas3], ["copy.copy() =>", czas4],
["[:] =>", czas5], ["*args =>", czas6], ["*1 =>", czas7], ["Zwykła pętla =>", czas8], ["Konwersja list() =>", czas9], ["extend() =>", czas10],
["Wbudowane copy() =>", czas11]]

[print(wynik[0], wynik[1]) for wynik in sorted(wyniki, key=lambda x: x[1])]