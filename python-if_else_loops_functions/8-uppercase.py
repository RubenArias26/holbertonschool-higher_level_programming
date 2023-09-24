def uppercase(str):
    for v in str:
        if ord(v) >= 97 and ord(v) <= 122:
            v = chr(ord(v) - 32)
        print("{}".format(v), end="")
    print("")
