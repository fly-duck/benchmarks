
indexes=[1,2,6]
# indexes=[x+1 for x in indexes]
# print(indexes)
print(indexes.index(6))

dict_indexes={}
for i in range(3):
    dict_indexes[indexes[i]]=indexes[i]
for i in range(3):
    dict_indexes[indexes[i]]=indexes[i]
test_set=set()

for index in indexes:
    if index>=3:
        test_set.add(index)

for index in test_set:
    del dict_indexes[index]

    
print dict_indexes

