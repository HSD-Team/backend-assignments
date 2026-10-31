def average(midterm: float, final_exam:float) -> float:
    return midterm * 0.4 + final_exam * 0.6

def letter_grade(avg:float) -> str:
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
    
    
def is_passing(avg:float) -> bool:
    return avg >= 60    
    




print("Not hesaplayıcı")
avg = average(70,85)
print(avg)
print(letter_grade(avg))
print(letter_grade(92))
print(letter_grade(42))
print(is_passing(avg))
print(is_passing(55))