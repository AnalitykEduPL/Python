import timeit
import copy

czas1=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=[item for item in numbers]""", number=1000000)
czas2=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=copy.deepcopy(numbers)""", globals=locals(), number=1000000)
czas3=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=numbers[0:len(numbers)]""", number=1000000)
czas4=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=copy.copy(numbers)""", globals=locals(), number=1000000)
czas5=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=numbers[:]""", number=1000000)
czas6=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=[*numbers]""", number=1000000)
czas7=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=numbers*1""", number=1000000)
czas8=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=[]; 
for item in numbers: numbers2.append(item)""", number=1000000)
czas9=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=list(numbers)""", number=1000000)
czas10=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=[]; numbers2.extend(numbers)""", number=1000000)
czas11=timeit.timeit("""numbers = [0,1,2,3,4,5,6,7,8,9]; numbers2=numbers.copy()""", number=1000000)

wyniki = [["List comprehension =>", czas1], ["copy.deepcopy() =>", czas2], ["[0:len(numbers)] =>", czas3], ["copy.copy() =>", czas4],
["[:] =>", czas5], ["*args =>", czas6], ["*1 =>", czas7], ["Zwykła pętla =>", czas8], ["Konwersja list() =>", czas9], ["extend() =>", czas10],
["Wbudowane copy() =>", czas11]]

[print(wynik[0], wynik[1]) for wynik in sorted(wyniki, key=lambda x: x[1])]