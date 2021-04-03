def filtrer(phrase,n):
    L=[]
    phrase=phrase.split()
    for i in range(len(phrase)):
        if  len(phrase[i])>=n:
            L.append(phrase[i])
    return L
