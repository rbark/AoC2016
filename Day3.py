trianglea = 0
nlines = 0

triangles = [[], [], []]



with open("day3.txt") as f:
    for line in f.readlines():
        nlines += 1
        sides = line.strip().split()
        sides[0] = int(sides[0].strip())
        sides[1] = int(sides[1].strip())
        sides[2] = int(sides[2].strip())

        sides = sorted(sides)
        if sides[2] < sides[0] + sides[1]:
            print('triangle h=' + str(sides[2]) + ' k1= ' + str(sides[0]) + ' k2= ' + str(sides[1]))
            trianglea += 1
            print(str(trianglea))
print(str(trianglea))


