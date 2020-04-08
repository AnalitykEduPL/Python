import timeit
import numpy as np
import copy
import random

arr = np.array([random.sample(range(7000000), 1000000)])

czas1=timeit.timeit(stmt="""arr2=np.array([item for item in arr])""", globals=locals(), number = 100)
czas2=timeit.timeit(stmt="""arr2=copy.deepcopy(arr)""", globals=locals(), number = 100)
czas3=timeit.timeit(stmt="""arr2=arr[0:len(arr)]""", globals=locals(),number = 100)
czas4=timeit.timeit(stmt="""arr2=copy.copy(arr)""", globals=locals(), number = 100)
czas5=timeit.timeit(stmt="""arr2=arr[:]""", globals=locals(), number = 100)
czas6=timeit.timeit(stmt="""arr2=np.array([*arr])""", globals=locals(), number = 100)
czas7=timeit.timeit(stmt="""arr2=arr*1""", globals=locals(), number = 100)
#czas8=timeit.timeit(stmt="""arr2=[]; for item in arr: arr2.append(item)""", globals=locals(), number = 100)
czas9=timeit.timeit(stmt="""arr2=np.array(arr)""", globals=locals(), number = 100)
#czas10=timeit.timeit(stmt="""arr2=[]; arr2.extend(arr)""", globals=locals(), number = 100)
czas11=timeit.timeit(stmt="""arr2=arr.copy()""", globals=locals(), number = 100)
czas12=timeit.timeit(stmt="""arr2=np.copy(arr)""", globals=locals(), number = 100)


wyniki = [["List comprehension =>", czas1], ["copy.deepcopy() =>", czas2], ["[0:len(numbers)] =>", czas3], ["copy.copy() =>", czas3],
["[:] =>", czas5], ["*args =>", czas6], ["*1 =>", czas7], ["Konwersja =>", czas9], ["Wbudowane copy() =>", czas11],["np.copy =>", czas12]]

[print(wynik[0], wynik[1]) for wynik in sorted(wyniki, key=lambda x: x[1])]
