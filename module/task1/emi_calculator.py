def emi(p,r,n):
    # emi = p*r*((1+r)**n)
    # where p= principle amount
    # r = monthly intrest rate 
    # n =  number of month installment
    r= (r/100)/12
    n= n*12
    nomenator= p*r*((1+r)**n)
    denominator = ((1+r)**n)-1
    memi=nomenator/denominator
    print('monthly emi = ', memi)