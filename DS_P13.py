# Python Program / Project

student_list = []
def get():
    n = int(input("Enter number of students in class: "))
    for i in range(n):
        k = int(input("Enter roll No.: "))
        student_list.append(k)

def dis():
    for i in student_list:
        print(i, end=" ")

def linear():
    cnt = 0
    key = int(input("Enter roll for searching whether students attended training program: "))
    for i in range(len(student_list)):
        if (key == student_list[i]):
            print("Student attended session at ", i ," location.")
            break
        else:
            cnt += 1
        
        if(cnt == i):
            print("Student not attended session.")

def sentinel():
    item = int(input("Enter roll for searching whether students attended training program: "))
    last = student_list[-1]
    student_list[-1] = item
    i = 0
    while(item != student_list[i]):
        i += 1
    student_list[-1] = last
    if(i<len(student_list)-1 or item == student_list[-1]):
        print("Student attended session at ", i ," location.")
    else:
        print("Student not attended session.")


if __name__ == '__main__':
    get()   # by this method, get the students list
    dis()   # by this method, display students list

    print("\n\n1. Linear Search.")
    print("2. Sentinel Search.")
    print("3. enter any key to exit.")

    ch = int(input("Enter your choice: "))
    if ch == 1:
        linear()
    elif ch == 2:
        sentinel()
    else:
        print("Exit.")
        exit()
        
