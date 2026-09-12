choose = int(input("Choose Code to print[0/1]: "))
if choose == 0:
    name = "alpha"
    battery = 78.456
    print("robot", name, "at", battery,"%")
    print(f"robot {name} at {battery}%")
    print(f"robot {name} at {battery:.1f}%")
    print(f"{name:<10} | {battery:>8.2f}%")