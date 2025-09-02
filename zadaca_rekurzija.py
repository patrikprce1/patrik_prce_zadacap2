def obrnuto(strr):
    if strr=="":
        return ""
    else:
        return obrnuto(strr[1:])+strr[0]
unos=str(input("Unesi neki string"))
print(obrnuto(unos))
