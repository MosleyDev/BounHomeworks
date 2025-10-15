tower_width = int(input("Enter tower width: "))
tower_height = int(input("Enter tower height: "))
car_width = int(input("Enter car width: "))
#---------------HOMEWORK STARTS BELOW---------------#
head_height = tower_width // 2
frame_width = 20 + car_width
frame_height = tower_height + head_height

for t in range(frame_width + 1):
    for y in range(frame_height):
        for x in range(frame_width):
            #Drawing the Car
            if(y == frame_height - 6 or y == frame_height - 4):
                if(x >= 20 - t and x <= 19 + car_width - t):
                    print("=", end="")
                    continue
            elif(y == frame_height - 5):
                if(x ==  20 - t):
                    print("(", end="")
                    continue
                elif(x == 19 + car_width - t):
                    print(")", end="")
                    continue
                elif(x > 20 - t and x < 19 + car_width - t):
                    print(" ", end="")
                    continue

            #Drawing the Tower
            if x >= 0 and x < tower_width:
                if y == frame_height - 1 or y == head_height:
                    print("X", end="")
                    continue
            if(x == 0 or x == tower_width - 1):
                if(y > tower_width // 2 and y < frame_height - 1):
                    print("|", end="")
                    continue
            if(y < head_height):
                if(x < head_height):
                    if(x + y == head_height - 1):
                        print("/", end="")
                        continue
                elif(x >= head_height and x < tower_width):
                    if(x - y == head_height):
                        print("\\", end="")
                        continue

            print(" ", end="")
        print()
    print()