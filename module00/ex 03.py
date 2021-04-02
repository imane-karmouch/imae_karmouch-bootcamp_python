        
def text_analyzer(text):
    if text=='':
        print("the text is empty")
    M=0
    m=0
    S=0
    p=0
    for char in text:
        if (ord(char)<=90 and ord(char)>=65):
            M+=1
        if (92<=ord(char)<=122):
            m+=1
        if (ord(char)==32):
            S+=1
        if (33<=ord(char)<=47 or 58<=ord(char)<=63):
            p+=1      
    print("the number of the upper letters is:",M)
    print("the number of the lower letters is:",m)
    print("the number of spaces is:",S)
    print("the number of punctuation marks is:",p)
