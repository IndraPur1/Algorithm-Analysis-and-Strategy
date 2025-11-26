# Fungsi untuk menjumlahkan dua matriks ukuran n x n
def matrix_add(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

# Fungsi untuk menyalin submatriks dari matriks utama A
# dengan ukuran 'size' dimulai dari baris dan kolom tertentu
def copy_submatrix(A, start_row, start_col, size):
    return [
        [A[start_row + i][start_col + j] for j in range(size)]
        for i in range(size)
    ]

# Fungsi untuk menyisipkan submatriks ke dalam matriks C
# di posisi baris dan kolom yang ditentukan
def merge_submatrix(C, submatrix, start_row, start_col):
    size = len(submatrix)
    for i in range(size):
        for j in range(size):
            C[start_row + i][start_col + j] = submatrix[i][j]
    return C

# Fungsi utama untuk mengalikan dua matriks dengan metode Divide and Conquer
def multiply_matrix(A, B):
    n = len(A)  # Ukuran matriks A (dan juga B)

    # Basis rekursi: matriks ukuran 1x1 → kalikan langsung
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    k = n // 2  # Bagi matriks menjadi empat bagian ukuran n/2 x n/2

    # Bagi matriks A menjadi 4 submatriks
    A11 = copy_submatrix(A, 0, 0, k)
    A12 = copy_submatrix(A, 0, k, k)
    A21 = copy_submatrix(A, k, 0, k)
    A22 = copy_submatrix(A, k, k, k)

    # Bagi matriks B menjadi 4 submatriks
    B11 = copy_submatrix(B, 0, 0, k)
    B12 = copy_submatrix(B, 0, k, k)
    B21 = copy_submatrix(B, k, 0, k)
    B22 = copy_submatrix(B, k, k, k)

    # Hitung Cij berdasarkan formula divide and conquer
    C11 = matrix_add(multiply_matrix(A11, B11), multiply_matrix(A12, B21))
    C12 = matrix_add(multiply_matrix(A11, B12), multiply_matrix(A12, B22))
    C21 = matrix_add(multiply_matrix(A21, B11), multiply_matrix(A22, B21))
    C22 = matrix_add(multiply_matrix(A21, B12), multiply_matrix(A22, B22))

    # Gabungkan 4 submatriks Cij menjadi matriks hasil akhir C
    C = [[0] * n for _ in range(n)]
    merge_submatrix(C, C11, 0, 0)       # Tempatkan C11 di kiri atas
    merge_submatrix(C, C12, 0, k)       # Tempatkan C12 di kanan atas
    merge_submatrix(C, C21, k, 0)       # Tempatkan C21 di kiri bawah
    merge_submatrix(C, C22, k, k)       # Tempatkan C22 di kanan bawah

    return C  # Kembalikan matriks hasil A × B

# Input ukuran N → ukuran matriks adalah 2^N × 2^N
N = int(input())
size = 2 ** N

# Input matriks A sebanyak size baris
A = [list(map(int, input().split())) for _ in range(size)]

# Input matriks B sebanyak size baris
B = [list(map(int, input().split())) for _ in range(size)]

# Kalikan kedua matriks menggunakan metode rekursif
C = multiply_matrix(A, B)

# Cetak hasil akhir matriks C baris per baris
for row in C:
    print(" ".join(map(str, row)))