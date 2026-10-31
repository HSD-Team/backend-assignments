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
    

def main() -> None:
    names = ["Ayşe","Mehmet","Zeynep","Can","Elif"]
    midterms=[72,45,90,60,85]
    finals=[88,60,95,40,70]
    
    
    for i in range (len(names)):
        avg = average(midterms[i],finals[i])
        status = "Geçti" if is_passing(avg) else "Kaldı"
        print(f"{names[i]}: avg: {avg:.2f} {letter_grade(avg)} {status}")
        
main()        