import time

start = time.time()
count=0

while time.time() - start < 1 :
    count += 1

print("iterasi dalam 1 detik :", count)