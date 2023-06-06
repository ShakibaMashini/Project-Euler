##The prime factors of 13195 are 5, 7, 13 and 29.
##What is the largest prime factor of the number 600851475143 ?

n = int(input("n ="))
for i in range(2,n+1):
    if n % i ==0:
        is_prime = True
        for item in range(2,i):
             if i % item == 0:
                 is_prime = False
                 break
        if (is_prime) :
            print(i)
            
            
        

