def selection_sort(l):
    for c in range(len(l)):
        lowest_idx = c 
        for s in range(c, len(l)):
            if l[s] < l[lowest_idx]:
                lowest_idx = s
        if lowest_idx != c:
            tmp = l[c]
            l[c] = l[lowest_idx]
            l[lowest_idx] = tmp
    return l

mylist = [10, 6, 3, 20, 12, 4, 5]
print(mylist)
print(selection_sort(mylist))
