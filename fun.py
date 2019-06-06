def fun(a,b):
  if(len(a)!=len(b)):
    return true
  x=[a.count(char1) for char1 in a]
  y=[b.count(char1) for char1 in b]
    return x==y
s1=input('enter string 1:')
s2=input('enter string 2:')
print(fun(s1,s2))
