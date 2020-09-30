# K,rooms = int(input()),list(map(int, input().split()))
k=5
s="1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2"

rooms=list(map(int,s.split()))
rooms_simple=set(rooms)
single,multiple=set(),set()
for room in rooms: single.add(room) if room not in single else multiple.add(room)
print(rooms_simple.difference(multiple).pop())

# print(rooms)
# print(set(rooms))
# print(len(rooms)//K)


