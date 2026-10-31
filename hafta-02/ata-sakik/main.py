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


def print_row(name:str, midterm:float, final_exam:float) -> None:
    avg = average(midterm, final_exam)
    status = "Geçti" if is_passing(avg) else "Kaldı"
    print(f"{name:<10} {avg:10.2f} {letter_grade(avg):<6} {status}")
    
    
def read_grade(prompt:str) -> float:
    while True:
        text=input(prompt)
        try:
            grade=float(text.replace(",", "."))    
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin. (ör: 75.5)")
            continue
        if 0 <= grade <= 100:
            return grade
        print("Not 0 ile 100 arasında olmalıdır. Lütfen tekrar deneyin.")

def main() -> None:
    names = ["Ayşe","Mehmet","Zeynep","Can","Elif"]
    midterms=[72,45,90,60,85]
    finals=[88,60,95,40,70]
    
    print(f"{'Ad':<10} {'Ortalama':<10} {'Harf':<6}Durum")
    print("-" * 32)
    
    
    for i in range (len(names)):
        avg = average(midterms[i],finals[i])
        status = "Geçti" if is_passing(avg) else "Kaldı"
        print(f"{names[i]:<10} {avg:10.2f} {letter_grade(avg):<6} {status}")
    print("-" * 32)
    
    
    answer=input("Kendi notunuzu hesaplamak ister misiniz? (e/h): ")
    if answer.strip().lower()=="e":
        name=input("Adınız: ")
        midterm=read_grade("Vize notunuzu girin: ")
        final_exam=read_grade("Final notunuzu girin: ")
        print_row(name, midterm, final_exam)
main()        