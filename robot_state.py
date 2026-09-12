chooose = int(input("Choose code to print [0/1]"))
if chooose == 0:
    robot_name = "alpha"
    battery_pct = 78.5
    is_docked = True
    waypoints = 12

    print(robot_name, battery_pct, is_docked, waypoints)


    print(type(robot_name), type(battery_pct), type(is_docked), type(waypoints))
elif chooose == 1:
    robot_arm = 15
    robot_leg = 30
    robot_head = "Node_Mcu"
    battery_level = 52
    print("robot_arm length:", robot_arm)
    print("robot_leg length:", robot_leg)
    print("robot_head = ", robot_head)
    print("battery % = ", battery_level)

    if battery_level < 50:
        print("Warning: The battery level is less than 50%.")

else: 
    print("Invalid choice. Please choose 0 or 1.")