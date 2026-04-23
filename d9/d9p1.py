import math 

file = open("d9/d9p1input.txt", "r")
content = file.read()
input_values = content.split('\n')

all_coordinates = []
for coordinate in input_values:
	x,y = coordinate.split(',')
	all_coordinates.append((x,y))

sol = 0
for x_1, y_1 in all_coordinates:
	for x_2, y_2 in all_coordinates:
		x_1,y_1,x_2,y_2 = int(x_1),int(y_1),int(x_2),int(y_2)
		sol = max(int((abs(x_1 - x_2) + 1) * (abs(y_1 - y_2) + 1)), sol)

print("max area:")
print(sol)
