def gugudan(n):
    for i in range(1,n):
        for j in range(1,n):
            print(i," x ",j, " = ", i*j,  end="\t")
        print()

gugudan(10)

def add(a,b):
    """
    (int, int)-->(int,int)
    This function take two integer values and adds them.
    """
    return a+b

