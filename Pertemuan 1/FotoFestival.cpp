#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
    int baris, kolom;
    cin >> baris >> kolom;

    vector<vector<int>> matriks(baris, vector<int>(kolom));

    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            cin >> matriks[i][j];
        }
    }
    
    int jumlahMaksimum = INT_MIN; 
    int ukuranMaksimum = 1;      
    int barisAwal = 0;           
    int kolomAwal = 0;            

    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            for (int ukuran = 1; i + ukuran <= baris && j + ukuran <= kolom; ukuran++) {
                int jumlahSaatIni = 0;
                for (int x = 0; x < ukuran; x++) {
                    for (int y = 0; y < ukuran; y++) {
                        jumlahSaatIni += matriks[i + x][j + y];
                    }
                }
                if (jumlahSaatIni > jumlahMaksimum) {
                    jumlahMaksimum = jumlahSaatIni;
                    ukuranMaksimum = ukuran;
                    barisAwal = i;
                    kolomAwal = j;
                }
                else if (jumlahSaatIni == jumlahMaksimum && ukuranMaksimum < ukuran) {
                    jumlahMaksimum = jumlahSaatIni;
                    ukuranMaksimum = ukuran;
                    barisAwal = i;
                    kolomAwal = j;
                }
            }
        }
    }

    // Menampilkan hasil
    cout << jumlahMaksimum << " " << ukuranMaksimum << " " << barisAwal + 1 << " " << kolomAwal + 1 << endl;
    return 0;
}