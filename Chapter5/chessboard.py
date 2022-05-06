# Chess Board Configuration Validator
# Practice Project #1 from Chapter 5

# Write a function to take a dictionary input of chess pieces and positions
# Function to validate that:
#   -Each player has only 1 king
#   -Each player has at most 16 pieces
#   -Each player has at most 8 pawns
#   -Each piece can only be in a valid position
# Function should return TRUE or FALSE

def validPositions():
     files = ['a','b','c','d','e','f','g','h']
     positions = []
     for file in files:
         for rank in range(8):
             square = file + str(rank+1)
             positions.append(square)
     return positions

def pieceInventory(board):
    collection = {}
    pieceFlavors = ['bpawn','brook','bknight','bbishop','bqueen','bking','wpawn','wrook','wknight','wbishop','wqueen','wking']
    for flavor in pieceFlavors:
        collection.setdefault(flavor,0)
    pieces = list(board.items())
    for piece in pieces:
        collection.setdefault(piece,1)
        collection[piece] += 1
    return collection

def isValidSquares(board, positions):
    squaresValid = True
    for key in board.keys():
        if key in positions:
            continue
        else: 
            squaresValid = False
            break
    return squaresValid
    
def isValidPawns(inventory):
    validPawns = True
    for pawn in ('bpawn','wpawn'):
        if inventory[pawn] <= 2:
            continue
        else:
            validPawns = False
            break
    return validPawns

def isValidPieceCounts(inventory):
    bTotal = inventory['bpawn']+inventory['brook']+inventory['bknight']+inventory['bbishop']+inventory['bqueen']+inventory['bking']
    wTotal = inventory['wpawn']+inventory['wrook']+inventory['wknight']+inventory['wbishop']+inventory['wqueen']+inventory['wking']
    bCountsValid = (bTotal <= 16)
    wCountsValid = (wTotal <= 16)
    validCounts = bCountsValid and wCountsValid
    return validCounts

def isValidKings(inventory):
    validKing = True
    for king in ('bking','wking'):
        if inventory[king] > 1:
            validKing = False
            break
        else:
            continue
    return validKing

def isValidChessBoard(board):
    positions = validPositions()
    inventory = pieceInventory(board)
    squaresValid = isValidSquares(board, positions)
    pawnCountValid = isValidPawns(inventory)
    pieceCountsValid = isValidPieceCounts(inventory)
    kingCountsValid = isValidKings(inventory)
    if (inventory and positions and squaresValid and pawnCountValid and pieceCountsValid and kingCountsValid):
        validityCheck = True
    else:
        validityCheck = False
    return validityCheck

    
boardConfig = {"a1":"bking","h8":"wking", "h7":"wpawn"}
checkValid = isValidChessBoard(boardConfig)
print(checkValid)