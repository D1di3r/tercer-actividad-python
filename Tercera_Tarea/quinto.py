def BinDec(n):
    s=0
    i=0
    print("El binario ",n,end='')
    while(n>=1):
        d=n%10;
        n=int(n/10);
        s=s+d*pow(2,i);
        i=i+1

        print("Corresponde al numero ",s)
def DecBin(n):
   d=[]
   print("El numero",n,end='')
   while(n>=1):
        d.append(n%2);
        n=int(n/2)
        s=d[::-1]

        print("Corresponde al binario ",end='')
        print(s)
        for k in s:
            print(k,end='')

BinDec(1101)
DecBin(13)

        