from itertools import product

init_cube = {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "H": "H", "I": "I",
             "J": "J", "K": "K", "L": "L", "M": "M", "N": "N", "O": "O", "P": "P", "Q": "Q", "R": "R",
             "S": "S", "T": "T", "U": "U", "V": "V", "W": "W", "X": "X"}


def check_green_front_eo(cube):
    valid_spots = ["A", "B", "C", "D", "U", "V", "W", "X", "J", "L", "R", "T"]
    for spot in valid_spots:
        if cube[spot] not in valid_spots:
            return False
    return True

def check_red_front_eo(cube):
    valid_spots = ["A", "B", "C", "D", "U", "V", "W", "X", "F", "H", "N", "P"]
    for spot in valid_spots:
        if cube[spot] not in valid_spots:
            return False
    return True

def check_yellow_front_eo(cube):
    valid_spots = ["I", "J", "K", "L", "Q", "R", "S", "T", "B", "D", "V", "X"]
    for spot in valid_spots:
        if cube[spot] not in valid_spots:
            return False
    return True

def r(cube):
    # letters affected: B, T, V, J, M, N, O, P
    curr_j = cube["J"]
    cube["J"] = cube["V"]
    cube["V"] = cube["T"]
    cube["T"] = cube["B"]
    cube["B"] = curr_j
    curr_m = cube["M"]
    cube["M"] = cube["P"]
    cube["P"] = cube["O"]
    cube["O"] = cube["N"]
    cube["N"] = curr_m
    return cube

def l(cube):
    # letters affected: D, L, X, R, E, F, G, H
    curr_d = cube["D"]
    cube["D"] = cube["R"]
    cube["R"] = cube["X"]
    cube["X"] = cube["L"]
    cube["L"] = curr_d
    curr_e = cube["E"]
    cube["E"] = cube["H"]
    cube["H"] = cube["G"]
    cube["G"] = cube["F"]
    cube["F"] = curr_e
    return cube

def u(cube):
    # letters affected: E, Q, M, I, A, B, C, D
    curr_e = cube["E"]
    cube["E"] = cube["I"]
    cube["I"] = cube["M"]
    cube["M"] = cube["Q"]
    cube["Q"] = curr_e
    curr_a = cube["A"]
    cube["A"] = cube["D"]
    cube["D"] = cube["C"]
    cube["C"] = cube["B"]
    cube["B"] = curr_a
    return cube

def d(cube):
    # letters affected: G, K, O, S, U, V, W, X
    curr_g = cube["G"]
    cube["G"] = cube["S"]
    cube["S"] = cube["O"]
    cube["O"] = cube["K"]
    cube["K"] = curr_g
    curr_u = cube["U"]
    cube["U"] = cube["X"]
    cube["X"] = cube["W"]
    cube["W"] = cube["V"]
    cube["V"] = curr_u
    return cube

def f(cube):
    # letters affected: C, P, U, F, I, J, K, L
    curr_c = cube["C"]
    cube["C"] = cube["F"]
    cube["F"] = cube["U"]
    cube["U"] = cube["P"]
    cube["P"] = curr_c
    curr_i = cube["I"]
    cube["I"] = cube["L"]
    cube["L"] = cube["K"]
    cube["K"] = cube["J"]
    cube["J"] = curr_i
    return cube

def b(cube):
    # letters affected: A, H, W, N, Q, R, S, T
    curr_a = cube["A"]
    cube["A"] = cube["N"]
    cube["N"] = cube["W"]
    cube["W"] = cube["H"]
    cube["H"] = curr_a
    curr_q = cube["Q"]
    cube["Q"] = cube["T"]
    cube["T"] = cube["S"]
    cube["S"] = cube["R"]
    cube["R"] = curr_q
    return cube


def generate_sequences(array, k):
    sequences = [''.join(seq) for seq in product(array, repeat=k)]
    return sequences

def move_cube(move, cube):
    if move == "R":
        r(cube)
    elif move == "L":
        l(cube)
    elif move == "U":
        u(cube)
    elif move == "D":
        d(cube)
    elif move == "F":
        f(cube)
    elif move == "B":
        b(cube)
    elif move == "R2":
        r(cube)
        r(cube)
    elif move == "L2":
        l(cube)
        l(cube)
    elif move == "U2":
        u(cube)
        u(cube)
    elif move == "D2":
        d(cube)
        d(cube)
    elif move == "F2":
        f(cube)
        f(cube)
    elif move == "B2":
        b(cube)
        b(cube)
    elif move == "R'":
        r(cube)
        r(cube)
        r(cube)
    elif move == "L'":
        l(cube)
        l(cube)
        l(cube)
    elif move == "U'":
        u(cube)
        u(cube)
        u(cube)
    elif move == "D'":
        d(cube)
        d(cube)
        d(cube)
    elif move == "F'":
        f(cube)
        f(cube)
        f(cube)
    elif move == "B'":
        b(cube)
        b(cube)
        b(cube)
    else:
        print("Invalid move")
        print(move)
        exit()
    return cube

def get_scramble():
    scramble = input("Enter scramble: ").split(" ")
    return scramble

def get_eo_depth():
    depth = int(input("Enter EO depth: "))
    return depth

def cancondense(sequence):
    # check if three consecutive elements of the array are the same type
    for i in range(len(sequence) - 2):
        curr_val = sequence[i][0]
        if curr_val == 'R' or curr_val == 'L':
            if (sequence[i+1][0] == 'R' or sequence[i+1][0] == 'L') and (sequence[i+2][0] == 'R' or sequence[i+2][0] == 'L'):
                return True
        if curr_val == 'F' or curr_val == 'B':
            if (sequence[i+1][0] == 'F' or sequence[i+1][0] == 'B') and (sequence[i+2][0] == 'F' or sequence[i+2][0] == 'B'):
                return True
        if curr_val == 'U' or curr_val == 'D':
            if (sequence[i+1][0] == 'U' or sequence[i+1][0] == 'D') and (sequence[i+2][0] == 'U' or sequence[i+2][0] == 'D'):
                return True
    return False

def move_sequences(eo_depth):
    # valid_moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]
    valid_moves = ['R ', "R' ", 'R2 ', 'L ', "L' ", 'L2 ', 'U ', "U' ", 'U2 ', 'D ', "D' ", 'D2 ', 'F ', "F' ", 'F2 ', 'B ', "B' ", 'B2 ']
    sequences = []
    x = generate_sequences(valid_moves, eo_depth)
    for seq in x:
        #print(seq)
        splitSeq = seq.split(" ")[:-1]
        sequences.append(splitSeq)
    return sequences





def get_eos(cube, scramble, eo_depth, sequences):
    counter = 0
    for move in scramble:
        cube = move_cube(move, cube)

    # go through every sequence in sequences, simulate on the cube, and check if eo is solved
    valid_eos = []
    for sequence in sequences:
        curr_cube = cube.copy()
        counter = 1
        stop_short = False
        for move in sequence:
            curr_cube = move_cube(move, curr_cube)
            if (check_green_front_eo(curr_cube) or check_red_front_eo(curr_cube) or check_yellow_front_eo(curr_cube)) and counter != eo_depth:
                # print(sequence)
                stop_short = True
            counter += 1
        if (check_green_front_eo(curr_cube) or check_red_front_eo(curr_cube) or check_yellow_front_eo(curr_cube)) and not cancondense(sequence) and not stop_short:
            valid_eos.append(sequence)
    # print(valid_eos)
    stringified_eos = []
    for sequence in valid_eos:
        stringified_eos.append(' '.join(sequence))


    condensed = []
    for sequence in stringified_eos:
        split_seq = sequence.split(" ")
        can_condense = False
        for i in range(len(split_seq)-1):
            if split_seq[i][0] == split_seq[i+1][0]:
                can_condense = True
        if not can_condense:
            condensed.append(sequence)

    # print every other element of condensed
    return condensed[::2]
    # for i in range(len(condensed)):
    #     if i % 2 == 0:
    #         print(condensed[i])

def get_inverse(scramble):
    # loop through scramble in backwards order
    inverse = []
    for move in reversed(scramble):
        if move[-1] == "'":
            inverse.append(move[:-1])
        elif move[-1] == "2":
            inverse.append(move)
        else:
            inverse.append(move + "'")
    return inverse

scramble = get_scramble()
eo_depth = get_eo_depth()
sequences = move_sequences(eo_depth)
inverse_scramble = get_inverse(scramble)


#scramble cube
cube = {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "H": "H", "I": "I", "J": "J", "K": "K", "L": "L", "M": "M", "N": "N", "O": "O", "P": "P", "Q": "Q", "R": "R", "S": "S", "T": "T", "U": "U", "V": "V", "W": "W", "X": "X"}
inv_cube = cube.copy()
eos = get_eos(cube, scramble, eo_depth, sequences)
inverse_eos = get_eos(inv_cube, inverse_scramble, eo_depth, sequences)
for i in eos:
    print(i)
for i in inverse_eos:
    print("(" + i + ")")

# TODO: 
# - check if second-to-last move is unnecessary. That is, if the second-to-last move is the opposite face as the last move AND is a double turn, then the second-to-last move is unnecessary
# - Improve detecting a condensed EO. For example, current version still returns something like L2 F B F --> can check if there is a sequence of 3 or more consecutive moves that are parallel faces