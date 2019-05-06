
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


prev_match_id={}
no_restrict_matches={}


# For calculating MOTP
MOTP_dist_cum = 0
MOTP_dist_count = 0
false_positives=0
miss=0
correct=0
id_switches_count=0
# print(prev_dist.items())
for i,j in prev_dist2.items() :
    print(i)
est_people=[]
gt_people=[]
est_people=random.sample(range(1,10),8)
gt_people=random.sample(range(2,11),8)
print("estimated_people\n")
print(est_people)
print("ground_truth_people\n")
print(gt_people)


# for i in range(10):
#     est_people.append(random.randrange(1,10))
increment=1
while (increment<4):
    match={}
    for prev_est_id,prev_gt_id in prev_match_id.items():
        found_est_person=None
        found_gt_person=None
        # since the original est_people list remain the same order, the the sample index probably is the same matches 
        # find the matched index 
        for est_person in est_people:
            est_index=est_people.index(est_person)
            if est_index==prev_est_id:
                found_est_person=est_person
                break
        for gt_person in gt_people:
            gt_index=gt_people.index(gt_person)
            if gt_index==prev_gt_id:
                found_gt_person=gt_person
                break
        if found_est_person and found_gt_person:
            dist=abs(found_est_person-found_gt_person)
            if dist<=1:
                match[found_est_person]=found_gt_person
    print("{0} matches".format(increment))
    print(match)
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
    print("dist_matrix:\n")
    print(dist_matrix)

    if dist_matrix:
        munkres=Munkres()
        # munkres2=munkres.Munkres()

        indexes=munkres.compute(dist_matrix)
        for i , j in indexes:
            no_restrict_matches[est_people[i]]=gt_people[j]
            if dist_matrix[i][j]<2:
                match[est_people[i]]=gt_people[j]
        print("assigned_result:\n")
        print(indexes)
        print("assigned_matches:\n")
        print(match)
        print("completed_matches:\n")
        print(no_restrict_matches)
    print("after computing the {0} matches".format(increment))
    print(match)
    fp_set=set()
    for est_person in est_people:
        if est_person not in match:
            print("false positive person in tracked object:{0}".format(est_person))
            fp_set.add(est_person)
            false_positives+=1

    miss_set=set()
    for gt_person in gt_people:
        if gt_person not in match.values():
            print("miss a person: {0}".format(gt_person))
            miss_set.add(gt_person)
            miss+=1

    id_switches_set=set()
    for est_person, gt_person in match.items():
        est_index=est_people.index(est_person)
        gt_index=gt_people.index(gt_person)
        if est_index in prev_match_id:
            if prev_match_id[est_index]==gt_index:
                correct+=1
            else:
                id_switches_set.add(est_person)
                id_switches_count+=1
        elif gt_index in prev_match_id.values():
            id_switches_set.add(gt_person)
            id_switches_count+=1
        else:
            # new tracked people
            correct+=1

    # calculate motp
    for est_person,gt_person in match.items():
        dist=abs(est_person-gt_person)
        MOTP_dist_cum+=dist
        MOTP_dist_count+1



    for est_person,gt_person in match.items():
        est_index=est_people.index(est_person)
        gt_index=gt_people.index(gt_person)
        prev_match_id[est_index]=gt_index


    est_people=[x+increment for x in est_people]
    gt_people=[x+increment for x in gt_people]
    increment+=1
# note that if we both increase the est_people and gt_people, the match list won't change. the action of increasing(equal to movement of the tracked object) cause the position changed in est and gt list 





        
                









