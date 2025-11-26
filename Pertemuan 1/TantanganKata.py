def SusunKata(Kata, Ascii):
    character = []
    character = ''.join(chr(num) for num in Ascii)

    kata_list = list(Kata)
    temp = ""
    found = True

    for i in character:
        if i in kata_list:
            temp += i
            indeks = kata_list.index(i)
            kata_list.pop(indeks)
        else:
            found = False
            break

    if found:
        print("Bisa")
        return temp
    else:
        print("Tidak")
        return temp

Kata = str(input())
Ascii = list(map(int, input().split()))

print(SusunKata(Kata, Ascii))