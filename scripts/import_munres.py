
# import numpy 
# a=numpy.array(1)
# print(a)
from munkres import Munkres # Third party library. For the minimum matching assignment problem. To install: https://pypi.python.org/pypi/munkres 

import random
# from munkres import Munkres
my_randoms=[]
for i in range (10):
    my_randoms.append(random.randrange(1,101))
# my_randoms = random.sample(range(100), 50)

print (my_randoms)
prev_dist = {'1','2','3'}
prev_dist2={}
prev_dist2[1]=2
prev_dist2[3]=4
prev_dist2[5]=6


match={}

# print(prev_dist.items())
for i,j in prev_dist2.items() :
    print(i)
est_people=[]
gt_people=[]
est_people=random.sample(range(1,10),8)
gt_people=random.sample(range(2,11),8)
print(est_people)
print(gt_people)


# for i in range(10):
#     est_people.append(random.randrange(1,10))

dist_matrix=[]
for est_person in est_people:
    dist_row=[]
    for gt_person in gt_people:
        if est_person not in match and gt_person not in match.values():
            dist=abs(est_person-gt_person)
        else:
            dist=99999
        dist_row.append(dist)
    dist_matrix.append(dist_row)
print(dist_matrix)

if dist_matrix:
    munkres=Munkres()
    # munkres2=munkres.Munkres()
    indexes=munkres.compute(dist_matrix)
    for i , j in indexes:
        if dist_matrix[i][j]<2:
            match[est_people[i]]=gt_people[j]
    print(indexes)
    print (match)





