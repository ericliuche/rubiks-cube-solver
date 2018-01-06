from enum import Enum
from subprocess import check_output
import sys


class Move(Enum):
    B = 0
    R = 1
    F = 2
    L = 3
    BP = 4
    RP = 5
    FP = 6
    LP = 7
    BD = 8
    RD = 9
    FD = 10
    LD = 11

    BF = 12
    BPF = 13
    BFP = 14
    BPFP = 15
    BDF = 16
    BFD = 17
    BDFD = 18
    BPFD = 19
    BDFP = 20

    RL = 21
    RPL = 22
    RLP = 23
    RPLP = 24
    RDL = 25
    RLD = 26
    RDLD = 27
    RPLD = 28
    RDLP = 29

    RY = 30
    RDY = 31
    LPY = 32
    LDY = 33

    BPX = 34
    BDX = 35
    FX = 36
    FDX = 37

    BPFX = 38
    BDFX = 39
    BDFDX = 40
    BPFDX = 41
    RLPY = 42
    RLDY = 43
    RDLDY = 44
    RDLPY = 45

    X = 46
    Y = 47

UP    = frozenset(['U', 'U\'', 'U2'])
DOWN  = frozenset(['D', 'D\'', 'D2'])
FRONT = frozenset(['F', 'F\'', 'F2'])
BACK  = frozenset(['B', 'B\'', 'B2'])
RIGHT = frozenset(['R', 'R\'', 'R2'])
LEFT  = frozenset(['L', 'L\'', 'L2'])

MIRROR_SET = frozenset([frozenset(['B'  , 'F']),
                        frozenset(['B\'', 'F\'']),
                        frozenset(['R'  , 'L']),
                        frozenset(['R\'', 'L\'']),
                        frozenset(['R2' , 'L']),
                        frozenset(['R\'', 'L2']),
                        frozenset(['B2' , 'F\'']),
                        frozenset(['B'  , 'F2'])])

BUILD_MOVE = {frozenset(['B'  , 'F'])  : Move.BF,
              frozenset(['B'  , 'F\'']): Move.BFP,
              frozenset(['B'  , 'F2']) : Move.BFD,
              frozenset(['B\'', 'F'])  : Move.BPF,
              frozenset(['B\'', 'F\'']): Move.BPFP,
              frozenset(['B\'', 'F2']) : Move.BPFD,
              frozenset(['B2' , 'F'])  : Move.BDF,
              frozenset(['B2' , 'F\'']): Move.BDFP,
              frozenset(['B2' , 'F2']) : Move.BDFD,
              frozenset(['R'  , 'L'])  : Move.RL,
              frozenset(['R'  , 'L\'']): Move.RLP,
              frozenset(['R'  , 'L2']) : Move.RLD,
              frozenset(['R\'', 'L'])  : Move.RPL,
              frozenset(['R\'', 'L\'']): Move.RPLP,
              frozenset(['R\'', 'L2']) : Move.RPLD,
              frozenset(['R2' , 'L'])  : Move.RDL,
              frozenset(['R2' , 'L\'']): Move.RDLP,
              frozenset(['R2' , 'L2']) : Move.RDLD,
              'B'  : Move.B,
              'B\'': Move.BP,
              'B2' : Move.BD,
              'F'  : Move.F,
              'F\'': Move.FP,
              'F2' : Move.FD,
              'R'  : Move.R,
              'R\'': Move.RP,
              'R2' : Move.RD,
              'L'  : Move.L,
              'L\'': Move.LP,
              'L2' : Move.LD, }

BUILD_MOVE_WITH_ROTATION = {frozenset(['B\'', 'F'])  : Move.BPFX,
                            frozenset(['B\'', 'F2']) : Move.BPFDX,
                            frozenset(['B2' , 'F'])  : Move.BDFX,
                            frozenset(['B2' , 'F2']) : Move.BDFDX,
                            frozenset(['R'  , 'L\'']): Move.RLPY,
                            frozenset(['R'  , 'L2']) : Move.RLDY,
                            frozenset(['R2' , 'L\'']): Move.RDLPY,
                            frozenset(['R2' , 'L2']) : Move.RDLDY,
                            'B\'': Move.BPX,
                            'B2' : Move.BDX,
                            'F'  : Move.FX,
                            'F2' : Move.FDX,
                            'R'  : Move.RY,
                            'R2' : Move.RDY,
                            'L\'': Move.LPY,
                            'L2' : Move.LDY, }

OPPOSITE = {'F'  : BACK,
            'F\'': BACK,
            'F2' : BACK,
            'B'  : FRONT,
            'B\'': FRONT,
            'B2' : FRONT,
            'R'  : LEFT,
            'R\'': LEFT,
            'R2' : LEFT,
            'L'  : RIGHT,
            'L\'': RIGHT,
            'L2' : RIGHT,
            'D'  : UP,
            'D\'': UP,
            'D2' : UP,
            'U'  : DOWN,
            'U\'': DOWN,
            'U2' : DOWN, }

ROTATE_X = {'U'  : 'B',
            'U\'': 'B\'',
            'U2' : 'B2',
            'B'  : 'D',
            'B\'': 'D\'',
            'B2' : 'D2',
            'D'  : 'F',
            'D\'': 'F\'',
            'D2' : 'F2',
            'F'  : 'U',
            'F\'': 'U\'',
            'F2' : 'U2', }

ROTATE_Y = {'U'  : 'R',
            'U\'': 'R\'',
            'U2' : 'R2',
            'R'  : 'D',
            'R\'': 'D\'',
            'R2' : 'D2',
            'D'  : 'L',
            'D\'': 'L\'',
            'D2' : 'L2',
            'L'  : 'U',
            'L\'': 'U\'',
            'L2' : 'U2', }

"""
             |************|
             |*U1**U2**U3*|
             |************|
             |*U4**U5**U6*|
             |************|
             |*U7**U8**U9*|
             |************|
 ************|************|************|************
 *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
 ************|************|************|************
 *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
 ************|************|************|************
 *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
 ************|************|************|************
             |************|
             |*D1**D2**D3*|
             |************|
             |*D4**D5**D6*|
             |************|
             |*D7**D8**D9*|
             |************|


             |************|
             |*B9**B8**B7*|
             |************|
             |*B6**B5**B4*|
             |************|
             |*B3**B2**B1*|
             |************|
 ************|************|************|************
 *L7**L4**L1*|*U1**U2**U3*|*R3**R6**R9*|*U7**U8**U8*
 ************|************|************|************
 *L8**L5**L2*|*U4**U5**U6*|*R2**R5**R8*|*U4**U5**U6*
 ************|************|************|************
 *L9**L6**L3*|*U7**U8**U9*|*R1**R4**R7*|*U1**U2**U3*
 ************|************|************|************
             |************|
             |*F1**F2**F3*|
             |************|
             |*F4**F5**F6*|
             |************|
             |*F7**F8**F9*|
             |************|

X, X, X, Y, Y, Y

D -> B
U -> F
F -> R
B -> L
L -> D
R -> U

UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB



"""


def is_normal(move):
    return move in set(['F', 'B', 'R', 'L'])


def build_move(first_move, second_move=None, rotate=False):
    move = frozenset([first_move, second_move]) if second_move else first_move
    return BUILD_MOVE_WITH_ROTATION[move] if rotate else BUILD_MOVE[move]


def is_opposite(move, other_move):
    return move in OPPOSITE[other_move]


def is_mirror(move, other_move):
    return frozenset([move, other_move]) in MIRROR_SET


def rotate_move_x(move):
    return ROTATE_X[move] if move in ROTATE_X else move


def rotate_move_y(move):
    return ROTATE_Y[move] if move in ROTATE_Y else move


def rotate_moves(moves, i, x):
    for j in range(i, len(moves)):
        if x:
            moves[j] = rotate_move_x(moves[j])
        else:
            moves[j] = rotate_move_y(moves[j])


def convert_moves(moves):
    converted_moves = []
    i = 0
    while i < len(moves):
        if moves[i] in UP | DOWN:
            converted_moves.append(Move.X)
            rotate_moves(moves, i, True)
            continue
        elif i == len(moves)-1:
            converted_moves.append(build_move(moves[i]))
        elif moves[i] in set(['B', 'L', 'R\'', 'F\'']):
            if is_opposite(moves[i], moves[i+1]):
                converted_moves.append(build_move(moves[i], moves[i+1]))
                i += 1
            else:
                converted_moves.append(build_move(moves[i]))
        else:
            if is_opposite(moves[i], moves[i+1]):
                if is_mirror(moves[i], moves[i+1]) or i == len(moves)-2:
                    converted_moves.append(build_move(moves[i], moves[i+1]))
                else:
                    converted_moves.append(build_move(
                        moves[i], moves[i+1], rotate=moves[i+2] in UP | DOWN))
                    if moves[i+2] in UP | DOWN:
                        rotate_moves(moves, i+2, moves[i] in BACK | FRONT)
                i += 1
            else:
                converted_moves.append(
                    build_move(moves[i], rotate=moves[i+1] in UP | DOWN))
                if moves[i+1] in UP | DOWN:
                    rotate_moves(moves, i+1, moves[i] in BACK | FRONT)
        i += 1
    return converted_moves

if __name__ == '__main__':
    moves = check_output(['./solve', sys.argv[1]]).split()
    print ' '.join(moves)
    converted_moves = convert_moves(moves)
    print '{' + ', '.join([str(o.value) for o in converted_moves]) + '}'
    print ' '.join([o.name for o in converted_moves])
