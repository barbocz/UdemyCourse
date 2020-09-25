# students=[]
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name,score])



students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

grades=[grade[1] for grade in students]
sorted_grades= sorted(grades)

min=sorted_grades[0]

for i in range(len(sorted_grades)):
    if (sorted_grades[i]>min):
        second_lowest=sorted_grades[i];
        break
sorted_names=[]
for name,grade in students:
    if (grade==second_lowest):
        sorted_names.append(name)

for name in sorted(sorted_names):
    print(name)

