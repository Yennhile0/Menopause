import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
import math
data=pd.read_csv('gbsg.csv')

#averages 
data.er
avg_of_er=sum(data.er)/685
print(f"The average of estrogen receptors in fmol/l is: {avg_of_er} fmol/l")


data.nodes
avg_of_nodes=sum(data.nodes)/685
print(f"The average of positive lymph nodes is: {avg_of_nodes} nodes")

data.rfstime
avg_of_rfstime=sum(data.rfstime)/685
print(f"The average recurrence free survival time is: {avg_of_rfstime} days")

data.age
avg_of_age=sum(data.age)/685
print(f"The average age: {avg_of_age} years")



#number of observations in the data set
print(data.shape)


#most common age
from collections import Counter

def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]
Most_Common(data.age)



#max and min age

column_name = 'age'
column_list = df['age'].tolist()


highest_float = float('-inf')
lowest_float = float('inf')

for num in column_list:
    if num > highest_float:
        highest_float = num
    if num < lowest_float:
        lowest_float = num

print(f"The highest age is: {highest_float}")
print(f"The lowest age is: {lowest_float}")



#most comon grade tumor

from collections import Counter
column_name = 'grade'
column_list = df['grade'].tolist()

counts = Counter(column_list)
max_count = 0
most_common_int = None

for num, count in counts.items():
    if count > max_count:
        max_count = count
        most_common_int = num

print(f"The most common grade tumor is: {most_common_int}")



#most common tumor size

from collections import Counter
column_name = 'size'
column_list = df['size'].tolist()

counts = Counter(column_list)
max_count = 0
most_common_int = None

for num, count in counts.items():
    if count > max_count:
        max_count = count
        most_common_int = num

print(f"The most common tumor size is: {most_common_int}mm")



#breast cancer and whether or not in occurs post or pre menopause
from collections import Counter
column_name = 'meno'
meno_list = df['meno'].tolist()

counts = Counter(meno_list)
max_count = 0
most_common_int = None

for num, count in counts.items():
    if count > max_count:
        max_count = count
        most_common_int = num

print(f"menopausal 1:meaning postmenopausal and 0: meaning premenopausal and data suggests that in the dataset there are more {most_common_int}")
#x is the index. if/else statement to find individual women who have been diagnosed with .



def menopause_age(x):
    meno=meno_list[x]
    age=age_list[x]
    if meno == 1:
        return "premenopausal"
    elif meno == 0:
        return "postmenopausal"
    else:
        return "Undefined"
    



