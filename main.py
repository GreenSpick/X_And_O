def Draw():
    global field
    print("-------------")
    for i in range(3):
        print("|", field[i][0], "|", field[i][1], "|", field[i][2], "|")
        print("-------------")

def Restart():
    global field, compare_field, round
    compare_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    round = 0
    print("game restarting")
    Draw()

def Compare(a):
    global field, compare_field
    for i in range(8):
        if (field[int(compare_field[i][0] // 3.1)][(compare_field[i][0] % 3)-1] == field[int(compare_field[i][1] // 3.1)][(compare_field[i][1] % 3)-1] == field[int(compare_field[i][2] // 3.1)][(compare_field[i][2] % 3)-1]):
            print("\nWin " + a)
            Restart()


def Turn(b, c):
    while True:
        global round
        a = input(c)
        if (field[int(int(a) // 3.1)][(int(a) % 3)-1]) != ("X" or "O"):
            field[int(int(a) // 3.1)][(int(a) % 3)-1] = b
            round += 1
        else:
            print("\n" * 3, "You can't go there")
            Draw()
            continue
        Draw()
        break

compare_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
round = 0
Draw()

while True:
    if round >=8:
        Restart()
    Turn("X", "\nPut X : ")
    Compare("X")
    Turn("O", "\nPut O : ")
    Compare("O")