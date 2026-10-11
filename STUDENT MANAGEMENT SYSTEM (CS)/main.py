import turtle

#Named constants 
PASSING_GWA = 3.00
MAX_GRADE = 5.00
MIN_PERCENT = 0.0
MAX_PERCENT = 100.0
ID_LENGTH = 10
MAX_NAME = 30
ROWS_PER_PAGE = 7
FILE_NAME = "students.txt"
TERMS = ["Prelims", "Midterms", "Semi-finals", "Finals"]

ID = 0
NAME = 1
COURSE = 2
YEAR = 3
FIRST_GRADE = 4

students = []
buttons = []
current = 0
list_page = 0
search_term = ""
message = ""
teacher = "Teacher"

rng_state = 12345
RNG_MOD = 2147483647


#Saving part nia siya
def load_students():
    file = open(FILE_NAME, "a")
    file.close()
    file = open(FILE_NAME, "r")
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 8:
            students.append(parts)
    file.close()


def save_students():
    file = open(FILE_NAME, "w")
    for s in students:
        file.write(",".join(s) + "\n")
    file.close()


# Mao nani ang grading table
def percent_to_grade(p):
    if p >= 97:    return 1.00, "Excellent"
    elif p >= 94:  return 1.25, "Excellent"
    elif p >= 91:  return 1.50, "Very Good"
    elif p >= 88:  return 1.75, "Very Good"
    elif p >= 85:  return 2.00, "Above Average"
    elif p >= 82:  return 2.25, "Above Average"
    elif p >= 79:  return 2.50, "Average"
    elif p >= 76:  return 2.75, "Average"
    elif p >= 75:  return 3.00, "Passing"
    elif p >= 72:  return 3.25, "Conditional"
    elif p >= 69:  return 3.50, "Conditional"
    elif p >= 66:  return 3.75, "Failed"
    elif p >= 65:  return 4.00, "Failed"
    else:          return 5.00, "Failed"


def grade_to_desc(g):
    if g <= 1.25:   return "Excellent"
    elif g <= 1.75: return "Very Good"
    elif g <= 2.25: return "Above Average"
    elif g <= 2.75: return "Average"
    elif g <= 3.00: return "Passing"
    elif g <= 3.50: return "Conditional"
    else:           return "Failed"


# The actual grade
def count_grades(s):
    count = 0
    for t in range(len(TERMS)):
        if s[FIRST_GRADE + t] != "":
            count += 1
    return count


def get_gwa(s):
    """GWA = average of the grades entered so far (0.0 if there are none)."""
    count = count_grades(s)
    if count == 0:
        return 0.0
    total = 0.0
    for t in range(len(TERMS)):
        if s[FIRST_GRADE + t] != "":
            total += float(s[FIRST_GRADE + t])
    return round(total / count, 2)


def is_complete(s):
    return count_grades(s) == len(TERMS)


def get_status(s):
    if count_grades(s) == 0:
        return "NO GRADES"
    elif not is_complete(s):
        return "INCOMPLETE"
    elif get_gwa(s) <= PASSING_GWA:
        return "PASSED"
    elif get_gwa(s) <= 3.50:
        return "CONDITIONAL"
    else:
        return "FAILED"


def get_color(status):
    if status == "PASSED":
        return "seagreen"
    elif status == "FAILED":
        return "firebrick"
    elif status == "CONDITIONAL":
        return "goldenrod"
    else:
        return "gray"


def first_missing_term(s):
    """Return the first term (1-4) without a grade, or 1 if all are filled."""
    for t in range(len(TERMS)):
        if s[FIRST_GRADE + t] == "":
            return t + 1
    return 1


# the design using drawings sa turtle
screen = turtle.Screen()
screen.setup(640, 560)
screen.title("Student Management System")
screen.bgcolor("white")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.pensize(2)


def write_text(x, y, text, size=14, style="normal", color="black", align="left", family="Arial"):
    pen.goto(x, y)
    pen.color(color)
    pen.write(text, align=align, font=(family, size, style))


def draw_rect(x, y, w, h, line_color, fill_color):
    """(x, y) is the bottom-left corner."""
    pen.penup()
    pen.goto(x, y)
    pen.color(line_color, fill_color)
    pen.pendown()
    pen.begin_fill()
    pen.goto(x + w, y)
    pen.goto(x + w, y + h)
    pen.goto(x, y + h)
    pen.goto(x, y)
    pen.end_fill()
    pen.penup()


def draw_circle(cx, cy, r, line_color, fill_color):
    """(cx, cy) is the center. Turtle draws a circle starting from its bottom."""
    pen.penup()
    pen.goto(cx, cy - r)
    pen.setheading(0)
    pen.color(line_color, fill_color)
    pen.pendown()
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()
    pen.penup()


def draw_triangle(cx, cy, size, line_color, fill_color):
    pen.penup()
    pen.goto(cx, cy + size)
    pen.color(line_color, fill_color)
    pen.pendown()
    pen.begin_fill()
    pen.goto(cx + size, cy - size)
    pen.goto(cx - size, cy - size)
    pen.goto(cx, cy + size)
    pen.end_fill()
    pen.penup()


def draw_button(x, y, w, h, text, color, action, size=13, family="Arial"):
    """Draw a button and remember its area so clicks can be detected."""
    draw_rect(x, y, w, h, "black", color)
    write_text(x + w / 2, y + h / 2 - size * 0.6, text, size, "bold", "white", "center", family)
    buttons.append([x, y, w, h, action])


def new_screen():
    pen.clear()
    buttons.clear()


def draw_message():
    if message != "":
        color = "firebrick" if message[:6] == "Error:" else "darkgreen"
        write_text(0, -258, message, 12, "bold", color, "center")


# The screen

def show_menu():
    new_screen()
    draw_rect(-320, 190, 640, 75, "navy", "navy")
    write_text(0, 213, "STUDENT MANAGEMENT SYSTEM", 24, "bold", "white", "center")
    write_text(0, 155, "Welcome, " + teacher + "!", 15, "bold", "navy", "center")
    write_text(0, 130, "Students saved: " + str(len(students)), 12, "normal", "gray", "center")
    draw_button(-130, 70, 260, 40, "Add Student", "seagreen", "add")
    draw_button(-130, 20, 260, 40, "Student List", "steelblue", "list")
    draw_button(-130, -30, 260, 40, "View Profiles", "darkorange", "profiles")
    draw_button(-130, -80, 260, 40, "Random Student", "purple", "random")
    draw_button(-130, -130, 260, 40, "Exit", "gray", "exit")
    draw_message()
    screen.update()


def get_visible():
    """Positions of the students that match the search (all if no search)."""
    result = []
    for i in range(len(students)):
        s = students[i]
        if search_term == "" or search_term in s[ID] or search_term in s[NAME].lower():
            result.append(i)
    return result


def show_list():
    global list_page
    new_screen()
    write_text(0, 215, "STUDENT LIST", 22, "bold", "navy", "center")
    draw_button(-305, 235, 80, 30, "Menu", "gray", "menu", 11)

    visible = get_visible()
    total_pages = (len(visible) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE
    if total_pages == 0:
        total_pages = 1
    if list_page >= total_pages:
        list_page = total_pages - 1

    if search_term == "":
        info = "Showing all students (" + str(len(visible)) + ")"
    else:
        info = "Search: '" + search_term + "'  (" + str(len(visible)) + " found)"
    write_text(0, 185, info, 11, "normal", "gray", "center")

    if len(visible) == 0:
        write_text(0, 60, "No students found.", 14, "normal", "gray", "center")

    start = list_page * ROWS_PER_PAGE
    end = min(start + ROWS_PER_PAGE, len(visible))
    for k in range(start, end):
        s = students[visible[k]]
        status = get_status(s)
        gwa_text = f"{get_gwa(s):.2f}" if count_grades(s) > 0 else "--"
        text = f"{s[ID]} {s[NAME][:16]:<16} {s[COURSE][:6]:<6} {gwa_text:>5} {status:<11}"
        draw_button(-260, 140 - (k - start) * 40, 520, 32, text, get_color(status),
                    "open:" + str(visible[k]), 11, "Courier")

    write_text(0, -140, "Page " + str(list_page + 1) + " of " + str(total_pages),
               11, "normal", "gray", "center")
    draw_button(-262, -200, 120, 38, "< Prev", "steelblue", "pageprev")
    draw_button(-127, -200, 120, 38, "Search", "darkorange", "search")
    draw_button(8, -200, 120, 38, "Show All", "seagreen", "showall")
    draw_button(143, -200, 120, 38, "Next >", "steelblue", "pagenext")
    draw_message()
    screen.update()


def show_profile():
    new_screen()
    draw_button(-305, 235, 80, 30, "Menu", "gray", "menu", 11)
    draw_button(225, 235, 80, 30, "List", "steelblue", "showlist", 11)

    if len(students) == 0:
        write_text(0, 50, "No students yet. Add one from the menu.", 14, "normal", "gray", "center")
        draw_message()
        screen.update()
        return

    s = students[current]
    status = get_status(s)
    color = get_color(status)
    count = count_grades(s)

    draw_rect(-230, -160, 460, 350, color, "white")
    write_text(0, 168, "Student " + str(current + 1) + " of " + str(len(students)),
               11, "normal", "gray", "center")

    draw_circle(0, 120, 30, color, color)
    write_text(0, 108, s[NAME][0].upper(), 26, "bold", "white", "center")
    write_text(0, 55, s[NAME], 20, "bold", "black", "center")

    write_text(-200, 20, "ID: " + s[ID], 13)
    write_text(-200, -5, "Course: " + s[COURSE], 13)
    write_text(-200, -30, "Year: " + s[YEAR], 13)
    for t in range(len(TERMS)):
        value = s[FIRST_GRADE + t]
        if value != "":
            shown = f"{float(value):.2f} ({grade_to_desc(float(value))})"
        else:
            shown = "--"
        write_text(20, 20 - t * 25, TERMS[t] + ": " + shown, 12)

    if count == 0:
        write_text(0, -90, "GWA: --  (no grades yet)", 15, "bold", "black", "center")
    else:
        label = "GWA" if is_complete(s) else "GWA so far"
        write_text(0, -90, f"{label}: {get_gwa(s):.2f}   ({count} of {len(TERMS)} grades)",
                   15, "bold", "black", "center")

    remark = grade_to_desc(get_gwa(s)) if count > 0 else ""
    write_text(0, -140, status + ("  -  " + remark if remark != "" else ""), 16, "bold", color, "center")
    icon_x = -230
    if status == "PASSED":
        draw_circle(icon_x, -128, 16, color, color)
        write_text(icon_x, -133, "OK", 9, "bold", "white", "center")
    elif status == "FAILED":
        draw_triangle(icon_x, -126, 16, color, color)
        write_text(icon_x, -138, "!", 12, "bold", "white", "center")
    else:
        draw_rect(icon_x - 14, -142, 28, 28, color, color)
        write_text(icon_x, -135, "...", 12, "bold", "white", "center")

    draw_button(-274, -222, 100, 38, "< Prev", "steelblue", "prev", 12)
    draw_button(-162, -222, 100, 38, "Add Grade", "seagreen", "grade", 12)
    draw_button(-50, -222, 100, 38, "Update", "darkorange", "update", 12)
    draw_button(62, -222, 100, 38, "Delete", "firebrick", "delete", 12)
    draw_button(174, -222, 100, 38, "Next >", "steelblue", "next", 12)
    draw_message()
    screen.update()


# Actions

def id_exists(student_id):
    for s in students:
        if s[ID] == student_id:
            return True
    return False


def add_student():
    global current, message

    student_id = screen.textinput("Add Student", "Student ID number (10 digits, e.g. 2026303095):")
    if student_id is None:
        return
    student_id = student_id.strip()

    if not student_id.isdigit() or len(student_id) != ID_LENGTH:
        message = "Error: the ID must be exactly " + str(ID_LENGTH) + " digits."
        show_menu()
        return
    if id_exists(student_id):
        message = "Error: that ID number is already used."
        show_menu()
        return

    name = screen.textinput("Add Student", "Enter student name:")
    if name is None:
        return
    course = screen.textinput("Add Student", "Enter course (e.g. BSCS):")
    if course is None:
        return
    year = screen.numinput("Add Student", "Year level (1-4):", 1, 1, 4)
    if year is None:
        return

    name = name.replace(",", "").strip().title()
    course = course.replace(",", "").strip().upper()

    if name == "" or course == "":
        message = "Error: name and course cannot be empty."
        show_menu()
    elif len(name) > MAX_NAME:
        message = "Error: name must be " + str(MAX_NAME) + " characters or less."
        show_menu()
    else:
        students.append([student_id, name, course, str(int(year)), "", "", "", ""])
        save_students()
        current = len(students) - 1
        message = "Student added! Use Add Grade to enter scores."
        show_profile()


def add_grade():
    global message

    s = students[current]
    term = screen.numinput("Add Grade", "Term: 1=Prelims 2=Midterms 3=Semi-finals 4=Finals",
                           first_missing_term(s), 1, len(TERMS))
    if term is None:
        return
    t = int(term) - 1
    score = screen.numinput("Add Grade",
                            TERMS[t] + " raw score in percent (" + str(int(MIN_PERCENT)) + "-" + str(int(MAX_PERCENT)) + "):",
                            75.0, MIN_PERCENT, MAX_PERCENT)
    if score is None:
        return

    grade, desc = percent_to_grade(score)
    s[FIRST_GRADE + t] = str(grade)
    save_students()
    message = TERMS[t] + ": " + f"{score:.1f}% = {grade:.2f} ({desc})"
    show_profile()


def update_student():
    global message

    s = students[current]
    name = screen.textinput("Update Student", "New name (blank = keep '" + s[NAME] + "'):")
    if name is None:
        return
    course = screen.textinput("Update Student", "New course (blank = keep '" + s[COURSE] + "'):")
    if course is None:
        return
    year = screen.numinput("Update Student", "Year level (1-4):", float(s[YEAR]), 1, 4)
    if year is None:
        return

    name = name.replace(",", "").strip().title()
    course = course.replace(",", "").strip().upper()
    name = name if name != "" else s[NAME]
    course = course if course != "" else s[COURSE]

    if len(name) > MAX_NAME:
        message = "Error: name must be " + str(MAX_NAME) + " characters or less."
    else:
        s[NAME] = name
        s[COURSE] = course
        s[YEAR] = str(int(year))
        save_students()
        message = "Student updated."
    show_profile()


def delete_student():
    global current, message

    answer = screen.textinput("Delete Student", "Type YES to delete " + students[current][NAME] + ":")
    if answer is not None and answer.strip().upper() == "YES":
        students.pop(current)
        save_students()
        message = "Student deleted."
        if current >= len(students):
            current = len(students) - 1
        if current < 0:
            current = 0
    show_profile()


def do_search():
    global search_term, list_page

    term = screen.textinput("Search Student", "Enter student ID or name:")
    if term is not None:
        search_term = term.strip().lower()
        list_page = 0
    show_list()


def next_random(limit):
    """Return a number from 0 to limit-1 using the click-seeded generator."""
    global rng_state
    rng_state = (rng_state * 48271 + 11) % RNG_MOD
    return rng_state % limit


def random_student():
    global current, message

    has_students = len(students) > 0
    if not has_students:
        message = "Error: there are no students yet."
        show_menu()
    else:
        current = next_random(len(students))
        message = "Random student picked!"
        show_profile()


def handle(action):
    """Run the action of the clicked button."""
    global current, list_page, search_term, message

    message = ""
    if action == "menu":
        show_menu()
    elif action == "add":
        add_student()
    elif action == "list":
        search_term = ""
        list_page = 0
        show_list()
    elif action == "showlist":
        show_list()
    elif action == "profiles":
        current = 0
        show_profile()
    elif action == "random":
        random_student()
    elif action == "prev":
        current -= 1
        if current < 0:
            current = len(students) - 1
        show_profile()
    elif action == "next":
        current += 1
        if current >= len(students):
            current = 0
        show_profile()
    elif action == "grade":
        add_grade()
    elif action == "update":
        update_student()
    elif action == "delete":
        delete_student()
    elif action == "search":
        do_search()
    elif action == "showall":
        search_term = ""
        list_page = 0
        show_list()
    elif action == "pageprev":
        list_page -= 1
        if list_page < 0:
            list_page = 0
        show_list()
    elif action == "pagenext":
        list_page += 1
        show_list()
    elif action == "exit":
        screen.bye()
    elif action[:5] == "open:":
        current = int(action[5:])
        show_profile()


def on_click(x, y):
    global rng_state
    rng_state = (rng_state * 31 + int(abs(x)) * 7 + int(abs(y)) * 13 + 17) % RNG_MOD
    for b in buttons:
        if x >= b[0] and x <= b[0] + b[2] and y >= b[1] and y <= b[1] + b[3]:
            handle(b[4])
            return


teacher = screen.textinput("Student Management System", "Enter your name (teacher):")
if teacher is None:
    teacher = ""
teacher = teacher.strip().title()
teacher = teacher if teacher != "" else "Teacher"

load_students()
show_menu()
screen.onscreenclick(on_click)
screen.mainloop()