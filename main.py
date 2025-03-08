import json

import canvasapi

# Load API token and Canvas URL
with open("canvas_info.json", "r") as f:
    info = json.load(f)

API_TOKEN = info["api_token"]
CANVAS_URL = info["canvas_url"]
CURRENT_YEAR = "2025"

canvas = canvasapi.Canvas(CANVAS_URL, API_TOKEN)


def get_courses(current_only=True):
    canvas_courses: list[canvasapi.canvas.Course] = canvas.get_courses()
    result_courses = []

    for course in canvas_courses:
        try:
            if not current_only or CURRENT_YEAR in course.name:
                result_courses.append(course)
        except AttributeError:
            pass
    return result_courses


if __name__ == '__main__':
    courses = get_courses()

    # Main menu selection
    print("Select an option:")
    print("1) List a course roster")
    print("2) Find students who share multiple classes with you")

    while True:
        option = input("Enter your choice (1 or 2): ").strip()
        if option in {'1', '2'}:
            break
        print("Invalid input. Please enter 1 or 2.")

    if option == '1':
        # Course selection
        print("\nSelect a Course:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}) {course.name:25} --- {course.id:7}")

        selected_course = None
        while True:
            response = input("Enter the number of the course: ").strip()
            if response.isdigit():
                index = int(response)
                if 1 <= index <= len(courses):
                    selected_course = courses[index - 1]
                    break
            print("Invalid input. Please try again.")

        print(f"\nSelected course: {selected_course.name} (ID: {selected_course.id})\n")

        # Course roster listing
        print("Course Roster:")
        user_list = list(selected_course.get_users())
        user_list.sort(key=lambda x: x.name)
        for user in user_list:
            print(f"{user.name} ({user.id})")

    elif option == '2':
        # Shared students report
        current_user = canvas.get_current_user()
        current_user_id = current_user.id
        student_courses = {}
        student_users = {}

        for course in courses:
            for user in course.get_users():
                if user.id != current_user_id:
                    if user.id not in student_courses:
                        student_courses[user.id] = [course]
                        student_users[user.id] = user
                    else:
                        student_courses[user.id].append(course)

        for user, course_list in student_courses.items():
            student_user = student_users[user]

        print("\nStudents who share multiple classes with you:\n")
        for user, shared_courses in sorted(student_courses.items(), key=lambda x: -len(x[1])):
            if len(shared_courses) > 1:
                student_user = student_users[user]
                print(f"{student_user.name}: {', '.join([course.name for course in shared_courses])}")
