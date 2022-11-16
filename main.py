win_x = 0
grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
used_numbers = []
score_x = 0
score_o = 0

def tah_x():
    while True:
        tah_x = int(input("Hráč 1 (x) : "))
        if tah_x in used_numbers:
            print("Toto pole je již plné.")
            continue
        else:
            used_numbers.append(tah_x)
            grid[tah_x] = "x"
            break


def tah_O():
    while True:
        tah_O = int(input("Hráč 2 (O) : "))
        if tah_O in used_numbers:
            print("Toto pole je již plné.")
            continue
        else:
            used_numbers.append(tah_O)
            grid[tah_O] = "O"
            break


def print_grid():
    print(grid[7], grid[8], grid[9])
    print(grid[4], grid[5], grid[6])
    print(grid[1], grid[2], grid[3])


def did_win_x():
    if grid[7] == "x" and grid[8] == "x" and grid[9] == "x":
        print("Hráč 1 vyhrává.")
        win_x = 1
    elif grid[4] == "x" and grid[5] == "x" and grid[6] == "x":
        print("Hráč 1 vyhrává.")
        win_x = 1
    elif grid[1] == "x" and grid[2] == "x" and grid[3] == "x":
        print("Hráč 1 vyhrává.")
        win_x = 1
    elif grid[7] == "x" and grid[4] == "x" and grid[1] == "x":
        print("Hráč 1 vyhrává.")
        win_x = 1
    elif grid[8] == "x" and grid[5] == "x" and grid[2] == "x":
        print("Hráč 1 vyhrává.")
        win_x = 1
    elif grid[9] == "x" and grid[6] == "x" and grid[3] == "x":
        print("Hráč 1 vyhrává.")
        win_x = 1
    elif grid[1] == "x" and grid[5] == "x" and grid[9] == "x":
        print("Hráč 1 vyhrává.")
        win_x = 1
    elif grid[3] == "x" and grid[5] == "x" and grid[7] == "x":
        print("Hráč 1 vyhrává.")
        win_x = 1
    else:
        win_x = 0

    return win_x


def did_win_o():
    if grid[7] == "O" and grid[8] == "O" and grid[9] == "O":
        print("Hráč 2 vyhrává.")
        win_O = 1
    elif grid[4] == "O" and grid[5] == "O" and grid[6] == "O":
        print("Hráč 2 vyhrává.")
        win_O = 1
    elif grid[1] == "O" and grid[2] == "O" and grid[3] == "O":
        print("Hráč 2 vyhrává.")
        win_O = 1
    elif grid[7] == "O" and grid[4] == "O" and grid[1] == "O":
        print("Hráč 2 vyhrává.")
        win_O = 1
    elif grid[8] == "O" and grid[5] == "O" and grid[2] == "O":
        print("Hráč 2 vyhrává.")
        win_O = 1
    elif grid[9] == "O" and grid[6] == "O" and grid[3] == "O":
        print("Hráč 2 vyhrává.")
        win_O = 1
    elif grid[1] == "O" and grid[5] == "O" and grid[9] == "O":
        print("Hráč 2 vyhrává.")
        win_O = 1
    elif grid[3] == "O" and grid[5] == "O" and grid[7] == "O":
        print("Hráč 2 vyhrává.")
        win_O = 1
    else:
        win_O = 0

    return win_O

# Start Hry
while True:
    while True:
        grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        used_numbers = []
        print('7 8 9\n4 5 6\n1 2 3\n')
        print_grid()
        tah_x()
        print_grid()
        tah_O()
        print_grid()
        tah_x()
        print_grid()
        tah_O()
        print_grid()
        tah_x()
        print_grid()
        win_1 = did_win_x()
        if win_1 == 1:
            score_x += 1
            break
        tah_O()
        print_grid()
        win_2 = did_win_o()
        if win_2 == 1:
            score_o += 1
            break
        tah_x()
        print_grid()
        win_1 = did_win_x()
        if win_1 == 1:
            score_x += 1
            break
        tah_O()
        print_grid()
        win_2 = did_win_o()
        if win_2 == 1:
            score_o += 1
            break
        tah_x()
        print_grid()
        win_1 = did_win_x()
        if win_1 == 1:
            score_x += 1
            break

    is_continue = input("Chcete chrát znovu? (ano/ne) : ")
    if is_continue != "ano":
        break

print("\nSkóre X = ", score_x, "\nSkóre O = ", score_o)
