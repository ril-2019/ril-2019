arr = []
i = 0
moyenne = 0

while i < 10:
    arr.append(int(input("entier : ")))
    i += 1

for i in range(len(arr)):
    moyenne += arr[i] / len(arr)

print(moyenne)