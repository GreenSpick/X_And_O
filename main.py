def Draw():
    global field
    print("\n", field[0], "|", field[1], "|", field[2], "\n",  "---------", "\n", field[3], "|", field[4], "|", field[5], "\n", "---------", "\n", field[6], "|", field[7], "|", field[8])

def Restart():
    global field, p1, p2, p3, p4, p5, p6, p7, p8, p9, restart
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = "1", "2", "3", "4", "5", "6", "7", "8", "9"
    field = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    Draw()
    restart = True

def Compare(a):
    global field
    if ((a == field[0] and a == field[1] and a == field[2]) or (a == field[3] and a == field[4] and a == field[5]) or (a == field[6] and a == field[7] and a == field[8]) or (a == field[0] and a == field[3] and a == field[6]) or (a == field[1] and a == field[4] and a == field[7]) or (a == field[2] and a == field[5] and a == field[8]) or (a == field[0] and a == field[4] and a == field[8]) or (a == field[6] and a == field[4] and a == field[2])):
        Restart()
        print("\nWin " + a)

def Turn(b, c):
    while True:
        a = input(c)
        if field[int(a) - 1] != "X" and field[int(a) - 1] != "O":
            field[int(a) - 1] = b
        else:
            print("\n" * 3, "You can't go there")
            Draw()
            continue
        Draw()
        break

p1, p2, p3, p4, p5, p6, p7, p8, p9 = "1", "2", "3", "4", "5", "6", "7" ,"8" ,"9"
field = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
restart = False

while True:
    Draw()
    Turn("X", "\nPut X : ")
    Compare("X")
    if restart == True:
        restart = False
        continue
    Turn("O", "\nPut O : ")
    Compare("O")