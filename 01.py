##If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
##Find the sum of all the multiples of 3 or 5 below 1000.


mylist = [ ]
for item in range(1000):
    if item%3 == 0 or item %5 ==0:
        mylist.append(item)
     

print(sum(mylist))
