#7.​ Define una función que cuente cuántas vocales tiene una palabra.

print("Digite una palabra")
palabra=input()

def cont_vocal (a):
    count=0
    for i in a:
        if "a"==i:
            count+=1
        elif "e"==i:
            count+=1
        elif "i"==i:
            count+=1
        elif "o"==i:
            count+=1
        elif "u"==i:
            count+=1
    return count

print(cont_vocal(palabra))