a = (input("Masukan bilangan A:"))
b = (input("Masukan bilangan B:"))
c = (input("Masukan bilangan C:"))

if a>b and a>c:
    if b>c:
        print(a,'terbesar dan' , c,' terkecil')
    else:
        print (a, 'terbesar dan' , b,'terkecil')
elif b>a and b>c:
    if a>c:
         print (b, 'terbesar dan' , c,'terkecil')
