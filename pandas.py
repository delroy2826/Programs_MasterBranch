import pandas as pd
dictionary = {'first':1,'second':2,'third':3,'fourth':4}
a = pd.Series(dictionary)
print(a)

import pandas as pd
dictionary = {'firstname':'Delroy','lastname':'Oliveira','contact':9880699060,'profession':'Jobless'}
dictionary['profession'] = 'job'
a = pd.Series(dictionary)
print(a)

import pandas as pd
data = ([1,2,3],[3,4,5])
i=['set 1','set 2']
a = pd.Series(data,i)
print(a)

import pandas as pd
data1 = {'a':1,'b':2,'c':3,'d':4}
data2 = {'e':5,'f':6,'g':7,'h':8}
i={'firstdata':data1,'seconddata':data2}
a=pd.DataFrame(i)
print(a)

import pandas as pd
a = pd.Series([1,2,3,4,5])
b = pd.Series([6,7,6,9,10])
c =pd.Series([11,12,13,14,15])
i={'first':a,'second':b,'third':c}
z = pd.DataFrame(i)
print(z)