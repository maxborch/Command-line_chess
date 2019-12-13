# dictionary of pieces with their chr representation
EMPTY = "--"
p = {"BK": chr(9818), "BQ": chr(9819), "BC": chr(9820), "BB": chr(9821), "BH": chr(9822), "BP": chr(9823),
     "WK": chr(9812), "WQ": chr(9813), "WC": chr(9814), "WB": chr(9815), "WH": chr(9816), "WP": chr(9817), EMPTY: " "}
letter_repr_dict = {"A": "0", "B": "1", "C": "2", "D": "3", "E": "4", "F": "5", "G": "6", "H": "7"}
numb_repr_dict = {"8": "0", "7": "1", "6": "2", "5": "3", "4": "4", "3": "5", "2": "6", "1": "7"}

distance = 0
direction = 0

# white makes the first move in the game
global last_move
last_move = "B"

# defines the lists making up the board
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
list_1 = ["BC", "BH", "BB", "BQ", "BK", "BB", "BH", "BC"]
list_2 = ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"]
list_3 = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
list_4 = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
list_5 = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
list_6 = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
list_7 = ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"]
list_8 = ["WC", "WH", "WB", "WQ", "WK", "WB", "WH", "WC"]
numb = ["1", "2", "3", "4", "5", "6", "7", "8"]
board = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8]

print("-----------------------------------")
print("            White starts!          ")
print("-----------------------------------")


# detects direction
def input_tester(codeinput1, codeinput2):
    h_movement = int(codeinput2[0]) - int(codeinput1[0])  # determines move on horizontal axis
    v_movement = int(codeinput2[1]) - int(codeinput1[1])  # determines move on vertical axis

    global distance
    global direction
    global error_check_input_tester

    if h_movement == 0:
        if v_movement == 0:
            # print("invalid move as same position")
            distance = 0
            direction = "INVALID"
            error_check_input_tester = 1
        elif v_movement > 0:
            distance = abs(v_movement)
            direction = "S"
        elif v_movement < 0:
            distance = abs(v_movement)
            direction = "N"

    elif v_movement == 0:
        if h_movement > 0:
            distance = abs(h_movement)
            direction = "E"
        elif h_movement < 0:
            distance = abs(h_movement)
            direction = "W"

    elif h_movement < 0:
        if v_movement < 0 and abs(h_movement) == abs(v_movement):
            distance = abs(v_movement)
            direction = "NW"
        elif v_movement > 0 and abs(h_movement) == abs(v_movement):
            distance = abs(v_movement)
            direction = "SW"
        else:  # if abs h_move != abs v_move (e.g. l-shaped move)
            distance = 0
            direction = "INVALID DIRECTION"
            error_check_input_tester = 1

    elif h_movement > 0:
        if v_movement < 0 and abs(h_movement) == abs(v_movement):
            distance = abs(v_movement)
            direction = "NE"
        elif v_movement > 0 and abs(h_movement) == abs(v_movement):
            distance = abs(v_movement)
            direction = "SE"
        else:
            distance = 0
            direction = "INVALID DIRECTION"
            error_check_input_tester = 1


#
def range_tester(direct, dist, inpt1):
    global error_check_range_tester

    if direct == "S":
        if error_check_range_tester == 0 and dist > 1:
            for i in range(1, dist):  # tests whether another piece is in the way
                temp_field = inpt1[0] + str(int(inpt1[1]) + 1)
                if board[int(temp_field[1])][int(temp_field[0])] != EMPTY:
                    error_check_range_tester = 1

    elif direct == "SE":
        if error_check_range_tester == 0 and dist > 1:
            for i in range(0, dist):
                temp_field = str(int(inpt1[0]) + 1) + str(int(inpt1[1]) + 1)
                if board[int(temp_field[1])][int(temp_field[0])] != EMPTY:
                    error_check_range_tester = 1

    elif direct == "E":
        if error_check_range_tester == 0 and dist > 1:
            for i in range(0, dist):
                temp_field = str(int(inpt1[0]) + 1) + inpt1[1]
                if board[int(temp_field[1])][int(temp_field[0])] != EMPTY:
                    error_check_range_tester = 1

    elif direct == "NE":
        if error_check_range_tester == 0 and dist > 1:
            for i in range(0, dist):
                temp_field = str(int(inpt1[0]) + 1) + str(int(inpt1[1]) - 1)
                if board[int(temp_field[1])][int(temp_field[0])] != EMPTY:
                    error_check_range_tester = 1

    elif direct == "N":
        if error_check_range_tester == 0 and dist > 1:
            for i in range(0, dist):
                temp_field = inpt1[0] + str(int(inpt1[1]) - 1)
                if board[int(temp_field[1])][int(temp_field[0])] != EMPTY:
                    error_check_range_tester = 1

    elif direct == "NW":
        if error_check_range_tester == 0 and dist > 1:
            for i in range(0, dist):
                temp_field = str(int(inpt1[0]) - 1) + str(int(inpt1[1]) - 1)
                if board[int(temp_field[1])][int(temp_field[0])] != EMPTY:
                    error_check_range_tester = 1

    elif direct == "W":
        if error_check_range_tester == 0:
            for i in range(0, dist):
                temp_field = str(int(inpt1[0]) - 1) + inpt1[1]
                if board[int(temp_field[1])][int(temp_field[0])] != EMPTY:
                    error_check_range_tester = 1

    elif direct == "SW":
        if error_check_range_tester == 0:
            for i in range(0, dist):
                temp_field = str(int(inpt1[0]) - 1) + str(int(inpt1[1]) + 1)
                if board[int(temp_field[1])][int(temp_field[0])] != EMPTY:
                    error_check_range_tester = 1


# test is move is valid for selected piece
def is_move_valid_test(codeinput1, codeinput2, direct):
    global error_check_move_valid
    global valid_moves
    temp_piece = board[int(codeinput1[1])][int(codeinput1[0])]
    temp = board[int(codeinput2[1])][int(codeinput2[0])]

    if temp_piece[1] == "K":
        valid_moves = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        if distance == 1 and direct in valid_moves:
            pass
        else:
            error_check_move_valid = 1

    elif temp_piece[1] == "Q":
        valid_moves = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        if distance <= 7 and direct in valid_moves:
            pass
        else:
            error_check_move_valid = 1

    elif temp_piece[1] == "C":
        valid_moves = ["N", "E", "S", "W"]
        if distance <= 7 and direct in valid_moves:
            pass
        else:
            error_check_move_valid = 1

    elif temp_piece[1] == "B":
        valid_moves = ["NE", "SE", "SW", "NW"]
        if distance <= 7 and direct in valid_moves:
            pass
        else:
            error_check_move_valid = 1

    elif temp_piece[1] == "H":  # program it extra

        knight1 = str(int(codeinput1[0]) - 1) + str(int(codeinput1[1]) + 2)
        knight2 = str(int(codeinput1[0]) + 1) + str(int(codeinput1[1]) + 2)
        knight3 = str(int(codeinput1[0]) + 1) + str(int(codeinput1[1]) - 2)
        knight4 = str(int(codeinput1[0]) - 1) + str(int(codeinput1[1]) - 2)
        knight5 = str(int(codeinput1[0]) - 2) + str(int(codeinput1[1]) + 1)
        knight6 = str(int(codeinput1[0]) + 2) + str(int(codeinput1[1]) + 1)
        knight7 = str(int(codeinput1[0]) + 2) + str(int(codeinput1[1]) - 1)
        knight8 = str(int(codeinput1[0]) - 2) + str(int(codeinput1[1]) - 1)

        temp_field_list = [knight1, knight2, knight3, knight4, knight5, knight6, knight7, knight8]

        if code_input2 not in temp_field_list:
            error_check_move_valid = 1

    elif temp_piece[1] == "P" and temp_piece[0] == "W":  # if white pawn
        valid_moves = []
        if temp == "--":
            valid_moves.append("N")
        elif temp[0] == "B":
            valid_moves.append("NE")
            valid_moves.append("NW")
        if distance == 1 and direct in valid_moves:
            pass
        else:
            error_check_move_valid = 1

    elif temp_piece[1] == "P" and temp_piece[0] == "B":  # if black pawn
        valid_moves = []
        if temp == "--":  # pawn can only go straight if field is empty
            valid_moves.append("S")
        elif temp[0] == "W":  # pawn can only go diagonal if field is occupied by opponent
            valid_moves.append("SW")
            valid_moves.append("SE")
        if distance == 1 and direct in valid_moves:
            pass
        else:
            error_check_move_valid = 1
    else:
        valid_moves = []
        error_check_move_valid = 1


# check if destination is valid (i.e. if it is empty of occupied by opponent)
def destination_check():
    global error_check_destination
    global right_turn_check
    global last_move

    # checks whether right colour is chosen and whether destination cell is empty or occupied by opposite colour
    temp_1 = board[int(code_input1[1])][int(code_input1[0])]
    temp_2 = board[int(code_input2[1])][int(code_input2[0])]

    # tests whether one tries to catch the same colour
    if temp_1[0] == temp_2[0]:
        error_check_destination = 1
    else:
        pass

    if error_check_input_tester + error_check_range_tester + error_check_move_valid + error_check_destination + right_turn_check == 0:
        if temp_1[0] != last_move:
            last_move = temp_1[0]
            right_turn_check = 0

        elif temp_1[0] == last_move:
            right_turn_check = 1
            print("Invalid move. Make a move with other colour!")
    elif error_check_range_tester + error_check_move_valid + error_check_destination + right_turn_check == 0:
        if temp_1[0] != last_move:
            last_move = temp_1[0]
            right_turn_check = 0

        elif temp_1[0] == last_move:
            right_turn_check = 1
            print("Invalid move. Make a move with other colour!")


# print board
def print_board():
    a = 8
    for i in board:
        print(a, "|", p[i[0]], "|", p[i[1]], "|", p[i[2]], "|", p[i[3]], "|", p[i[4]], "|", p[i[5]], "|", p[i[6]], "|",
              p[i[7]], "|")
        print("  " + "-----------" * 3)
        a -= 1
    print("   ", "A", " ", "B", " ", "C", " ", "D", " ", "E", " ", "F", " ", "G", " ", "H")


# Checks if somebody has won the game (i.e. if one of the Kings has been catched)
def win_check():
    if "BK" not in board_consol:
        print("----------------------------------------------------")
        print("Victory!!!! White has won the game. Congratulations!")
        print("----------------------------------------------------")
    elif "WK" not in board_consol:
        print("----------------------------------------------------")
        print("Victory!!!! Black has won the game. Congratulations!")
        print("----------------------------------------------------")


print_board()
board_consol = ['BC', 'BH', 'BB', 'BQ', 'BK', 'BP', 'WP', 'WC', 'WH', 'WB', 'WQ', 'WK']

# Loop (MAIN)
while 'WK' in board_consol and 'BK' in board_consol:

    # resets error checks after every loop
    error_check_input_tester = 0
    error_check_range_tester = 0
    error_check_move_valid = 0
    error_check_destination = 0
    right_turn_check = 0
    horizontal = ["A", "B", "C", "D", "E", "F", "G", "H"]
    vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]

    # input 1 (which piece to move)
    raw_input1 = input("Please enter the position of the piece that you want to move: ")
    input1 = raw_input1.upper()

    if len(input1) != 2:
        if input1 == "HELP":
            print("--------------------------------------------")
            print("For more details on Chess rules click here: ")
            print("https://en.wikipedia.org/wiki/Chess")
            print("--------------------------------------------")
            continue
        else:
            print("Invalid Input! Try Again")
            continue
    elif input1[0] not in horizontal or input1[1] not in vertical:
        print("Please enter a valid field!")
        continue

    # input 2 (destination of move)
    raw_input2 = input("Please enter the position where you want to move the selected piece: ")
    input2 = raw_input2.upper()
    if len(input2) != 2:
        if input2 == "HELP":
            print("--------------------------------------------")
            print("For more details on Chess rules click here: ")
            print("https://en.wikipedia.org/wiki/Chess")
            print("--------------------------------------------")
            continue
        else:
            print("Invalid Input! Try Again")
            continue
    elif input2[0] not in horizontal or input2[1] not in vertical:
        print("Please enter a valid field!")
        continue
    # translates input field into numeric field (e.g. A=0/1=0)
    code_input1 = letter_repr_dict[input1[0]] + numb_repr_dict[input1[1]]
    code_input2 = letter_repr_dict[input2[0]] + numb_repr_dict[input2[1]]

    temp1 = board[int(code_input1[1])][int(code_input1[0])]

    input_tester(code_input1, code_input2)  # 1
    range_tester(direction, distance, code_input1)  # 2
    is_move_valid_test(code_input1, code_input2, direction)  # 3
    destination_check()  # 4

    # if no error was found: make move
    normal_characters = ["K", "Q", "B", "C", "P"]
    # for all except Knight
    if temp1[1] in normal_characters:
        if error_check_input_tester + error_check_range_tester + error_check_move_valid + error_check_destination + right_turn_check == 0:
            board[int(code_input2[1])][int(code_input2[0])] = board[int(code_input1[1])][int(code_input1[0])]
            board[int(code_input1[1])][int(code_input1[0])] = EMPTY
            print_board()
    # for Knight
    elif temp1[1] == "H":
        if error_check_range_tester + error_check_move_valid + error_check_destination + right_turn_check == 0:
            board[int(code_input2[1])][int(code_input2[0])] = board[int(code_input1[1])][int(code_input1[0])]
            board[int(code_input1[1])][int(code_input1[0])] = EMPTY
            print_board()

    else:
        print("Invalid Move! Try again!")
        continue

    if error_check_range_tester == 1:
        print("--------------------------------------------")
        print("Move cannot be made!")
        print("--------------------------------------------")
    if error_check_move_valid == 1:
        print("--------------------------------------------")
        print("Move is not valid for selected character!")
        print("--------------------------------------------")
    if error_check_destination == 1:
        print("--------------------------------------------")
        print("You cannot move that piece to the selected destination")
        print("--------------------------------------------")
    if right_turn_check == 1:
        print("--------------------------------------------")
        print("It is not your turn! Make a move with other colour")
        print("--------------------------------------------")

    board_consol = []  # checks whether Kings are still on the board --> win check
    for i in board:
        for l in i:
            if l != "--" and l not in board_consol:
                board_consol.append(l)

    win_check()

