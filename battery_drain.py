battery = 100
minutes = 0
while battery >20:
    battery -= 7
    minutes += 1
print(f"low-battery alert after {minutes} minutes ({battery}%)")