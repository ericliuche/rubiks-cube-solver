from subprocess import check_output

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
hi = True
spinx = False
spiny = False
while hi:
    #result = raw_input()
    result = check_output(["./solve", "RDFLUDUUBUBLLRFRULFBLDFUFBURLFRDFRUBUDLFLFDBDDRBLBRDRB"])
                                       
    hi = False
    moves = result.split()
    count = 0
    output = []
    i = 0
    print moves
#    print result
    while i < len(moves):
        spinx = False
        spiny = False
        if (moves[i] == 'U'):
            output.append(X)
            spinx = True
            moves[i] = 'B'
            i = i-1
        elif (moves[i] == 'U\''):
            output.append(X)
            moves[i] = 'B\''
            spinx = True
            i = i-1
        elif (moves[i] == 'U2'):
            output.append(X)
            moves[i] = 'B2'
            spinx = True
            i = i-1
        elif (moves[i] == 'D'):
            output.append(X)
            moves[i] = 'F'
            spinx = True
            i = i-1
        elif (moves[i] == 'D\''):
            output.append(X)
            moves[i] = 'F\''
            spinx = True
            i = i-1
        elif (moves[i] == 'D2'):
            output.append(X)
            moves[i] = 'F2'
            spinx = True
            i = i-1
        elif (moves[i] == 'B'):
            if (i == len(moves)-1):
                output.append(B)
            elif (moves[i+1] == 'F'):
                output.append(BF)
                i = i+1
            elif (moves[i+1] == 'F\''):
                output.append(BFP)
                i = i+1
            elif (moves[i+1] == 'F2'):
                output.append(BFD)
                i = i+1
            else:
                output.append(B)
        elif (moves[i] == 'B\''):
            if (i == len(moves)-1):
                output.append(BP)
            elif (moves[i+1] == 'F'):
                if (i == len(moves)-2):
                    output.append(BPF)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(BPFX)
                    moves[i+2] = 'B'
                    spinx = True
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(BPFX)
                    moves[i+2] = 'B\''
                    spinx = True
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(BPFX)
                    moves[i+2] = 'B2'
                    spinx = True
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(BPFX)
                    moves[i+2] = 'F'
                    spinx = True
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(BPFX)
                    moves[i+2] = 'F\''
                    spinx = True
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(BPFX)
                    moves[i+2] = 'F2'
                    spinx = True
                    i = i+1
                else:
                    output.append(BPF)
                    i = i+1
            elif (moves[i+1] == 'F\''):
                output.append(BPFP)
                i = i+1
            elif (moves[i+1] == 'F2'):
                if (i == len(moves)-2):
                    output.append(BPFD)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(BPFDX)
                    moves[i+2] = 'B'
                    spinx = True
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(BPFDX)
                    moves[i+2] = 'B\''
                    spinx = True
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(BPFDX)
                    moves[i+2] = 'B2'
                    spinx = True
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(BPFDX)
                    moves[i+2] = 'F'
                    spinx = True
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(BPFDX)
                    moves[i+2] = 'F\''
                    spinx = True
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(BPFDX)
                    moves[i+2] = 'F2'
                    spinx = True
                    i = i+1
                else:
                    output.append(BPFD)
                    i = i+1
            elif (moves[i+1] == 'U'):
                output.append(BPX)
                spinx = True
                moves[i+1] = 'B'
            elif (moves[i+1] == 'U\''):
                output.append(BPX)
                spinx = True
                moves[i+1] = 'B\''
            elif (moves[i+1] == 'U2'):
                output.append(BPX)
                spinx = True
                moves[i+1] = 'B2'
            elif (moves[i+1] == 'D'):
                output.append(BPX)
                spinx = True
                moves[i+1] = 'F'
            elif (moves[i+1] == 'D\''):
                output.append(BPX)
                spinx = True
                moves[i+1] = 'F\''
            elif (moves[i+1] == 'D2'):
                output.append(BPX)
                spinx = True
                moves[i+1] = 'F2'
            else:
                output.append(BP)
        elif (moves[i] == 'B2'):
            if (i == len(moves)-1):
                output.append(BD)
            elif (moves[i+1] == 'F'):
                if (i == len(moves)-2):
                    output.append(BDF)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'B'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'B\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'B2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'F'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'F\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'F2'
                    i = i+1
                else:
                    output.append(BDF)
                    i = i+1
            elif (moves[i+1] == 'F\''):
                output.append(BDFP)
                i = i+1
            elif (moves[i+1] == 'F2'):
                if (i == len(moves)-2):
                    output.append(BDFD)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'B'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'B\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'B2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'F'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'F\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'F2'
                    i = i+1
                else:
                    output.append(BDFD)
                    i = i+1
            elif (moves[i+1] == 'U'):
                output.append(BDX)
                spinx = True
                moves[i+1] = 'B'
            elif (moves[i+1] == 'U\''):
                output.append(BDX)
                spinx = True
                moves[i+1] = 'B\''
            elif (moves[i+1] == 'U2'):
                output.append(BDX)
                spinx = True
                moves[i+1] = 'B2'
            elif (moves[i+1] == 'D'):
                output.append(BDX)
                spinx = True
                moves[i+1] = 'F'
            elif (moves[i+1] == 'D\''):
                output.append(BDX)
                spinx = True
                moves[i+1] = 'F\''
            elif (moves[i+1] == 'D2'):
                output.append(BDX)
                spinx = True
                moves[i+1] = 'F2'
            else:
                output.append(BD)
    ##-------------------------------------------

        elif (moves[i] == 'F'):
            if (i == len(moves)-1):
                output.append(F)
            elif (moves[i+1] == 'B'):
                output.append(BF)
                i = i+1
            elif (moves[i+1] == 'B\''):
                if (i == len(moves)-2):
                    output.append(BPF)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(BPFX)
                    spinx = True
                    moves[i+2] = 'B'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(BPFX)
                    spinx = True
                    moves[i+2] = 'B\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(BPFX)
                    spinx = True
                    moves[i+2] = 'B2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(BPFX)
                    spinx = True
                    moves[i+2] = 'F'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(BPFX)
                    spinx = True
                    moves[i+2] = 'F\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(BPFX)
                    spinx = True
                    moves[i+2] = 'F2'
                    i = i+1
                else:
                    output.append(BPF)
                    i = i+1
            elif (moves[i+1] == 'B2'):
                if (i == len(moves)-2):
                    output.append(BDF)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'B'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'B\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'B2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'F'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'F\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(BDFX)
                    spinx = True
                    moves[i+2] = 'F2'
                    i = i+1
                else:
                    output.append(BDF)
                    i = i+1
            elif (moves[i+1] == 'U'):
                output.append(FX)
                spinx = True
                moves[i+1] = 'B'
            elif (moves[i+1] == 'U\''):
                output.append(FX)
                spinx = True
                moves[i+1] = 'B\''
            elif (moves[i+1] == 'U2'):
                output.append(FX)
                spinx = True
                moves[i+1] = 'B2'
            elif (moves[i+1] == 'D'):
                output.append(FX)
                spinx = True
                moves[i+1] = 'F'
            elif (moves[i+1] == 'D\''):
                output.append(FX)
                spinx = True
                moves[i+1] = 'F\''
            elif (moves[i+1] == 'D2'):
                output.append(FX)
                spinx = True
                moves[i+1] = 'F2'
            else:
                output.append(F)
        elif (moves[i] == 'F\''):
            if (i == len(moves)-1):
                output.append(FP)
            elif (moves[i+1] == 'B'):
                output.append(BFP)
                i = i+1
            elif (moves[i+1] == 'B\''):
                output.append(BPFP)
                i = i+1
            elif (moves[i+1] == 'B2'):
                output.append(BDFP)
                i = i+1
            else:
                output.append(FP)
        elif (moves[i] == 'F2'):
            if (i == len(moves)-1):
                output.append(FD)
            elif (moves[i+1] == 'B'):
                output.append(BFD)
                i = i+1
            elif (moves[i+1] == 'B\''):
                if (i == len(moves)-2):
                    output.append(BPFD)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(BPFDX)
                    spinx = True
                    moves[i+2] = 'B'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(BPFDX)
                    spinx = True
                    moves[i+2] = 'B\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(BPFDX)
                    spinx = True
                    moves[i+2] = 'B2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(BPFDX)
                    spinx = True
                    moves[i+2] = 'F'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(BPFDX)
                    spinx = True
                    moves[i+2] = 'F\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(BPFDX)
                    spinx = True
                    moves[i+2] = 'F2'
                    i = i+1
                else:
                    output.append(BPFD)
                    i = i+1
            elif (moves[i+1] == 'B2'):
                if (i == len(moves)-2):
                    output.append(BDFD)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'B'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'B\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'B2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'F'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'F\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(BDFDX)
                    spinx = True
                    moves[i+2] = 'F2'
                    i = i+1
                else:
                    output.append(BDFD)
                    i = i+1
            elif (moves[i+1] == 'U'):
                output.append(FDX)
                spinx = True
                moves[i+1] = 'B'
            elif (moves[i+1] == 'U\''):
                output.append(FDX)
                spinx = True
                moves[i+1] = 'B\''
            elif (moves[i+1] == 'U2'):
                output.append(FDX)
                spinx = True
                moves[i+1] = 'B2'
            elif (moves[i+1] == 'D'):
                output.append(FDX)
                spinx = True
                moves[i+1] = 'F'
            elif (moves[i+1] == 'D\''):
                output.append(FDX)
                spinx = True
                moves[i+1] = 'F\''
            elif (moves[i+1] == 'D2'):
                output.append(FDX)
                spinx = True
                moves[i+1] = 'F2'
            else:
                output.append(FD)
    ##-------------------------------------------


        elif (moves[i] == 'R'):
            if (i == len(moves)-1):
                output.append(R)
            elif (moves[i+1] == 'L'):
                output.append(RL)
                i = i+1
            elif (moves[i+1] == 'L\''):
                if (i == len(moves)-2):
                    output.append(RLP)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'R'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'R\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'R2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'L'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'L\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'L2'
                    i = i+1
                else:
                    output.append(RLP)
                    i = i+1
            elif (moves[i+1] == 'L2'):
                if (i == len(moves)-2):
                    output.append(RLD)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'R'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'R\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'R2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'L'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'L\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'L2'
                    i = i+1
                else:
                    output.append(RLD)
                    i = i+1
            elif (moves[i+1] == 'U'):
                output.append(RY)
                spiny = True
                moves[i+1] = 'R'
            elif (moves[i+1] == 'U\''):
                output.append(RY)
                spiny = True
                moves[i+1] = 'R\''
            elif (moves[i+1] == 'U2'):
                output.append(RY)
                spiny = True
                moves[i+1] = 'R2'
            elif (moves[i+1] == 'D'):
                output.append(RY)
                spiny = True
                moves[i+1] = 'L'
            elif (moves[i+1] == 'D\''):
                output.append(RY)
                spiny = True
                moves[i+1] = 'L\''
            elif (moves[i+1] == 'D2'):
                output.append(RY)
                spiny = True
                moves[i+1] = 'L2'
            else:
                output.append(R)
        elif (moves[i] == 'R\''):
            if (i == len(moves)-1):
                output.append(RP)
            elif (moves[i+1] == 'L'):
                output.append(RPL)
                i = i+1
            elif (moves[i+1] == 'L\''):
                output.append(RPLP)
                i = i+1
            elif (moves[i+1] == 'L2'):
                output.append(RPLD)
                i = i+1
            else:
                output.append(RP)
        elif (moves[i] == 'R2'):
            if (i == len(moves)-1):
                output.append(RD)
            elif (moves[i+1] == 'L'):
                output.append(RDL)
                i = i+1
            elif (moves[i+1] == 'L\''):
                if (i == len(moves)-2):
                    output.append(RDLP)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'R'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'R\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'R2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'L'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'L\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'L2'
                    i = i+1
                else:
                    output.append(RDLP)
                    i = i+1
            elif (moves[i+1] == 'L2'):
                if (i == len(moves)-2):
                    output.append(RDLD)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'R'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'R\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'R2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'L'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'L\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'L2'
                    i = i+1
                else:
                    output.append(RDLD)
                    i = i+1
            elif (moves[i+1] == 'U'):
                output.append(RDY)
                spiny = True
                moves[i+1] = 'R'
            elif (moves[i+1] == 'U\''):
                output.append(RDY)
                spiny = True
                moves[i+1] = 'R\''
            elif (moves[i+1] == 'U2'):
                output.append(RDY)
                spiny = True
                moves[i+1] = 'R2'
            elif (moves[i+1] == 'D'):
                output.append(RDY)
                spiny = True
                moves[i+1] = 'L'
            elif (moves[i+1] == 'D\''):
                output.append(RDY)
                spiny = True
                moves[i+1] = 'L\''
            elif (moves[i+1] == 'D2'):
                output.append(RDY)
                spiny = True
                moves[i+1] = 'L2'
            else:
                output.append(RD)

    ##-------------------------------------------
        elif (moves[i] == 'L'):
            if (i == len(moves)-1):
                output.append(L)
            elif (moves[i+1] == 'R'):
                output.append(RL)
                i = i+1
            elif (moves[i+1] == 'R\''):
                output.append(RPL)
                i = i+1
            elif (moves[i+1] == 'R2'):
                output.append(RDL)
                i = i+1
            else:
                output.append(L)
        elif (moves[i] == 'L\''):
            if (i == len(moves)-1):
                output.append(LP)
            elif (moves[i+1] == 'R'):
                if (i == len(moves)-2):
                    output.append(RLP)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'R'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'R\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'R2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'L'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'L\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(RLPY)
                    spiny = True
                    moves[i+2] = 'L2'
                    i = i+1
                else:
                    output.append(RLP)
                    i = i+1 
            elif (moves[i+1] == 'R\''):
                output.append(RPLP)
                i = i+1
            elif (moves[i+1] == 'R2'):
                if (i == len(moves)-2):
                    output.append(RDLP)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'R'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'R\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'R2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'L'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'L\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(RDLPY)
                    spiny = True
                    moves[i+2] = 'L2'
                    i = i+1
                else:
                    output.append(RDLP)
                    i = i+1
            elif (moves[i+1] == 'U'):
                output.append(LPY)
                spiny = True
                moves[i+1] = 'R'
            elif (moves[i+1] == 'U\''):
                output.append(LPY)
                spiny = True
                moves[i+1] = 'R\''
            elif (moves[i+1] == 'U2'):
                output.append(LPY)
                spiny = True
                moves[i+1] = 'R2'
            elif (moves[i+1] == 'D'):
                output.append(LPY)
                spiny = True
                moves[i+1] = 'L'
            elif (moves[i+1] == 'D\''):
                output.append(LPY)
                spiny = True
                moves[i+1] = 'L\''
            elif (moves[i+1] == 'D2'):
                output.append(LPY)
                spiny = True
                moves[i+1] = 'L2'
            else:
                output.append(LP)
        elif (moves[i] == 'L2'):
            if (i == len(moves)-1):
                output.append(LD)
            elif (moves[i+1] == 'R'):
                if (i == len(moves)-2):
                    output.append(RLD)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'R'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'R\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'R2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'L'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'L\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(RLDY)
                    spiny = True
                    moves[i+2] = 'L2'
                    i = i+1
                else:
                    output.append(RLD)
                    i = i+1
            elif (moves[i+1] == 'R\''):
                output.append(RPLD)
                i = i+1
            elif (moves[i+1] == 'R2'):
                if (i == len(moves)-2):
                    output.append(RDLD)
                    i = i+1
                elif (moves[i+2] == 'U'):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'R'
                    i = i+1
                elif (moves[i+2] == 'U\''):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'R\''
                    i = i+1                
                elif (moves[i+2] == 'U2'):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'R2'
                    i = i+1
                elif (moves[i+2] == 'D'):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'L'
                    i = i+1
                elif (moves[i+2] == 'D\''):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'L\''
                    i = i+1                
                elif (moves[i+2] == 'D2'):
                    output.append(RDLDY)
                    spiny = True
                    moves[i+2] = 'L2'
                    i = i+1
                else:
                    output.append(RDLD)
                    i = i+1
            elif (moves[i+1] == 'U'):
                output.append(LDY)
                spiny = True
                moves[i+1] = 'R'
            elif (moves[i+1] == 'U\''):
                output.append(LDY)
                spiny = True
                moves[i+1] = 'R\''
            elif (moves[i+1] == 'U2'):
                output.append(LDY)
                spiny = True
                moves[i+1] = 'R2'
            elif (moves[i+1] == 'D'):
                output.append(LDY)
                spiny = True
                moves[i+1] = 'L'
            elif (moves[i+1] == 'D\''):
                output.append(LDY)
                spiny = True
                moves[i+1] = 'L\''
            elif (moves[i+1] == 'D2'):
                output.append(LDY)
                spiny = True
                moves[i+1] = 'L2'
            else:
                output.append(LD)
        i = i+1
        j = i+1
        if (spinx):
            while j < len(moves):
                if moves[j] == 'U':
                    moves[j] = 'B'
                elif moves[j] == 'U\'':
                    moves[j] = 'B\''
                elif moves[j] == 'U2':
                    moves[j] = 'B2'
                elif moves[j] == 'B':
                    moves[j] = 'D'
                elif moves[j] == 'B\'':
                    moves[j] = 'D\''
                elif moves[j] == 'B2':
                    moves[j] = 'D2'
                elif moves[j] == 'D':
                    moves[j] = 'F'
                elif moves[j] == 'D\'':
                    moves[j] = 'F\''
                elif moves[j] == 'D2':
                    moves[j] = 'F2'
                elif moves[j] == 'F':
                    moves[j] = 'U'
                elif moves[j] == 'F\'':
                    moves[j] = 'U\''
                elif moves[j] == 'F2':
                    moves[j] = 'U2'
                j = j+1
        if (spiny):
            while j < len(moves):
                if moves[j] == 'U':
                    moves[j] = 'R'
                elif moves[j] == 'U\'':
                    moves[j] = 'R\''
                elif moves[j] == 'U2':
                    moves[j] = 'R2'
                elif moves[j] == 'R':
                    moves[j] = 'D'
                elif moves[j] == 'R\'':
                    moves[j] = 'D\''
                elif moves[j] == 'R2':
                    moves[j] = 'D2'
                elif moves[j] == 'D':
                    moves[j] = 'L'
                elif moves[j] == 'D\'':
                    moves[j] = 'L\''
                elif moves[j] == 'D2':
                    moves[j] = 'L2'
                elif moves[j] == 'L':
                    moves[j] = 'U'
                elif moves[j] == 'L\'':
                    moves[j] = 'U\''
                elif moves[j] == 'L2':
                    moves[j] = 'U2'
                j = j+1

    output_format = []
    for i in range(len(output)):
        if output[i] == 0:
            output_format.append('B')
        if output[i] == 1:
            output_format.append('R')
        if output[i] == 2:
            output_format.append('F')
        if output[i] == 3:
            output_format.append('L')
        if output[i] == 4:
            output_format.append('BP')
        if output[i] == 5:
            output_format.append('RP')
        if output[i] == 6:
            output_format.append('FP')
        if output[i] == 7:
            output_format.append('LP')
        if output[i] == 8:
            output_format.append('BD')
        if output[i] == 9:
            output_format.append('RD')
        if output[i] == 10:
            output_format.append('FD')
        if output[i] == 11:
            output_format.append('LD')
        if output[i] == 12:
            output_format.append('BF')
        if output[i] == 13:
            output_format.append('BPF')
        if output[i] == 14:
            output_format.append('BFP')
        if output[i] == 15:
            output_format.append('BPFP')
        if output[i] == 16:
            output_format.append('BDF')
        if output[i] == 17:
            output_format.append('BFD')
        if output[i] == 18:
            output_format.append('BDFD')
        if output[i] == 19:
            output_format.append('BPFD')
        if output[i] == 20:
            output_format.append('BDFP')
        if output[i] == 21:
            output_format.append('RL')
        if output[i] == 22:
            output_format.append('RPL')
        if output[i] == 23:
            output_format.append('RLP')
        if output[i] == 24:
            output_format.append('RPLP')
        if output[i] == 25:
            output_format.append('RDL')
        if output[i] == 26:
            output_format.append('RLD')
        if output[i] == 27:
            output_format.append('RDLD')
        if output[i] == 28:
            output_format.append('RPLD')
        if output[i] == 29:
            output_format.append('RDLP')
        if output[i] == 30:
            output_format.append('RY')
        if output[i] == 31:
            output_format.append('RDY')
        if output[i] == 32:
            output_format.append('LPY')
        if output[i] == 33:
            output_format.append('LDY')
        if output[i] == 34:
            output_format.append('BPX')
        if output[i] == 35:
            output_format.append('BDX')
        if output[i] == 36:
            output_format.append('FX')
        if output[i] == 37:
            output_format.append('FDX')
        if output[i] == 38:
            output_format.append('BPFX')
        if output[i] == 39:
            output_format.append('BDFX')
        if output[i] == 40:
            output_format.append('BDFDX')
        if output[i] == 41:
            output_format.append('BPFDX')
        if output[i] == 42:
            output_format.append('RLPY')
        if output[i] == 43:
            output_format.append('RLDY')
        if output[i] == 44:
            output_format.append('RDLDY')
        if output[i] == 45:
            output_format.append('RDLPY')
        if output[i] == 46:
            output_format.append('X')
        if output[i] == 47:
            output_format.append('Y')
    print output
    print output_format
    print len(output_format)























