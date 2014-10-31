__author__ = 'Luke'
#1. L =[[1,2],[1,-1],[5,8],[-4,-2],[4,3]]
# D. L is a list of ordered pairs. Use a for loop to create a list M which contains the largest element for each of the ordered pairs and the
# ordered pairs as a tuple.
#   M =[(2,[1,2]),(1,[1,-1]),(8,[5,8]),(-2,[-4,-2]),(4,[4,3])]
# (max is a built in function)
# S. Sort M
# U. Return the list L sorted in order by the maximum element. If there is a tie how is the list sorted?

# Your program should work for any list L, not just the one I provided here.

#2. Write a function mean which will compute the average of any number of numbers:
# mean(1,2) = 1.5
# mean(1,2,3) = 2
# etc.

L =[[1,2],[1,-1],[5,8],[-4,-2],[4,3]]
M =[(2,[1,2]),(1,[1,-1]),(8,[5,8]),(-2,[-4,-2]),(4,[4,3])]

def sort_by_length(*list):
    t=[]
    for num in list:
        t.append((len(num),num))
    t.sort(reverse=True)
    res = []
    for length,num in t:
        res.append(num)
    return res

def mean(one,two):
    a=range(one,two)
    mean=(sum(a)/len(a))
    return mean()