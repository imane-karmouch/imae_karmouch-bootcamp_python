def operation(nb1,nb2):
    if type(nb1)==str or type(nb2)==str:
        print("ERROR")
   
    else:
        S=nb1+nb2
        D=nb1-nb2
        P=nb1*nb2
    
        if nb2!=0:
            Q=nb1/nb2
            R=nb1%nb2
        else:
            Q="ERROR"
            R="ERROR"
        print("Sum=",S)
        print("Difference=",D)
        print("Product=",P )   
        print("Quotient=",Q)
        print("Remainder=",R)
