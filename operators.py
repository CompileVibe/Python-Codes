choose = int(input("choose the code to run (0/1/2): "))
if choose == 0:
    heading = 359
    turn = 5
    print("wrong :",heading + turn)
    print("right :",(heading + turn) % 360)
    print("negative",(-30)%360)
elif choose == 1:
    distance = 8.0
    limit = 10
    print(distance < limit)
    print(distance == limit)
    print(0<=distance <= limit)
elif choose == 2:
    battery = 45
    print(battery < 5 and battery > 20)
    print(battery > 5 or battery > 90)
    print(not (battery < 5))
else:
    print("Invalid choice. Please choose 0, 1, or 2.")