def average(midterm:float,final_exam:float) ->float:
    return (midterm*0.4)+(final_exam*0.6)

def letter_grade(avg:float) ->str:
    if avg>=90:
        return "AA"
    elif avg>=85:
        return "BA"
    elif avg>=80:
        return "BB"
    elif avg>=75:
        return "CB"
    elif avg>=70:
        return "CC" 
    elif avg>=65:
        return "DC"
    elif avg>=60:
        return "DD"
    elif avg>=50:
        return "FD"
    else:
        return "FF"


def is_passing(avg:float) ->bool:
    if avg>=60:
        return True
    else:
        return False

def get_grade(prompt:str) ->float:
    while True:
        value=input(prompt)
        if value.isdigit():
            grade=float(value)
            if 0<=grade<=100:
                return grade
            else:
                print("Lütfen 0 ile 100 arasında bir not giriniz.")
        else:
            print("Lütfen geçerli bir sayı giriniz.")


def main():
    students=[]
    for i in range(5):
        name=input("Öğrencinin adı: ")
        midterm=get_grade("Vize notu: ")
        final_exam=get_grade("Final notu: ")

        avg=average(midterm,final_exam)
        grade=letter_grade(avg)
        passing=is_passing(avg)
        students.append((name, avg, grade, passing))
    
    print(f"{'İsim:':<10}{'Ortalama':<10}{'Harf Notu':<10}{'Durum':<6}")

    for name, avg, grade,passing in students:
        print(f"{name:<10}{avg:<10.2f}{letter_grade(avg):<10}{passing}") 
        

main()

