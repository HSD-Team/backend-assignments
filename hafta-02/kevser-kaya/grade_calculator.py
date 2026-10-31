#Calculate the average  
def average(midterm, final_exam):
    result=midterm*0.40+final_exam*0.60
    return result 

#Determine the letter grade based on the average  
def letter_grade(avg):
    if avg >=90:
        return 'AA'
    elif avg >=85:
        return 'BA'
    elif avg >=80:
        return 'BB'
    elif avg >=75:
        return 'CB'
    elif avg >=70:
        return 'CC'
    elif avg >=65:
        return 'DC'
    elif avg >=60:
        return 'DD'
    elif avg >=50:
        return 'FD'
    else:
        return 'FF'


#Checks if the student passes (avg>=60)
def is_passing(avg):
    return avg >=60


students=[]
print ("Pleae enter the information for 5 students:  \n")
#Collects data for 5 students 
for i in range (1,6):
    name=input("Student's name: ")
    midterm=float(input("Midterm grade :"))
    final_exam=float(input(" Final exam grade :"))

    avg=average(midterm,final_exam)
    grade =letter_grade(avg)
    students.append((name,avg,grade))
    print()


#Displays calculated student results
print("\t Student Grade Results \t")
for name,avg,grade in students:
    print(f" {name } - Average : {avg:.1f}   - Letter Grade : {grade}")