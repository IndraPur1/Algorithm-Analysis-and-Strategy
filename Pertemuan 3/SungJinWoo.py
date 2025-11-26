def hitung_kombinasi(nums1, nums2):
    indeks_nums2 = {nilai: i for i, nilai in enumerate(nums2)}
    nums1_dalam_nums2 = [indeks_nums2[x] for x in nums1]

    def count_lis_triplets(arr):
        n = len(arr)
        kiri = [0] * n
        kanan = [0] * n

        for i in range(n):
            kiri[i] = 1
            for j in range(i):
                if arr[j] < arr[i]:
                    kiri[i] += 1

        for i in range(n-1, -1, -1):
            kanan[i] = 1
            for j in range(i+1, n):
                if arr[i] < arr[j]:
                    kanan[i] += 1
        
        return sum((kiri[i] - 1) * (kanan[i] - 1) for i in range(n))

    return count_lis_triplets(nums1_dalam_nums2)

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(hitung_kombinasi(nums1, nums2))