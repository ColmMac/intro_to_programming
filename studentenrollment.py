
registry = {}

def add_course(code, title, capacity=30):
    code = code.strip().upper()
    if code in registry:
        print("Course already added!")
        return False
    registry[code] = {
        "title": title,
        "capacity": capacity,
        "enrolled": set()
        }
    print(f"{title} successfully added!")
    return True

def enroll_students(code, studentid):
    code = code.upper().strip()
    studentid = studentid.lower().strip()
    if code not in registry:
        print(f"KeyError prevented: {code} does not exist!")
        return False
    course = registry[code]
    if course["capacity"] <= len(course["enrolled"]):
        print(f"Course {code} is full!")
        return False
    course["enrolled"].add(studentid)
    print(f'{studentid} is enrolled into {course["title"]}')
    return True

def get_all_students(course_list):
    all_students = set()
    for code in course_list:
        if code in registry:
            all_students = all_students.union(registry[code]["enrolled"])
    return all_students

print("STUDENT ENROLLMENT")

while True:
    print("1. Add Course \n2. Enroll student \n3. Check Overall Student List\n4. Exit")
    try:
        action = int(input("Please enter an option from 1-4: "))
    except ValueError:
        print("Please enter a valid integer from 1-4.")

    if action == 1:
        code = input("Please enter class code: ")
        title = input("Please enter course name: ")
        add_course(code, title)
    elif action == 2:
        code = input("Please enter class code: ")
        studentid = input("Please enter student id: ")
        enroll_students(code, studentid)
    elif action == 3:
        course_codes = list(registry)
        print(get_all_students(course_codes))
    elif action == 4:
        break