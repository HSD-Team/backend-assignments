#I intentionally did not use the "new" notation here, so that there would be an example of both.
def average(midterm, final_exam):
    return midterm * 0.4 + final_exam * 0.6

def letter_grade(average:float) -> str:
    if average >= 90:
        return "AA"
    elif average >= 85:
        return "BA"
    elif average >= 80:
        return "BB"
    elif average >= 75:
        return "CB"
    elif average >= 70:
        return "CC"
    elif average >= 65:
        return "DC"
    elif average >= 60:
        return "DD"
    elif average >= 50:
        return "FD"
    else:
        return "FF"
    
def is_passing(average:float)->bool:
    return average >= 60

def main() -> None:
    names = ["Osman","Meyra","Yaprak","Rana","Can"]
    midterms = [60,70,80,20,40]
    finals = [80,70,60,50,40]

    print(f"{'Name':<10} {'Average':<10} {'Harf':<6} {'Status':>10}") 
    print("-" * 40)
    for i in range(len(names)):
        avg = average(midterms[i], finals[i])
        status = "Pass" if is_passing(avg) else "Fail"
        print(f"{names[i]:<10} {avg} {avg:10.2f} {letter_grade(avg):<6} {status}")
    print("-" * 40)

main()