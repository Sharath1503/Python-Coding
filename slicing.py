name = "Vijay Deenanath Chauhan"
print(name[::-1])

x = [1,2,3,4,5,6,7,8,9]
for item in x[::-1]:
    print(item)
    
#reverse a list in place
a = [1,2,3,4,5]
print(a[:]) # get all elements
print(a[::-1]) # get all elements in reverse order

#rotate list
x = [1,2,3,4,5]
print(x[2:] + x[:2]) #rotate left by 2
print(x[-2:] + x[:-2]) #rotate right by 2

#list comprehension
x=[1,2,3,4,5]
x2 = []
for i in x:
    s = i*2
    x2.append(s)
print(x,x2)

x=[4,8,12,16]
x3 = []
for i in x:
    x3.append(i//2)
print(x,x3)

x = [1,2,3]
y = [4,5,6]
xy = []
for i,j in zip(x,y):
    xy.append(i+j)
print(x,y,xy,sep="\n")

z = [2,3,4]
zsqr = []
for i in z:
    zsqr.append(i**2)
print(z,zsqr,sep="\n")

y = [1,2,3]
ysqr = [i**2 for i in y]
print(y,ysqr,sep="\n")