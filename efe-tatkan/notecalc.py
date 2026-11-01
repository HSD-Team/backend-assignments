import sys
import re
import random

def average(midterm, final_exam):
    return int(0.4*midterm+0.6*final_exam+0.01)

def letter_grade(avg : int):
    ls = ['D','C','B','A']
    d0 = (avg+5)//10-6
    d1 = avg//10-6
    if avg>=60: 
        return ls[max(d1, 0)] + ls[max(d0, 0)] 
    else: 
        return 'FD' if avg >= 50 else 'FF'

def is_passing(avg : int):
    return True if avg>=60 else False

if len(sys.argv)==3:
    a=sys.argv[1]
    b=sys.argv[2]
    if re.search(r"^\d+$", a+b) == None:
        print("notecalc error: please enter integers only.")
        exit(-1)
    a = int(a)
    b = int(b)
    if a>100 or b>100:
        print("notecalc error: the input is out of range (0-100).")
        exit(-1)
    print(f"your average grade: {average(a,b)} \n your letter grade: {letter_grade(average(a,b))}")

else:
    print("notecalc: calculate your average grade based on a midterm and final exam score.")
    print("usage: notecalc.py <MIDTERM> <FINAL_EXAM>")
    print("all arguments weren't provided, running demo:")
    for i in range(0,5):
        a=random.randint(0,100)
        b=random.randint(0,100)
        print(f"STUDENT {i} || exam scores: {a}, {b} | average: {average(a,b)} | letter grade: {letter_grade(average(a,b))} \n")