#Arithmetic Operators
a=10
b=20
print("Addtions(+):",a+b)#Addtions(+): 30
print("Subraction(-):",a-b)#Subraction(-): -10
print("Multiplication(*):",a*b)#Multiplication(*): 200
print("div(/):",a/b)#div(/): 0.5
print("FloDiv(//):",a//b)#FloDiv(//): 0
print("Mod(%):",a%b)#Mod(%): 10
print("Exp(**):",a**b)#Exp(**): 100000000000000000000



#Comparison Operators
c = 22
b = 33
print("Equal to(==)",c==b)#Equal to(==) False
d='ramya'
e='raju'
print("Not Equal to(!=):",d!=e)#Not Equal to(!=): True
print("Greater then(>):",a>b)#Greater then(>): False
print("Less than(<):",c<b)#Less than(<): True
print("Greater then or Equal to(>=)",c>=b)#Greater then or Equal to(>=) False
print("Less than or Equal to(<=)",a<=c)#Less than or Equal to(<=) True



#Assignment Operators
'''var=var(op)(val)
e=e+10
var(op)=val
e+=10
'''
x=5
print("Assign(=):",x)#Assign(=): 5
x+=20
print("Add & Assign(+=):",x)#Add & Assign(+=): 25
x-=8
print("Sub & Assign(-=):",x)#Sub & Assign(-=): 17
x*=10
print("Mul & Assign(*=):",x)#Mul & Assign(*=): 170
x/=2
print("Div & Assign(/=):",x)#Div & Assign(/=): 85.0
x//=3
print("FlooDiv & Assign(//=):",x)#FlooDiv & Assign(//=): 28.0
x%=3
print("Module & Assign(%=):",x)#Module & Assign(%=): 1.0
x**=4
print("Expo & Assign(**=):",x)#Expo & Assign(**=): 1.0



#Logical Operators
'''
=====AND=====
T AND T = T
T AND F = F
F AND T = F
F AND F = F

=====OR=====
T OR T = T
T OR F = T
F OR T = T
F OR F = F

=====NOT=====
NOT T = F
NOT F = T

'''
y=10
z=20
print("AND(and):", y%10==0 and z%10==0)#AND(and): False
print("OR(or):", y%5==0 or z%9==0)#OR(or): True
print("NOT(not):", not(y>z))#NOT(not): True


#Membership Operators
list = [10,20,30,40]
print("In(in):", 30 in list)#In(in): True
print("Not In (not in):", 20 not in list)#Not In (not in): False



#Identity Operators
l= [9,7,6,5]
o = l
m =[9,7,6,5]
print("IS(is):",l is o)#IS(is): False
print("IS(is):",l is m)#IS(is): False(Different object with same contant but different memory location)
print("IS NOT(is not):", l is not m)#IS NOT(is not): True



#Bitwise Operators
print("AND(&):",y & z)#AND(&): 0
print("OR(|):",y|z)#OR(|): 30
print("XOR(^):",y ^ z)#XOR(^): 30
print("NOT(~):",~z)#NOT(~): -21
print("LEFT SHIFT(<<):",y << z)#LEFT SHIFT(<<): 10485760
print("RIGHT SHIFT(>>):",y >> z)#RIGHT SHIFT(>>): 0

