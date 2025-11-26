#include <stdio.h>

void identityMatrix(int n) {
    int matrix[n][n];

    // Mengisi matriks dengan 1 di diagonal utama dan 0 di tempat lain
    for (int i = 1; i < n; i++) {  // Loop pertama (baris)
        for (int j = 1; j < n; j++) {  // Loop kedua (kolom)
            if (i == j)
                matrix[i][j] = 1;  // Isi diagonal utama dengan 1
            else
                matrix[i][j] = 0;  // Isi lainnya dengan 0
        }
    }

    // Mencetak matriks
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int n = 5; // Ukuran matriks (bisa diubah)
    identityMatrix(n);
    return 0;
}