choose = int(input("choose the code to run (0/1/2): "))
if choose == 0:
    temp = 45.0
    if temp <40:
        print("Cooling ON")
    print("check complete")
elif choose == 1:
    temp = float(input("Enclosure temperature: "))
    if temp < 0:
        mode = "Heating ON"
    elif temp <40:
        mode = "Normal"
    elif temp <=60:
        mode = "Cooling ON"
    else:
        mode = "shutdown"
    print("operating mode = ",mode)
elif choose == 2:
    marks = 95
    if marks >=40:
        grade = "pass"
    elif marks >= 95:
        grade = "distinction"
    else:
        grade = "fail"
    print(grade)
else:
    print("Invalid choice. Please choose 0 or 1.")  