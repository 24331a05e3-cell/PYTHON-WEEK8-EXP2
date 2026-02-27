#24331A05E3
#list of tuples and sorts the list of tuples in increasing order
tuples = [(1, 3), (4, 1), (2, 2), (5, 0)]
print("Unsorted list: ",tuples)
sorted_tuples = sorted([t[::-1] for t in tuples])
sorted_tuples = [t[::-1] for t in sorted_tuples]
print("Sorted list:", sorted_tuples)
