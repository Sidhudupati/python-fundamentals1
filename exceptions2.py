def remainder(a,b):
    if(b==0):
        raise Exception('Divisor cannot be 0')
    result=a//b
    remainder=a%b
    print("Result is ",result,"and remainder is",remainder)
remainder(10,0)
