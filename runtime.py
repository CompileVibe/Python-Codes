choose = int(input("Choose Code to print[0/1/2]: "))
if choose == 0:
    name = "alpha"
    battery = 78.456
    print("robot", name, "at", battery,"%")
    print(f"robot {name} at {battery}%")
    print(f"robot {name} at {battery:.1f}%")
    print(f"{name:<10} | {battery:>8.2f}%")
elif choose == 1:
    cap = float(input("Enter battery capacity: ")) 
    draw = float(input("Enter battery draw: "))
    runtime = cap / draw
    print(f"the battery will run for {runtime:.2f} hours")
elif choose == 2:
    capacity = float(input("Enter battery capacity mah: "))
    load = float(input("current draw (mah): "))
    hours = capacity / load
    print(f"Estimated runtime: {hours:.2f} hours")
else:  
    print("Invalid choice. Please choose 0, 1, or 2.")  