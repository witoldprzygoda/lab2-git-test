import time
for znak in "|/-\\" * 10:      # albo ".oOo" * 10
    print(znak, end="", flush=True)
    time.sleep(0.2)
    print("\r", end="", flush=True)
print("gotowe")
