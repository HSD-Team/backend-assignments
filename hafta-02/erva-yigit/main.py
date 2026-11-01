def average(midterm: float, final_exam: float)->float:
    avg = midterm * 0.4 + final_exam * 0.6 
    return avg

def letter_grade(avg: float)-> str:
    if 90 <= avg:
        return "AA"
    if 85 <= avg:
        return "BA"
    if 80 <= avg:
        return "BB"
    if 75 <= avg:
        return "CB"
    if 70 <= avg:
        return "CC"
    if 65 <= avg:
        return "DC"
    if 60 <= avg:
        return "DD"
    if 50 <= avg:
        return "FD"
    return "FF"

def is_passing(avg: float)-> bool:
    if avg >= 60:
        return True
    return False


for _ in range(5):
    student_name = input("Student's Name: ")
    
    while True:
        try:
            student_midterm = int(input("Student's Midterm Grade: "))
            if 0<= student_midterm <=100:
                break
        except ValueError:
            print("Invalid grade. Please ensure your grade is between 0 and 100.")
            student_midterm = int(input("Student's Midterm Grade: "))
        print("Invalid grade. Please ensure your grade is between 0 and 100.")

    while True:
        try:
            student_fin = int(input("Student's Final Grade: "))
            if 0<= student_fin <=100:
                break
        except ValueError:
            print("Invalid grade. Please ensure your grade is between 0 and 100.")
            student_fin = int(input("Student's Final Grade: "))
        print("Invalid grade. Please ensure your grade is between 0 and 100.")

    student_avg = average(student_midterm,student_fin)

    print(f"""
    Student's Name: {student_name}
    Student's Average Grade: {student_avg}
    Student's Letter Grade: {letter_grade(student_avg)}
    """)
