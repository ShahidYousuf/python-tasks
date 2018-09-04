count_A = int(input())
a = list(map(int, input().split()))[:count_A]
A = set(a)
count_sets = int(input())
for count in range(count_sets):
    args = input().split()
    other_set_list = list(map(int, input().split()))[:int(args[1])]
    other_set = set(other_set_list)
    try:
        if args[0] == "intersection_update":
            A.intersection_update(other_set)
        if args[0] == "update":
            A.update(other_set)
        if args[0] == "difference_update":
            A.difference_update(other_set)
        if args[0] == "symmetric_difference_update":
            A.symmetric_difference_update(other_set)
    except (Exception):
        continue

print(sum(A))
    

