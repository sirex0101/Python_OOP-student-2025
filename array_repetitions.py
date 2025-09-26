from time import time

print("REPETITIONS: ", end="")
REPETITIONS = 20_000
while REPETITIONS <= 200_000:
    print(REPETITIONS, end="")
    REPETITIONS += 20_000
    if REPETITIONS <= 200_000:
        print(", ", end="")
print("\n")

print("append: ", end="")
REPETITIONS = 20_000
while REPETITIONS <= 200_000:
    start = time()
    arr = []
    for _ in range(REPETITIONS):
        arr.append(5)
    stop = time()
    print(stop - start, end="")
    if REPETITIONS < 200_000:
        print(", ", end="")
    REPETITIONS += 20_000
print("\n")

print("pop: ", end="")
REPETITIONS = 20_000
while REPETITIONS <= 200_000:
    arr = []
    for _ in range(REPETITIONS):
        arr.append
    start = time()
    for _ in range(REPETITIONS):
        arr.pop
    stop = time()
    print(stop - start, end="")
    if REPETITIONS < 200_000:
        print(", ", end="")
    REPETITIONS += 20_000
print("\n")

print("insert(0, 5): ", end="")
REPETITIONS = 20_000
while REPETITIONS <= 200_000:
    start = time()
    arr = []
    for _ in range(REPETITIONS):
        arr.insert(0, 5)
    stop = time()
    print(stop - start, end="")
    if REPETITIONS < 200_000:
        print(", ", end="")
    REPETITIONS += 20_000
print("\n")

print("pop(0): ", end="")
REPETITIONS = 20_000
while REPETITIONS <= 200_000:
    arr = []
    for _ in range(REPETITIONS):
        arr.append(5)
    start = time()
    for _ in range(REPETITIONS):
        arr.pop(0)
    stop = time()
    print(stop - start, end="")
    if REPETITIONS < 200_000:
        print(", ", end="")
    REPETITIONS += 20_000
print("\n")