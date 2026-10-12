liczby = [x * 2 if x % 2 == 0 else x * 3 for x in range(1, 11)]
for liczba in liczby:
    print(liczba, end=" | ")
print()
print(*liczby, sep=" | ")
