import sys, argparse

# Graverage interpreter in python: core module
def graverage(points, bags, instructions, execdepth):
    if points == -1:
        print("ERROR, divition by 0, value %d" % bags)

    for instruction in instructions*execdepth:

        bag = bags[instruction]
        newx, newy = (0, 0)

        for point in bag:
            newx += points[point][0]
            newy += points[point][1]

        newx /= len(bag)
        newy /= len(bag)

        points[instruction] = (newx, newy)

    return points

def parseGraverageString(string): # Takes a string in standard graverage form, and returns the 3 objects needed for execition
    intlist = string.split(" ")

    intlist = intlist[::-1]

    for _ in range(0, len(intlist)):
        intlist[_] = int(intlist[_])

    N = intlist.pop()

    pts = {}
    bgs = {}
    ins = []

    for i in range(N):
        xtop = intlist.pop()
        xbot = intlist.pop()
        ytop = intlist.pop()
        ybot = intlist.pop()
        try:
            pts[i+1] = (xtop/xbot, ytop/ybot)
        except:
            return (-1, i, -1)

        M = intlist.pop()
        thisbag = []
        for j in range(M):
            bEle = intlist.pop()
            thisbag.append(bEle)
        
        bgs[i+1] = thisbag

    ins = intlist[::-1]

    return (pts, bgs, ins)

ap = argparse.ArgumentParser()

ap.add_argument("-f", "--file-name", required=True, help="File name to be opend")
ap.add_argument("-e", "--exec-depth", required=False, help="execution depth of program", default=1)

args = vars(ap.parse_args())

filename = args["file_name"]
execdepth = int(args["exec_depth"])

with open(filename, "r") as file:
    txt = file.readlines()

cleaned = txt[0].rstrip("\n")

prog = parseGraverageString(cleaned)
print("Processed machine state: " + str(prog))
print("Output: ", end='')
print(graverage(prog[0], prog[1], prog[2], execdepth))