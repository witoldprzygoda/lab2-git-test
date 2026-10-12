wejscie = input("Podaj słowa oddzielone przecinkami: ")
wejscie = wejscie.strip().replace(",,", ",")
lista_slow = [slowo.strip().lower() for slowo in wejscie.split(",") if slowo.strip()]
print("Lista słów:", lista_slow)
print("Liczba słów:", len(lista_slow))
