#lambda:
x=lambda a:a+10
print(x(5))

x=lambda a,b:a*b
print(x(2,5))

#lambda in functions:
def fuct(n):
    return lambda a:a*n
result=fuct(2)
print(result(3))
frame=pd.DataFrame(np.arange(9).reshape(3,3),index=[1,2,3],
                   columns=['x','y','z'])
frame
f=lambda x: x.max()-x.min()
frame.apply(f)
frame.apply(f,axis='columns')

def f(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])
frame.apply(f)

format=lambda x:'%.2f'% x
format(2)
format(1)
format(400)
frame.applymap(format)

f=lambda x:x**2
frame.apply(f)
frame.applymap(f)


