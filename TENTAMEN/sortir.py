def proses_paket(n, q, paket, query):
    paket_urut = sorted(paket)  
    hasil = [str(paket_urut[i - 1]) for i in query if 1 <= i <= n]  
    return " ".join(hasil)  

def main():
    n, q = map(int, input().split())  
    paket = list(map(int, input().split()))  
    query = list(map(int, input().split()))  
    print(proses_paket(n, q, paket, query))  

if __name__ == "__main__":  
    main()