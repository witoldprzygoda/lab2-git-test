from time import sleep
END = " "
FLUSH = False
for i in range(10):
    print(i, end=END, flush=FLUSH)
    sleep(0.5)
print()
