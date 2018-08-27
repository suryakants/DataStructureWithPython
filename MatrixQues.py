# A matrix m*n is given. If a cell contains 0 (zero) make that row and column zero.


def matrixPrint(arr, m, n):
    for i in arr:
        for j in i:
            print(j, end = " ");
        print("\n");

def makeZeroToColRow(arr, m, n):
    for i in range(m):
        m[i][n] = 0;
    for j in range(n):
        m[m][j] = 0;
    return arr;

def zerofyMatrix(arr, m, n):
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                #do some stuff here
                arr = makeZeroToColRow(arr, i, j);
    return arr;

t = [
     [11, 0, 2],
     [15, 6,0],
     [10, 12, 5]
    ];
matrixPrint(t, 3,3);
t = zerofyMatrix(t, 3,3);
matrixPrint(t, 3,3);
