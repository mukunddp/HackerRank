# Enter your code here. Read input from STDIN. Print output to STDOUT
d = int(input(""))
for i in range(0, d):
    a = input("")

    b = a[0:len(a): 2]
    c = a[1:len(a):2]
    print(b, c)
