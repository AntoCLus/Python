# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Enter row #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)

ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Check if all columns are good.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Make a string containing all digits from a sub-square.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")
class Sudoku:
    def __init__(self):
        pass


def expandLine(row):
    return row[0]+row[5:9].join([row[1:5]*(base-1)]*base)+row[9:13]
row0  = expandLine("╔═══╤═══╦═══╗")
row1  = expandLine("║ . │ . ║ . ║")
row2  = expandLine("╟───┼───╫───╢")
row3  = expandLine("╠═══╪═══╬═══╣")
row4  = expandLine("╚═══╧═══╩═══╝")

symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums   = [ [""]+[symbol[n] for n in row] for row in board ]
print(row0)
for r in range(1,side+1):
    print( "".join(n+s for n,s in zip(nums[r-1],row1.split("."))) )
    print([row2,row3,row4][(r%side==0)+(r%base==0)])