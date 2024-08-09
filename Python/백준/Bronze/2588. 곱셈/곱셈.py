A,B = (int(input()),int(input()))
B1,B2,B3 = (B//100,B%100//10,B%10)
print(B3*A,B2*A,B1*A,A*B,sep='\n')
