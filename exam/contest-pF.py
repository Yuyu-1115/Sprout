#pF
class Student:
    def __init__(self, num, known) -> None:
        self.num = num
        self.known = known

def record(recorded, student: Student):
    recorded[student.num] = 1
    for s in student.known:
        if recorded[s] != 1:
            recorded[s] = 1
            record(recorded, stu_list[s])
    return recorded
        

n = int(input())
stu_list = list()

for i in range(n):
    data = list(map(int, input().split()))
    stu_list.append(Student(data[0], data[1:]))

for i in range(n):
    if 0 in record([0 for i in range(n)], stu_list[i]):
        print("False")
        break
else:
    print("True")

