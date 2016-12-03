triangles = 0
nlines = 0

triangles_row1 = []
triangles_row2 = []
triangles_row3 = []

def check_if_triangle(sides):
    global triangles
    sides = sorted(sides)
    print(sides)
    if sides[2] < sides[0] + sides[1]:
        triangles += 1


with open("day3.txt") as f:
    for line in f.readlines():
        sides = line.strip().split()
        triangles_row1.append(int(sides[0].strip()))
        triangles_row2.append(int(sides[1].strip()))
        triangles_row3.append(int(sides[2].strip()))
        nlines += 1

all_triangles = triangles_row1 + triangles_row2 +triangles_row3

counter = 0

while counter < len(all_triangles):
    sides_to_check = all_triangles[counter:counter+3]
    print(all_triangles)
    counter +=3
    check_if_triangle(sides_to_check)

print(triangles)



