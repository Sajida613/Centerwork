def lines():
    line = int(input("Enter a number of lines = "))
    for i in range(1, line+1):
        for j in range(i+1):
            print("*",end=" ")
        print()

    return ("The {lines}   number of triangle has been created")
    
triangle = lines()
print(triangle)    


   