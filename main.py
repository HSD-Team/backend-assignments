
def average(midterm: float, final_exam: float):
    return (midterm * 0.4)+(final_exam * 0.6)


def letter_grade(avg: float):
    if avg >= 90:
        return "AA"
    elif avg >= 85:
        return "BA"
    elif avg >= 80:
        return "BB"
    elif avg >= 75:
        return "CB"
    elif avg >= 70:
        return "CC"
    elif avg >= 65:
        return "DC"
    elif avg >= 60:
        return "DD"
    elif avg >= 50:
        return "FD"
    else:
        return "FF"
    

def is_passing(avg: float):
    return avg>=60

def is_valid(prompt: str):
    while True:
        try:
            score = float(input(prompt))
            if 0<=score<=100:
                return score
            print("Grades need to be in range of 0-100. Try again.")
        except ValueError:
            print("Error: Please enter a valid number.")

                
students = []

def main():
    for i in range(5):
        name = input(f"Please enter {i+1}. student's name: ")
        midterm = is_valid(f"Please enter {name}'s midterm grade: ")
        final_exam = is_valid(f"Please enter {name}'s final exam grade: ")
        

        avg = average(midterm, final_exam)
        grade = letter_grade(avg)
        
        current_student = {
            "Names": name,
            "Average": avg,
            "Letter Grade": grade
        }
        
        students.append(current_student)

    print("\n" + "=" * 45)
    print(f"{'Name':<15} | {'Average':<4} | {'Letter Grade':<3} ")
    print("-" * 45)
    
    for student in students:
        print(f"{student['Names']:<16}| {student['Average']:<9.1f}| {student['Letter Grade']:<14}")

    print("-" * 45)


main()


