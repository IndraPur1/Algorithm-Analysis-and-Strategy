def Problem(nakal):
    def mergesort(nakal, kiri, kanan):
        if kiri >= kanan:
            return 0
        mid = (kiri + kanan) // 2
        error = mergesort(nakal, kiri, mid)
        error += mergesort(nakal, mid + 1, kanan)
        error += merge(nakal, kiri, mid, kanan)
        return error

    def merge(nakal, kiri, tengah, kanan):
        left = nakal[kiri:tengah + 1]
        right = nakal[tengah + 1:kanan + 1]
        
        i = j = 0
        k = kiri
        error = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nakal[k] = left[i]
                i += 1
            else:
                nakal[k] = right[j]
                j += 1
                error += len(left) - i
            k += 1

        while i < len(left):
            nakal[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nakal[k] = right[j]
            j += 1
            k += 1
        return error
    return mergesort(nakal, 0, len(nakal) - 1)

n = int(input())
nakal = list(map(int, input().split()))

print(Problem(nakal))