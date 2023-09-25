n, k = map(int, input().split())
k_arr = list(map(int, input().split()))
students = []
for idx in range(n):
    our_input = [int(el) for el in input().split()]
    students.append({'rate': our_input[0], 'priorities': our_input[2:], 'idx': idx})
students = sorted(students, key=lambda x: x['rate'])

result = []
for student in students:
    result.append(student['priorities'][0])
print(*result)
