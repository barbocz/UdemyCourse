# student_names=[]
# student_scores=[]
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#         student_names.append(name)
#         student_scores.append(scores)
#     query_name = input()
#
# dict=dict(zip(student_names,student_scores))
#
# for item in dict.items():
#     if (item[0]==query_name):
#         print("%.2f" %  (sum(item[1]) / len(item[1])))

# friends = ["Rolf", "Bob", "Jen", "Anne"]
# time_since_seen = [{1,2}, {7}, {10,20}, {11,2}]
#
# dict = {
#     friends[i]: time_since_seen[i]
#     for i in range(len(friends))
#
# }
#
# for item in dict.items():
#     if (item[0]=="Jen"):
#         print(sum(item[1]) / len(item[1]))


