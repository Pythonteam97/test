def Prime(n):
    if(n==0 or n==1):
        return 'false'
    else:
        i=2
        while i<n:
            if(n%i==0):
                return 'false';
            i+=1;
        return 'true'
    
