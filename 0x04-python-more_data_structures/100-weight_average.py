#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == None:
        return 0
    product = 1
    weight_sum = 0
    sum_scores = 0
    for i in my_list:
        (scores, weight) = i
        sum_scores += scores * weight
        weight_sum += weight
    average = sum_scores / weight_sum if weight_sum > 0 else 0
    return average
