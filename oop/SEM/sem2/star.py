h = 5
w=h*2-1
for i in range(0, h):
    for k in range ((w-2*i +1)//2):
        print( " ",end = "" )
    for k in range (2*i +1):
        print( "*",end = "" )

    print()