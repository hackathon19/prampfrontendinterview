def solve( A, B):
    i = 0
    ans = 0
    while(i < len(A)):
        j = i+B-1
        if(j >= len(A)):
            j = len(A)-1
        while( j > i and A[j] != 1 ):
            j -= 1
        
        if( A[j] == 1 ):
            ans += 1
            if((j+B-1)+1 >= len(A)):
                return ans
            i = (j+B-1)+1
        else:
            j = i-1
            if( j < 0):
                return -1
            if( j < (i-B+1)):
                return -1
            
            while( j > (i-B+1) and A[j] != 1 ):
                j -= 1
            if( A[j] == 1 ):
                ans += 1
                if((j+B-1)+1 >= len(A)):
                    return ans
                i = (j+B-1)+1
            else:
                return -1

        print("jump",i)

    while(i < len(A)):
        j = i-1
        if( j < 0):
            return -1
        if( j < (i-B+1)):
            return -1
        while(j < 0):
            j += 1
        while(  j > (i-B+1) and A[j] != 1 ):
            j -= 1
        if( A[j] == 1 ):
            ans += 1
            if((j+B-1)+1 >= len(A)):
                return ans
            i = (j+B-1)+1
        else:
            return -1
        print("jumpo",i)


A = [ 1, 1, 1 ]
B = 6
print(len(A))                 

ans = solve( A, B)
print(ans)       

            
    

